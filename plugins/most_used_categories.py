from pelican import signals


def most_used_categories(generator):
    """Add a list of most used categories in descending order of use."""
    most_used_categories = sorted(generator.categories, key=lambda c: len(c[1]), reverse=True)

    # Add to the context.
    generator.most_used_categories = most_used_categories
    generator._update_context(['most_used_categories'])


def register():
    signals.article_generator_finalized.connect(most_used_categories)
