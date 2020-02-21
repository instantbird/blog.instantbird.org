Status Update: April 2011 - May 2011
####################################
:date: 2011-05-27 19:03:22
:author: clokep
:category: Development
:tags: status update
:slug: status-update-april-2011-may-2011
:status: published

A lot has been going on for Instantbird as the pace has been picking up
as we approach the release of 0.3. Below we've highlighted some of the
exciting new features that have become available since our last update.
Some of these are currently available in 0.3 alpha 2, and the rest are
available in the `nightly <http://nightly.instantbird.im/>`__ builds!
They'll of course be included in 0.3 beta 1 (and the final release of
0.3).

Instantbird is participating in `Google Summer of Code
2011 <http://www.google-melange.com/gsoc/org/google/gsoc2011/mozilla>`__
with `one student
project <http://www.google-melange.com/gsoc/project/google/gsoc2011/vpj/6001>`__.
`Mozilla <http://www.mozilla.org/>`__ has been gracious enough to allow
us to participate this year as part of their mentoring organization. The
project includes an implementation of the XMPP protocol in JavaScript as
an Instantbird extension. The XMPP implementation will be extensible to
allow Instantbird extension developers to easily implement extra parts
of the XMPP protocol beyond what will be included by default, some
examples of this include collaborative editors and drawing boards.
Details of the `project
proposal <http://www.google-melange.com/gsoc/project/google/gsoc2011/vpj/6001>`__,
as well as `code <https://github.com/vpj/xmpp-js>`__ and a
`blog <https://xmpp-js.posterous.com/>`__ are available to track this
project.

Done:
-----

-   0.3 alpha 2 released! `Give it a
    try <http://www.instantbird.com/download-0.3a2.html>`__ and let us
    know what you think!
-   Contacts now show the list of the buddies they contain (as well as
    their online status) in the tooltip.
-   Windows (and Linux) users can now minimize to the system tray (we've
    integrated the popular MinTrayR add-on). Note that by default
    Instantbird will minimize to tray when the "x" is clicked, to quit
    the application choose "Quit" from the File menu or right click on
    the system tray icon and choose "Quit". This behavior can be changed
    from the preferences window.
-   Alphabetical sorting of group names (bug 366) and contacts (bug 343).
-   You can now quickly jump to the n-th tab using <modifier>+<n> in the
    conversation window (bug 496), where <modifier> is ctrl on
    Windows/Linux and Command on Mac.
-   The conversation tabs styling has been updating to match Firefox 4
    (bug 768), although we're still working on getting some of the Aero
    glass effects in.
    |Screenshot of a work in progress|
    Screenshot of the ongoing work on the Windows Aero theme, but also
    showing the already finished new conversation and contacts list UI.
-   Users can now set their buddy icon and the display name of their
    accounts right on the contacts list (bug 334).
-   The Conversation UI has received a major overhaul to show the buddy
    icon, display name and current status of your contact. In addition,
    you can switch the buddy you're talking to by clicking on the
    protocol icon (bug 744).
-   Message themes can also properly show the user's own icon, go `check
    one
    out <https://addons.instantbird.org/en-US/instantbird/browse/type:1/cat:6>`__!
-   A help command ('/help') was added to quickly and easily see which
    commands are available for the current conversation (bug 691).

For Developers:
---------------

-  An 'icon-changed' notification was added for when the user updates
   their buddy icon.
-  The UI code has been moved into the 'content' directory inside of
   omnijar (this will affect developers who have been unzipping omnijar
   to edit code).

Known Issues with Nightly Builds (0.3a3pre)
-------------------------------------------

-  Commands do not work in protocol overrides (i.e. GTalk, Facebook)
   (bug 697).
-  Twitter dumps too much information to the error console (bug 681).
-  The user icon may not appear anymore on some protocols (ICQ/AIM/?)
   after restarting the application (bug 783).

.. |Screenshot of a work in progress| image:: {static}/images/IbGlassBorders.png
   :target: {static}/images/IbGlassBorders.png
   :width: 100%
