blog.instantbird.org
####################

This is the source for https://blog.instantbird.org. It is a static site generated using
`Pelican <https://blog.getpelican.com/>`_ with separate articles stored under the
``content/articles`` directory. Each article is stored as a separate
`reStructuredText <https://docutils.sourceforge.io/docs/user/rst/quickstart.html>`_ file.

Comments are read-only and use the `pelican_comment_system`_ plugin, they are stored
under ``content/comments/<article-slug>/<globally-unique-id>.rst``.

.. _pelican_comment_system: https://github.com/getpelican/pelican-plugins/tree/master/pelican_comment_system

Additional static files are stored under other directories of ``content/``.

The theme is converted from the WordPress PHP theme to Jinja_ files, but is generally
unmodified.

.. Jinja: https://jinja.palletsprojects.com

Development
===========

Note that development happens on the ``source`` branch from the git repository.

You'll first need to install Python 3, then setup a new virtualenv and activate it:

.. code-block:: bash

    python -m venv .venv
    source .venv/bin/activate

Then install the necessary Python packages:

.. code-block:: bash

    pip install -r requirements.txt

You should be all set to re-generate the content now! You can do this using invoke:

.. code-block:: bash

    inv build

The results get stored in a directory called ``output/``, you can easily serve them
on localhost using the built in Python server:

.. code-block:: bash

    inv serve

A general useful way to develop is to use three terminals:

1. The first terminal checks for changes to any of the project files and constantly
   re-runs Pelican to update the output: ``inv regenerate``.
2. The second terminal serves the files: ``inv serve``.
3. The last terminal is free to use ``git`` or other commands.

Publishing
==========

Once changes are complete, they should be committed to git and pushed to the ``source``
branch. The rendered changes can be created and pushed to the server using invoke:

.. code-block:: bash

    inv publish

This first runs Pelican with the publish configuration, then uses
`ghp-import <https://pypi.org/project/ghp-import/>`_ to push the the output to the
``master`` branch on GitHub. It sometimes takes 5 - 10 minutes for the update to
propagate to be viewable.

History
=======

This blog was originally served via a custom blog engine, then converted to WordPress,
now converted to Pelican. There might be some things lost / broken during those
conversions, please let us know if you see any problems.

.. _let us know: https://github.com/instantbird/blog.instantbird.org/issues/new
