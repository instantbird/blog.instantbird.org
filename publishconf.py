#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# This file is only used during publishing.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# Use the full site URL for feeds.
SITEURL = 'http://blog.instantbird.org'
FEED_DOMAIN = SITEURL

# Ensure the output is clean.
DELETE_OUTPUT_DIRECTORY = True
