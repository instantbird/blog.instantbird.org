Status update
#############
:date: 2010-10-19 13:05
:author: flo
:category: Development
:tags: status update
:slug: status-update-2
:status: published

It's time again to give an overview of what we've been doing in the last
few weeks and what we plan to do next.

Done:
-----

-  The rewrite of the buddy list backend is going well. The new
   implementation, is almost usable (as long as you don't need to add,
   remove or rename a contact). I can't wait to land this in our nightly
   builds! (This will occur as soon as everything is re-implemented so
   there is no feature-loss). `Bug
   555 <https://bugzilla.instantbird.org/show_bug.cgi?id=555>`__ tracks
   this work.
-  I've spent some time analyzing the crash reports we have received
   after the libpurple update. I
   `emailed <http://pidgin.im/pipermail/devel/2010-October/009876.html>`__
   the Pidgin developers mailing list to share my findings. The feedback
   received allowed us to fix a whole class of Windows-only crashes by
   applying `a Glib
   fix <https://bugzilla.gnome.org/show_bug.cgi?id=167569>`__.
-  On Mac, the mozilla-central switch from ppc/i386 universal builds to
   i386/x64 universal builds caused some breakage in our nightly builds.

   -  For now, we have reverted to producing ppc/i386 builds, following
      the direction taken on comm-central.
   -  However, we are aware that current nightly builds are pretty
      broken when run on a PPC machine.
   -  We will switch to i386/x64 universal builds as soon as we have a
      new Mac build machine that can run Mac OS X 10.6 (the current
      nightly builds are compiled on a `PowerMac
      G5 <http://en.wikipedia.org/wiki/Power_Mac_G5>`__).

-  I wasted a disappointingly large amount of time trying to buy a
   recent used Mac Mini on ebay, dealing with the confusing messages of
   an inexperienced seller. Transaction finally canceled today, back to
   square one |:(|.
-  Some time spent trying to understand issues with the update system,
   with our servers, and our buildbot slaves. No exciting details to
   report about this.
-  Various fixes:

   -  Emoticons will no longer annoyingly appear in URLs. This was
      `fixed <https://hg.instantbird.org/instantbird/rev/a078133a0492>`__
      in `bug
      207 <https://bugzilla.instantbird.org/show_bug.cgi?id=207>`__.
   -  The issue mentioned previously about message themes installed with
      the new add-on manager is
      `fixed <https://hg.instantbird.org/instantbird/rev/ad88e44b2d14>`__.
   -  The 'themes' icon in the preferences dialog has changed (`bug
      484 <https://bugzilla.instantbird.org/show_bug.cgi?id=484>`__).

Next:
-----

-  Land the new buddy list backend, and start implementing new features
   above it.
-  Have an interesting example of a protocol plugin implemented in JS.
-  Setup a nonprofit to make money matters related to the project
   transparent, and to be able to accept donations.

.. |:(| image:: {filename}/smileys/triste.png

