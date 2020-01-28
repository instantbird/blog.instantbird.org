Status Update: February 2011 - March 2011
#########################################
:date: 2011-04-06 23:39:37
:author: clokep
:category: Development
:tags: status update
:slug: status-update-february-2011-march-2011
:status: published

Done:
-----

-  Contact merging (`bug
   698 <https://bugzilla.instantbird.org/show_bug.cgi?id=698>`__).  If
   you talk to the same person on multiple IM networks you can now
   combine the buddies from each network into a single contact.  When
   opening a new chat the buddy that is online will be chosen
   automatically and the conversation window will automatically change
   to another buddy if they switch to a different IM network.
-  `Tags have begun to be
   implemented <http://hg.instantbird.org/instantbird/rev/75644053615a>`__
   (to replace the groups concept in the current buddy list).  Tags can
   be hidden by clicking the "x" on the right side of the buddy list,
   all buddies from this tag will go into an "Other Contacts" tag
   automatically, which is shown at the bottom of the buddy list.
-  The buddy list can now be closed on Mac without Instantbird quitting
   (`bug 24 <https://bugzilla.instantbird.org/show_bug.cgi?id=24>`__). 
   It can be reopened from the Dock.
-  Offline contacts vs. unknown contacts are now `differentiated with
   icons <http://hg.instantbird.org/instantbird/rev/7019846a7be3>`__.
-  Instantbird has been upgraded from libpurple 2.7.9 to
   `2.7.11 <http://hg.instantbird.org/instantbird/rev/4af8bacbd226>`__.
   Changes of note include a fix for adding buddies in MSN (see all
   changes at `their change
   log <http://developer.pidgin.im/wiki/ChangeLog>`__).
-  Dark variant of the "Simple" skin (`bug
   710 <https://bugzilla.instantbird.org/show_bug.cgi?id=710>`__).
-  **For Developers:**

   -  Extensions are now able to register commands (`bug
      118 <https://bugzilla.instantbird.org/show_bug.cgi?id=118>`__).
   -  A general JavaScript socket object has been included (`bug
      673 <https://bugzilla.instantbird.org/show_bug.cgi?id=673>`__).
   -  Instantbird 0.3a2pre nightlies are now based on the
      ``mozilla-2.0`` branch instead of the ``mozilla-central`` trunk
      (`commit <http://hg.instantbird.org/instantbird/rev/31b8187656ec>`__). 
      This is the version of the Mozilla source that is used in Firefox
      4.x.

Known Issues with Nightly Builds (0.3a2pre):
--------------------------------------------

-  No feedback when an extension fails to install (`bug
   712 <https://bugzilla.instantbird.org/show_bug.cgi?id=712>`__).
-  Sounds do not work when the buddy list is closed on Mac (`bug
   731 <https://bugzilla.instantbird.org/show_bug.cgi?id=731>`__).
-  Commands do not work in protocol overrides (i.e. GTalk, Facebook)
   (`bug 697 <https://bugzilla.instantbird.org/show_bug.cgi?id=697>`__).
-  Twitter dumps too much information to the error console (`bug
   681 <https://bugzilla.instantbird.org/show_bug.cgi?id=681>`__).

Next:
-----

-  Release 0.3 alpha 2.
-  A `detailed
   roadmap <https://wiki.instantbird.org/Instantbird:Roadmap:0.3>`__ for
   the continued work on 0.3 has been released.  Please take a look and
   help out!
-  Instantbird is participating in `Google Summer of Code
   2011 <http://www.google-melange.com/gsoc/homepage/google/gsoc2011>`__. 
   Mozilla has been gracious enough to allow us to participate this year
   as part of their organization; you can see ideas and information on
   the `Mozilla
   Wiki <https://wiki.mozilla.org/Community:SummerOfCode11#Instantbird>`__.

   -  Contact us via `email <mailto:contact@instantbird.org>`__ (any
      email to this address can be found in our public `Google
      Group <http://groups.google.com/group/instantbird-contact>`__) or
      `IRC <irc://irc.mozilla.org/#instantbird>`__ if you have any
      question.
   -  Applications are due Friday, April 6th, 2011 at 12:00 PM PDT!
