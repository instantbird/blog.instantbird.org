"""
Generates a tag cloud similar to `wp_generate_tag_cloud` from WordPress.

Based on https://github.com/getpelican/pelican-plugins/tree/master/tag_cloud
Algorithm based on https://github.com/WordPress/WordPress/blob/3.2-branch/wp-includes/category-template.php#L582-L704

"""
from collections import defaultdict
import logging
from operator import itemgetter
import random

import math
import random

from pelican import signals

logger = logging.getLogger(__name__)

def generate_tag_cloud(generator):
    tag_cloud = defaultdict(int)
    for article in generator.articles:
        for tag in getattr(article, 'tags', []):
            tag_cloud[tag] += 1

    tag_cloud = sorted(tag_cloud.items(), key=itemgetter(1), reverse=True)
    tag_cloud = tag_cloud[:generator.settings.get('TAG_CLOUD_MAX_ITEMS', 100)]

    # Add scaled counts to the tag cloud.
    tag_cloud = [(tag, count, round(math.log10(count + 1) * 100)) for tag, count in tag_cloud]

    min_count = min(map(itemgetter(2), tag_cloud))
    spread = max(map(itemgetter(2), tag_cloud)) - min_count
    if spread <= 0:
        spread = 1

    min_font = generator.settings.get('TAG_CLOUD_MIN_FONT', 8)
    max_font = generator.settings.get('TAG_CLOUD_MAX_FONT', 22)
    font_spread = max_font - min_font
    if font_spread < 0:
        font_spread = 1
    font_step = font_spread / spread

    def generate_tag(tag, count, scaled_count):
        """Return a tuple of tag, font size, count."""
        font_size = min_font + (scaled_count - min_count) * font_step

        return (tag, font_size, count)

    tag_cloud = [generate_tag(*tag) for tag in tag_cloud]

    # Handle sorting.
    order_by = generator.settings.get('TAG_CLOUD_ORDER_BY', 'name')
    order = generator.settings.get('TAG_CLOUD_ORDER', 'ASC')

    if order == 'RAND':
        random.shuffle(tag_cloud)
    else:
        # Sort by name or count.
        if order_by == 'name':
            tag_cloud = sorted(tag_cloud, key=lambda elem: elem[0].name.lower())
        elif order_by == 'count':
            tag_cloud = sorted(tag_cloud, key=lambda elem: elem[1])

        # Sort ascending, descending, or random.
        if order == 'DESC':
            tag_cloud = reverse(tag_cloud)

    # Add to the context.
    generator.tag_cloud = tag_cloud
    generator._update_context(['tag_cloud'])


def register():
    signals.article_generator_finalized.connect(generate_tag_cloud)
