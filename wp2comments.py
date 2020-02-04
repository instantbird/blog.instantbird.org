"""
Retrieve the WordPress comments from an XML export.
"""
import argparse
import logging
import os
import re
import subprocess
from html import unescape

# because logging.setLoggerClass has to be called before logging.getLogger
from pelican.log import init
from pelican.settings import read_settings
from pelican.tools.pelican_import import (
    decode_wp_content,
    get_ext,
    get_filename,
    get_pandoc_version,
    is_pandoc_needed,
    xml_to_soup,
)
from pelican.utils import SafeDatetime, slugify


logger = logging.getLogger(__name__)


def wp2comments(xml):
    """Opens a wordpress XML file, and yield Pelican comments"""

    soup = xml_to_soup(xml)
    items = soup.rss.channel.findAll('item')
    for item in items:
        status = item.find('status')
        if status and status.string in ["publish", "draft"]:
            # Get the list of comments.
            raw_comments = item.findAll('comment')

            post_name = item.find('post_name').string
            post_id = item.find('post_id').string
            filename = get_filename(post_name, post_id)

            comments = []
            for comment in raw_comments:
                raw_date = comment.find('comment_date').string
                if raw_date == u'0000-00-00 00:00:00':
                    date = None
                else:
                    date_object = SafeDatetime.strptime(
                        raw_date, '%Y-%m-%d %H:%M:%S')
                    date = date_object.strftime('%Y-%m-%d %H:%M')

                comment_id = comment.find('comment_id').string
                comment_author = comment.find('comment_author').string
                comment_author_email = comment.find('comment_author_email').string
                comment_author_url = comment.find('comment_author_url').string
                comment_author_IP = comment.find('comment_author_IP').string
                comment_content = comment.find('comment_content').string

                comment_approved = bool(comment.find('comment_approved').string)
                status = 'published' if comment.find('comment_approved').string == "1" \
                    else 'hidden'

                comment_type = comment.find('comment_type').string
                comment_type = 'comment' if not comment_type else comment_type
                comment_parent = int(comment.find('comment_parent').string)
                comment_user_id = comment.find('comment_user_id').string

                # TODO Generate filename?

                comments.append((
                    comment_id,
                    comment_type,
                    comment_author,
                    date,
                    comment_author_email,
                    comment_author_url,
                    comment_content,
                    status,
                    comment_parent,
                    'wp-html',
                ))

            yield (filename, comments)


def build_header(title, date, author, website, replyto, **kwargs):
    """Build a header from a list of fields"""

    from docutils.utils import column_width

    # reStructuredText documents need a title.
    header = '%s\n%s\n' % (title, '#' * column_width(title))

    header += ':date: %s\n' % date
    header += ':author: %s\n' % author
    if website:
        header += ':website: %s\n' % website
    if replyto:
        header += ':replyto: %s\n' % replyto
    for key, value in kwargs.items():
        header += ':%s: %s\n' % (key, value)
    header += '\n'
    return header


def get_out_filename(output_path, post_path, comment_filename, ext):
    filename = os.path.basename(comment_filename)

    # Enforce filename restrictions for various filesystems at once; see
    # http://en.wikipedia.org/wiki/Filename#Reserved_characters_and_words
    # we do not need to filter words because an extension will be appended
    filename = re.sub(r'[<>:"/\\|?*^% ]', '-', filename)  # invalid chars
    filename = filename.lstrip('.')  # should not start with a dot
    if not filename:
        filename = '_'
    filename = filename[:249]  # allow for 5 extra characters

    out_filename = os.path.join(output_path, post_path, filename + ext)

    return out_filename



