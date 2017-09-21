Instantbird 0.2 feature preview: protocols as extensions
########################################################
:date: 2009-04-19 19:45
:author: flo
:category: Development
:tags: 0.2, addons, preview
:slug: instantbird-0-2-feature-preview-protocols-as-extensions-2
:status: published

One of the features we wanted in Instantbird 0.2 was the ability to
install libpurple protocol plugins like any other addon. I'm happy to
report that this is now possible with current `nightly
builds <http://ftp.instantbird.com/instantbird/nightly/latest-trunk/>`__.

To demonstrate this feature, I compiled the `Facebook Chat libpurple
protocol plugin <http://code.google.com/p/pidgin-facebookchat/>`__. The
result is an `installable xpi file`_ of about 200kB,
that people can try with nightly builds of Instantbird.

This file contains a binary module compiled for Windows, Linux and Mac
OS X (universal), produced by copying the code from
`here <http://pidgin-facebookchat.googlecode.com/files/pidgin-facebookchat-source-1.47.tar.bz2>`__
into the Instantbird source tree. This is the quickest way I found to
build it, we will need to figure out a better (without having to
download and build the whole Instantbird source code) way later. This is
`the exact patch I used`_ to build it.

The xpi file also contains a set of icons and a locale file. I will
explain in another post how we replaced the usage of ``gettext`` in
libpurple by a way to get localized strings from regular .properties
files.

Feel free to try this facebook chat addons. I don't know how stable it
is, but I've used it for a few days already and haven't encountered any
serious issue. If this turns out to be crashy for you, don't hesitate to
send us crash reports, I uploaded the symbols to our symbol servers, so
the reports should provide useful information.

I have other nearly-ready Instantbird 0.2 features to introduce in more
details later, including: localization, emoticon themes, message styles
(like Adium), ...

Next time: how localization works with Instantbird and how we replaced
``gettext``.

.. _installable xpi file: {filename}/files/facebook.xpi
.. _the exact patch I used: {filename}/files/add-facebook-chat-prpl.patch
