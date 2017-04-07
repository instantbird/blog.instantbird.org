Nightly builds available
########################
:date: 2008-10-18 16:23
:author: flo
:category: Downloads
:tags: nightly
:slug: nightly-builds-available
:status: published

Nightly builds
--------------

We produce nightly builds of Instantbird every day with buildbot. These
builds can be downloaded from our server at
http://ftp.instantbird.com/instantbird/nightly/latest-trunk/. Please
note that these builds are available for testing purpose only, and are
totally untested before we put them online. Use them at your own risks.
If you want to help us with testing, there is no need to download and
install a new build from the server everyday, the application will
automatically propose updates.

To ensure that users won't confuse nightly unstable builds with
releases, we use a different set of icons for the nightlies. The nightly
icon is:

|Nightly logo|

What's new?
-----------

It has already been a few months since the last release, so I guess it's
a good time for a quick status update.

Just after the 0.1.2 release, we switched from subversion to mercurial
for the versioning of our source code. Our mercurial repository is
publicly available at http://hg.instantbird.org/. At the same time, for
the Mozilla code we use, we switched from the CVS trunk (1.9.0.x) to
mozilla-central and we are now using a build system which is very
similar to the comm-central one. In fact, it's a copy of it with very
small modifications. Thanks to the people who helped us for the
transition and to the people who worked on the comm-central build
system.

There are also some new features: There's a findbar in the conversation
window (Ctrl/Cmd + F to open it), commands (/me, /topic, etc...) work in
conversations, the list of chat room participants is displayed (for
example, in IRC channels), typing notifications work, idleness (becoming
idle based on the inactivity time) works, status changes are displayed
in conversations, it's possible to force a check for update, ...

We also spent time on code cleanup (debug logging for example) and
stability improvements (taking into account the data from the crash
reporting system).

What's next?
------------

We plan to do another minor release soon, and after that, for the 0.2
release, the focus will be on extensibility.

On a side note, this project has been public for one year, Instantbird
0.1 was released on October 18th, 2007. Even if we hoped to do more,
it's been a great year for the project!

.. |Nightly logo| image:: http://www.instantbird.com/images/nightly.png

