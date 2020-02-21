#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'The Instantbird Team'
SITENAME = "The blog of Instantbird's development"
SITEURL = 'http://localhost:8000'
# The main Instantbird site's URL.
MAIN_SITE_URL = 'https://www.instantbird.com'

# Set up locations of articles, pages and theme.
PATH = 'content'
ARTICLE_PATHS = ['articles']
PAGE_PATHS = ['pages']
# Set up static content and output locations.
STATIC_PATHS = [
    'files',
    'images',
    'smileys',
    'static',
    'wp-content',
]
EXTRA_PATH_METADATA = {
    # Include a favicon.
    'static/favicon.ico': {'path': 'favicon.ico'},
}
TEMPLATE_PAGES = {
    # Custom 404 page for GitHub pages.
    '404.html': '404.html',
}

TIMEZONE = 'UTC'
DEFAULT_DATE_FORMAT = '%B %-d, %Y'

DEFAULT_LANG = 'en'

# Improve readability of HTML.
TYPOGRIFY = True

# Top-level links.
LINKS = (
    ('Blog', SITEURL),
    ('Add-ons', 'https://addons.instantbird.org/'),
    ('F.A.Q.', 'http://www.instantbird.com/faq.html'),
    ('Wiki', 'https://wiki.instantbird.org/'),
    ('About', 'http://www.instantbird.com/about.html'),
)

# This is currently a modified copy of notmyidea, one of the default themes.
THEME = 'theme'

# Configuration pagination to show 7 articles per page.
DEFAULT_PAGINATION = 7
PAGINATED_TEMPLATES = {
    'index': None,
    'tag': None,
    'category': None,
    'author': None,
    'period_archives': None,
}
PAGINATION_PATTERNS = (
    (1, '{url}', '{save_as}'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Create an archive for each year, month, and day.
YEAR_ARCHIVE_URL = '{date:%Y}/'
YEAR_ARCHIVE_SAVE_AS = YEAR_ARCHIVE_URL + 'index.html'
MONTH_ARCHIVE_URL = YEAR_ARCHIVE_URL + '{date:%m}/'
MONTH_ARCHIVE_SAVE_AS = MONTH_ARCHIVE_URL + 'index.html'
DAY_ARCHIVE_URL = MONTH_ARCHIVE_URL + '{date:%d}/'
DAY_ARCHIVE_SAVE_AS = DAY_ARCHIVE_URL + 'index.html'

# Place each article under the year & month.
ARTICLE_URL = MONTH_ARCHIVE_URL + '{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'

# Create separate archives for each author, category, and tag.
AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = AUTHOR_URL + 'index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = CATEGORY_URL + 'index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = TAG_URL + 'index.html'

# Change the default feed URLs.
FEED_ALL_RSS_URL = 'feed/'
FEED_ALL_RSS = FEED_ALL_RSS_URL + 'rss.xml'

TAG_FEED_RSS_URL = TAG_URL + 'feed/'
TAG_FEED_RSS = TAG_FEED_RSS_URL + 'rss.xml'
CATEGORY_FEED_RSS_URL = CATEGORY_URL + 'feed/'
CATEGORY_FEED_RSS = CATEGORY_FEED_RSS_URL + 'rss.xml'

AUTHOR_FEED_RSS_URL = AUTHOR_URL + 'feed/'
AUTHOR_FEED_RSS = AUTHOR_FEED_RSS_URL + 'rss.xml'

# Disable atom feeds.
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TAG_FEED_ATOM = None
AUTHOR_FEED_ATOM = None

# Disable translation feeds.
FEED_ATOM = None
FEED_RSS = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None

# Show full content in the feeds.
RSS_FEED_SUMMARY_ONLY = False
# Show 7 items in the feed.
FEED_MAX_ITEMS = 7
# The domain to serve the feeds from.
FEED_DOMAIN = SITEURL

# Match the slugification of Wordpress.
SLUG_REGEX_SUBSTITUTIONS = [
    # Only this first regular expression is modified. It replaces with a -,
    # instead of removing characters.
    (r'[^\w\s]', '-'), # replace non-alphabetical/whitespace/'-' chars with -
    (r'(?u)\A\s*', ''), # strip leading whitespace
    (r'(?u)\s*\Z', ''), # strip trailing whitespace
    (r'[-\s]+', '-'), # reduce multiple whitespace or '-' to single '-'
]

# Enable the comments system.
PELICAN_COMMENT_SYSTEM = True

# Configure permalink redirects.
REDIRECT_SAVE_AS = [
    'a{index}-{slug}.html',
    'c{index}-{slug}.html',
    'n{index}-{slug}.html',
]

# Configure the tag cloud.
TAG_CLOUD_MAX_ITEMS = 100
TAG_CLOUD_MIN_FONT = 8
TAG_CLOUD_MAX_FONT = 22
TAG_CLOUD_ORDER_BY = 'name'
TAG_CLOUD_ORDER = 'ASC'

# Configure installed plug-ins.
PLUGIN_PATHS = [
    'pelican-plugins/',
]
PLUGINS = [
    'pelican_comment_system',
    'plugins.archives',
    'plugins.comments',
    'plugins.most_used_categories',
    'plugins.redirects',
    'plugins.tag_cloud',
]