def comments2pelican(comments, out_markup, output_path, strip_raw=False, include_pingbacks=False):
    pandoc_version = get_pandoc_version()
    posts_require_pandoc = []

    settings = read_settings()
    slug_subs = settings['SLUG_REGEX_SUBSTITUTIONS']
    comments_dir = settings.get('PELICAN_COMMENT_SYSTEM_DIR', 'comments')

    output_path = os.path.join(output_path, comments_dir)

    # Ensure the comments directory exists.
    if not os.path.exists(output_path):
        try:
            os.mkdir(output_path)
        except OSError:
            error = 'Unable to create the output folder: ' + output_path
            exit(error)

    for post_path, post_comments in comments:
        # Skip posts without comments
        if not post_comments:
            continue

        # Ensure the directory for this article exists.
        article_path = os.path.join(output_path, post_path)
        if not os.path.exists(article_path):
            try:
                os.mkdir(article_path)
            except OSError:
                error = 'Unable to create the output folder: ' + article_path
                exit(error)

        for (filename, comment_type, author, date, author_email, author_url, content, status,
                parent, in_markup) in post_comments:
            if not include_pingbacks and comment_type == 'pingback':
                continue
            if is_pandoc_needed(in_markup) and not pandoc_version:
                posts_require_pandoc.append(filename)

            ext = get_ext(out_markup, in_markup)
            if ext == '.md':
                raise RuntimeError('Not supported')
                #header = build_markdown_header(
                #    title, date, author, categories, tags, slug,
                #    status, links.values() if links else None)
            else:
                out_markup = 'rst'
                header = build_header(
                    filename, date, author, author_url, parent, status=status)

            out_filename = get_out_filename(output_path, post_path, filename, ext)
            print(out_filename)

            if in_markup in ('html', 'wp-html'):
                html_filename = os.path.join(article_path, filename + '.html')

                with open(html_filename, 'w', encoding='utf-8') as fp:
                    # Replace newlines with paragraphs wrapped with <p> so
                    # HTML is valid before conversion
                    if in_markup == 'wp-html':
                        new_content = decode_wp_content(content)
                    else:
                        paragraphs = content.splitlines()
                        paragraphs = ['<p>{0}</p>'.format(p) for p in paragraphs]
                        new_content = ''.join(paragraphs)

                    fp.write(new_content)

                if pandoc_version < (2,):
                    parse_raw = '--parse-raw' if not strip_raw else ''
                    wrap_none = '--wrap=none' \
                        if pandoc_version >= (1, 16) else '--no-wrap'
                    cmd = ('pandoc --normalize {0} --from=html'
                           ' --to={1} {2} -o "{3}" "{4}"')
                    cmd = cmd.format(parse_raw, out_markup, wrap_none,
                                     out_filename, html_filename)
                else:
                    from_arg = '-f html+raw_html' if not strip_raw else '-f html'
                    cmd = ('pandoc {0} --to={1}-smart --wrap=none -o "{2}" "{3}"')
                    cmd = cmd.format(from_arg, out_markup,
                                     out_filename, html_filename)

                try:
                    rc = subprocess.call(cmd, shell=True)
                    if rc < 0:
                        error = 'Child was terminated by signal %d' % -rc
                        exit(error)

                    elif rc > 0:
                        error = 'Please, check your Pandoc installation.'
                        exit(error)
                except OSError as e:
                    error = 'Pandoc execution failed: %s' % e
                    exit(error)

                os.remove(html_filename)

                with open(out_filename, 'r', encoding='utf-8') as fs:
                    content = fs.read()
                    if out_markup == 'markdown':
                        # In markdown, to insert a <br />, end a line with two
                        # or more spaces & then a end-of-line
                        content = content.replace('\\\n ', '  \n')
                        content = content.replace('\\\n', '  \n')

            with open(out_filename, 'w', encoding='utf-8') as fs:
                fs.write(header + content)

    if posts_require_pandoc:
        logger.error("Pandoc must be installed to import the following posts:"
                     "\n  {}".format("\n  ".join(posts_require_pandoc)))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Transform feed, Blogger, Dotclear, Posterous, Tumblr, or"
                    "WordPress files into reST (rst) or Markdown (md) files. "
                    "Be sure to have pandoc installed.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        dest='input', help='The input file to read')
    parser.add_argument(
        '-o', '--output', dest='output', default='content',
        help='Output path')
    parser.add_argument(
        '-m', '--markup', dest='markup', default='rst',
        help='Output markup format (supports rst & markdown)')
    parser.add_argument(
        '--strip-raw', action='store_true', dest='strip_raw',
        help="Strip raw HTML code that can't be converted to "
             "markup such as flash embeds or iframes (wordpress import only)")
    parser.add_argument(
        '--include-pingbacks', action='store_true', dest='include_pingbacks',
        help='Include pingbacks in imported comments')

    args = parser.parse_args()
    if not os.path.exists(args.output):
        try:
            os.mkdir(args.output)
        except OSError:
            error = 'Unable to create the output folder: ' + args.output
            exit(error)

    # init logging
    init(logging.DEBUG)
    comments = wp2comments(args.input)
    comments2pelican(comments,
                     args.markup,
                     args.output,
                     strip_raw=args.strip_raw or False,
                     include_pingbacks=args.include_pingbacks or False)
