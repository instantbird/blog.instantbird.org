#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'The Instantbird Team'
SITENAME = "The blog of Instantbird's development"
SITEURL = ''

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

TIMEZONE = 'UTC'
DEFAULT_DATE_FORMAT = '%B %-d, %Y'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

# This is currently a modified copy of notmyidea, one of the default themes.
THEME = 'theme'

DEFAULT_PAGINATION = 7

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Change the default URLs.
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'
AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = AUTHOR_URL + 'index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = CATEGORY_URL + 'index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = TAG_URL + 'index.html'

# Match the slugification of Wordpress.
SLUG_REGEX_SUBSTITUTIONS = [
    # Only this first regular expression is modified. It replaces with a -,
    # instead of removing characters.
    (r'[^\w\s]', '-'), # replace non-alphabetical/whitespace/'-' chars with -
    (r'(?u)\A\s*', ''), # strip leading whitespace
    (r'(?u)\s*\Z', ''), # strip trailing whitespace
    (r'[-\s]+', '-'), # reduce multiple whitespace or '-' to single '-'
]
