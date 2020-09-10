"""
Create redirects from old URLs to the currently hosted URLs.

This is vaguely based on https://github.com/getpelican/pelican-plugins/blob/master/permalinks/

"""
import itertools
import logging
import os
import os.path

from pelican import signals
from pelican.generators import Generator
from pelican.utils import mkdir_p

logger = logging.getLogger(__name__)


REDIRECT_STRING = """
<!DOCTYPE HTML>
<html lang="en-US">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="refresh" content="0;url=/{url}">
        <script type="text/javascript">
            window.location.href = "{url}"
        </script>
        <title>Page Redirection to {title}</title>
    </head>
    <body>
        If you are not redirected automatically, follow the
        <a href="/{url}">link to {title}</a>
    </body>
</html>
"""


class RedirectGenerator(Generator):
    """
    Generate a redirect page for every item of content with a
    permalink_id metadata
    """

    def _get_redirect_save_as(self, article, index):
        """
        Method to get permalink ids from content. To be bound to the class last
        thing.
        """
        redirect_save_as = self.settings.get('REDIRECT_SAVE_AS', ['{slug}.html'])
        for redirect in redirect_save_as:
            # Make a copy of the metadata.
            metadata = article.metadata.copy()

            # Use 1-based indexing.
            metadata['index'] = index + 1

            redirect = redirect.format(**metadata)
            yield redirect

    def generate_context(self):
        """Setup context"""
        self.redirect_output_path = os.path.join(
            self.output_path, self.settings.get('REDIRECT_PATH', ''))

    def generate_output(self, writer=None):
        """Generate redirect files"""
        logger.info(
            'Generating permalink files in %r', self.redirect_output_path)

        mkdir_p(self.redirect_output_path)
        for i, article in enumerate(reversed(self.context['articles'])):
            # Generate an HTML redirect.
            redirect_string = REDIRECT_STRING.format(
                url=article.url,
                title=article.title)

            # Write it to each redirect path.
            for redirect_path in self._get_redirect_save_as(article, i):
                redirect_path = os.path.join(
                    self.redirect_output_path, redirect_path)

                with open(redirect_path, 'w') as f:
                    f.write(redirect_string)


class RedirectTagGenerator(Generator):
    """
    Generate a redirect page for every item of content with a
    permalink_id metadata
    """

    def _get_redirect_save_as(self, tag):
        """
        Method to get permalink ids from content. To be bound to the class last
        thing.
        """
        redirect_save_as = self.settings.get('REDIRECT_TAG_SAVE_AS', [])
        for redirect in redirect_save_as:
            redirect = redirect.format(**tag.as_dict())
            yield redirect

    def generate_context(self):
        """Setup context"""
        self.redirect_output_path = os.path.join(
            self.output_path, self.settings.get('REDIRECT_PATH', ''))

    def generate_output(self, writer=None):
        """Generate redirect files"""
        logger.info(
            'Generating permalink files in %r', self.redirect_output_path)

        for tag, _ in self.context['tags']:
            # Generate an HTML redirect.
            redirect_string = REDIRECT_STRING.format(
                url="/" + tag.url,
                title=tag.name)

            # Write it to each redirect path.
            for redirect_path in self._get_redirect_save_as(tag):
                redirect_path = os.path.join(
                    self.redirect_output_path, redirect_path)

                mkdir_p(os.path.dirname(redirect_path))

                with open(redirect_path, 'w') as f:
                    f.write(redirect_string)


def get_generators(pelican_object):
    return [RedirectGenerator, RedirectTagGenerator]


def register():
    signals.get_generators.connect(get_generators)
