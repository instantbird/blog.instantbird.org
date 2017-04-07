Instantbird 0.2 Feature Preview: Localizability
###############################################
:date: 2009-07-16 18:04
:author: flo
:category: Development
:tags: 0.2, preview, translations
:slug: instantbird-0-2-feature-preview-localizability
:status: published

As you may (or may not) know, we previously wrote that `Instantbird
0.1.\* was not
localizable <http://www.instantbird.org/about_translations.html>`__. The
reason evoked for this was the use of gettext by libpurple, which is not
compatible with the way XUL applications are localized. I'm going to
give more details about the issue, and explain how we solved it for
Instantbird 0.2.

Comparison of translation systems used by Mozilla and libpurple:
----------------------------------------------------------------

| Inside libpurple, localizable strings are just marked by
  ``_("string")``.
| For example, you can find
  `this <http://lxr.instantbird.org/instantbird/source/purple/libpurple/connection.c#549>`__
  in the code:

::

       description = _("Unknown error");

During the compilation, \_() is expanded by the C preprocessor to a call
to a gettext function. Gettext tools can analyze the source code, find
all strings enclosed in \_() markers, and produce a translation
template. `This template <http://developer.pidgin.im/l10n/pidgin.pot>`__
(a .pot file) is then handed to translators, who translate the strings
and then provide a .po file for their language.

The translation system for XUL applications is quite different, here are
2 significant differences:

-  localizable strings are not directly in the source code. The source
   code uses unique identifiers, and these identifiers are used to find
   the actual string in the locale files.
-  the strings are spread across several localized files. Usually each
   window has its separate files, which makes it easy to decide at a
   later point that something will become an extension, and makes it
   easy to localize an extension like any other part of the application.

How do we deal with this in Instantbird?
----------------------------------------

Obviously, we don't want Instantbird to use both of these localization
systems, so one had to be removed. In Instantbird 0.1.\*, we just
removed gettext without replacing it. This means that the gettext \_()
macro was defined to something doing nothing, and the string used was
just the one specified directly inside the source code.

For Instantbird 0.2, this is no longer acceptable, and we worked on a
way to simulate the action of gettext, that is, hiding the 2 differences
I've just explained.

Splitting the translation in different files wasn't very difficult.
Actually, gettext has a concept of packages that makes it possible to
split the translation of an application into several packages, the
feature is just unused by libpurple. With a little bit of build system
tweaking, I finally got a translation file for the core of libpurple,
and a separate translation file for each protocol plugin. This was
needed so that `libpurple protocol plugins packaged as
extensions <http://blog.instantbird.org/a9-instantbird-0-2-feature-preview-protocols-as-extensions.html>`__
can be localized.

Creating a unique identifier for each localizable string was a bit more
work. The solution we have settled on is:

-  Take the original string and remove all string formatters (words
   starting with %), hexadecimal numbers (words starting with 0x) and
   more generally, all non alphanumeric characters.
-  Remove all the whitespace in the remaining string, keep only the 7
   first words, and convert to camel case.

At this point, we have an identifier for the original string, but it is
not unique. Long strings that differ only at the end result in the same
identifier, and strings that don't contain any real word ('%s:%s' for
instance) all result in an empty string. To disambiguate in these cases,
and only in these cases, we append the 8 first characters of the
hexadecimal MD5 hash of the original string to the identifier.

Now, how do we use this?
~~~~~~~~~~~~~~~~~~~~~~~~

We have a .properties file for libpurple and one for each protocol
plugin. When libpurple is compiled for Instantbird, the gettext macros
are modified to point to some of our code instead of the gettext
library. Our code uses the en-US string to build the identifier, and
attempts to find it in the .properties file. If it isn't found, it tries
again with the identifier plus the 8 first characters of the MD5 hash of
the string. If it still isn't found, then it returns the en-US string as
a fallback (and emits a warning in debug builds).

How do we make the .properties files for libpurple?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

I wrote `a python
script <https://hg.instantbird.org/instantbird/file/b288fc7228e7/tools/l10n/convert-purple-po-files-to-properties-files.py>`__
that generates automatically the appropriate .properties files for the
en-US language from the source code of libpurple. Additionnaly, it uses
the various .po files of Pidgin to produce files that can be used as a
base for localizing this part of Instantbird.

Does this mean I can start translating Instantbird into my own language?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No, not yet, but very soon! Once we are ready to accept contributions
from translators, we will ask translators who volunteer to localize
Instantbird to contact us so that we can provide them with these
generated files.

An alpha build of Instantbird 0.2 will be available soon. We will
provide an experimental French translation of this build (most people in
our team are French, so French was the logical choice for testing all of
this ourselves).
