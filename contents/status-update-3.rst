Status update
#############
:date: 2010-11-17 00:01
:author: mic
:category: Development
:tags: status update
:slug: status-update-3
:status: published

It's been three weeks now since the `last status
update <http://blog.instantbird.org/c31-status-update.html>`__ and
here's a short summary of things that have been done in the meantime.

Some contributors are getting more closely involved with the project
lately. Subsequently some tasks, such as posting status updates, will
occasionally be performed by people besides Florian, in fact this entry
was written by Benedikt P.

Done:
-----

-  Making the buddy list ready for the future: the buddy list backend
   mentioned in the last update has been finished, debugged and finally
   `landed <https://hg.instantbird.org/instantbird/rev/bf56c9f22e75>`__
   two weeks ago.
-  The Mozilla framework has supported CSS transitions for a while now
   and we decided to ditch our old animation code in favour of this
   state-of-the-art technology. Changing the display- and
   hide-animations on the buddy list is part of `bug
   504 <https://bugzilla.instantbird.org/show_bug.cgi?id=504>`__. Along
   with the change to the buddy list backend it greatly increased the
   speed when switching on the display of offline buddies. There should
   no longer be any noticeable delay, even when there are many buddies
   on the list.
-  If you ever tried to \*emphasize\* words in a plain text chat, be
   happy: we are displaying plain text formatting now, such as \*bold\*,
   /italics/, underline and ``|code|`` (`bug
   543 <https://bugzilla.instantbird.org/show_bug.cgi?id=543>`__).
-  We made conversation tabs look more native on Mac, taking advantage
   of a `suggestion <http://blog.instantbird.org/a18-tabs.html>`__\ from
   Markus Stange:The old flat look:
   |Cropped screenshot of the old look of the unified toolbar on
   Mac|\ Now with a nice gradient in the title bar:
   |Cropped screenshot of the new look of the unified toolbar on Mac|

   .. raw:: html

      </p>
      <p>

   If you have any other ideas how to make Instantbird more awesome,
   feel free to `contact us <irc://irc.mozilla.org/#instantbird>`__ or
   to file an enhancement request on our
   `bugtracker <https://bugzilla.instantbird.org/>`__.
-  Stuff for devs, stuff that matters: we're `using
   Services.jsm <https://hg.instantbird.org/instantbird/rev/2a42fc158bfd>`__
   now and were able to reduce the number of lines used to get XPCOM
   services by 2/3.
-  Brainstorming: some `brainstorming about
   completion <http://log.bezut.info/instantbird/101110/#m162>`__ of
   nicknames (among other things) happened on our IRC channel,
   summarized results and ideas can be found `in the
   wiki <https://wiki.instantbird.org/Brainstorm:completion>`__.

Next:
-----

-  We're planning to release Instantbird 0.2.0.1, which will include
   security and stability fixes for our current stable release.
   Additionally it will be available in a few additional locales that
   were finished soon after 0.2 was released.
-  We're planning to release a 0.3 alpha 1 version, which will include
   the changes mentioned above and some more visible changes.
-  Carrying on the task of getting a new Mac build machine and switch
   Mac build from PPC/i386 to i386/x64.
-  Setup a nonprofit organization to make money matters related to the
   project transparent and to be able to accept donations.

.. |Cropped screenshot of the old look of the unified toolbar on Mac| image:: http://blog.instantbird.org/images/tabs8-macosxactiveinactive.png
.. |Cropped screenshot of the new look of the unified toolbar on Mac| image:: http://blog.instantbird.org/images/tabs8-macosxactiveinactive-trunk.png

