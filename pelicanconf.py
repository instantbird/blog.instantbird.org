#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'The Instantbird Team'
SITENAME = "The blog of Instantbird's development"
SITEURL = 'http://localhost'

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
# TODO redirect /feed/rss2/ to /feed/
FEED_ALL_RSS_URL = 'feed/'
FEED_ALL_RSS = FEED_ALL_RSS_URL + 'rss.xml'

TAG_FEED_RSS_URL = TAG_URL + 'feed/'
TAG_FEED_RSS = TAG_FEED_RSS_URL + 'rss.xml'
CATEGORY_FEED_RSS_URL = CATEGORY_URL + 'feed/'
CATEGORY_FEED_RSS = CATEGORY_FEED_RSS_URL + 'rss.xml'

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

PLUGINS = [
    'plugins.archives'
]
