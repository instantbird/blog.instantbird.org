"""
Generates and adds archive objects to the context for iterating through the yearly, monthly, or daily archives on any page.
"""

from itertools import groupby
from operator import attrgetter

from pelican import signals
from pelican.urlwrappers import URLWrapper

class Archive(URLWrapper):
    def __init__(self, name, date, *args, **kwargs):
        super().__init__(name, *args, **kwargs)
        self.date = date


class Year_Archive(Archive):
    pass


class Month_Archive(Archive):
    pass


class Day_Archive(Archive):
    pass


# This is heavily based on pelican.generators.ArticlesGenerator.generate_period_archives.
def generate_period_archives(article_generator):
    """Generate per-year, per-month, and per-day archives."""
    period_save_as = {
        'year': article_generator.settings['YEAR_ARCHIVE_SAVE_AS'],
        'month': article_generator.settings['MONTH_ARCHIVE_SAVE_AS'],
        'day': article_generator.settings['DAY_ARCHIVE_SAVE_AS'],
    }

    period_url = {
        'year': article_generator.settings['YEAR_ARCHIVE_URL'],
        'month': article_generator.settings['MONTH_ARCHIVE_URL'],
        'day': article_generator.settings['DAY_ARCHIVE_URL'],
    }

    period_date_key = {
        'year': attrgetter('date.year'),
        'month': attrgetter('date.year', 'date.month'),
        'day': attrgetter('date.year', 'date.month', 'date.day')
    }

    period_date_class = {
        'year': Year_Archive,
        'month': Month_Archive,
        'day': Day_Archive
    }

    def _generate_period_archives(dates, key, ArchiveClass, settings):
        """Generate period archives from `dates`, grouped by
        `key` and written to `save_as`.
        """
        # `dates` is already sorted by date
        for _period, group in groupby(dates, key=key):
            archive = list(group)
            # arbitrarily grab the first date so that the usual
            # format string syntax can be used for specifying the
            # period archive dates
            date = archive[0].date

            if key == period_date_key['year']:
                name = date.strftime("%Y")
            else:
                if key == period_date_key['month']:
                    name = date.strftime("%B %Y")
                else:
                    name = date.strftime("%B %d, %Y")

            yield ArchiveClass(name, date, settings)

    for period in 'year', 'month', 'day':
        save_as = period_save_as[period]
        url = period_url[period]
        if save_as:
            key = period_date_key[period]
            ArchiveClass = period_date_class[period]
            archives = list(_generate_period_archives(article_generator.dates, key, ArchiveClass, article_generator.settings))
            article_generator.context[period + '_archives'] = archives


def register():
    signals.article_generator_finalized.connect(generate_period_archives)
