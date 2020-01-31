Weekly Meeting: October 31, 2011
################################
:date: 2011-11-04 15:52:14
:author: clokep
:category: Development
:tags: weekly meetings
:slug: weekly-meeting-october-31-2011
:status: published

At the weekly meeting held on October 31, 2011 plans for Instantbird 1.2
were discussed as well as a summary of what's happened since the 1.1
release. (`Full chatlogs <http://log.bezut.info/instantbird/111031/#m220>`__
are also available, as well as the `Etherpad
timelime <https://etherpad.mozilla.org/instantbird-weekly-meeting-20111031>`__.)

    .. compound::

        Weekly meetings are held every Monday at 4pm UTC (that's 6pm for
        people in France, and 9am for people in San Francisco) in
        `#instantbird on irc.mozilla.org <irc://irc.mozilla.org/instantbird>`__.

What's Happened Since the 1.1 Release:
--------------------------------------

*   Lots of patches have been reviewed and some new features are in (or soon
    to be in) the `nightly builds <http://nightly.instantbird.im/>`__.

    *  Tab complete is now smart about case sensitivity.
    *  You can now change your status from the tray icon.
    *  You can now copy the link directly to a tweet.

*   Some major changes have been made to the repository to pave the way for
    large improvements. If you have the code checked out, you should update!

What's Being Worked On:
-----------------------

.. container:: wp-caption alignleft

    .. image:: {static}/images/nickcolor13.png
        :width: 159px
        :height: 387px
        :alt: Active participants are highlighted in color.
        :target: {static}/images/nickcolor13.png

    Active participants are highlighted in color.

-  `Only show colors of participants who have
   participated <https://bugzilla.instantbird.org/show_bug.cgi?id=1112>`__,
   allowing you to quickly see who's active! This first patch will keep
   participants gray until they've talked once, look for it in a nightly
   soon!
-  Cleaning up and renaming of the interfaces to make them easier to
   work with. This is paving stone to making libpurple optional (and
   only loading protocols when they're needed).
-  Integration work of the JavaScript IRC code into the Instantbird
   source has started (instead of using it as an extension).
-  Florian will be attending `MozCamp
   Berlin <https://wiki.mozilla.org/EU_MozCamp_2011>`__, from November
   12th to November 13th, and will be giving a talk on Instantbird, go
   say "Hi!" if you'll be attending!
-  Lots of user interface (in particular, when using Twitter) "paper
   cut" bugs! Those annoying bugs that you can live with, but get in
   your way? Yeah, we don't like those either.

**Ways You Help Out:**
----------------------

There's a few tasks that we could use help with, if you're interested in
any of these, please `contact
us <http://instantbird.com/about.html>`__.  (And if there's something
else you're interested, let us know about that too!)

-  A QA/testing team would help to find regressions and bugs quickly
-  Help is needed in organizing the localization effort and keeping them
   up to date with information.
-  Someone to work on making the add-on experience more enjoyable would
   be appreciated.

Stop by at our next meeting on November 7, 2011 at 6:00 PM France time
in `#instantbird on
irc.mozilla.org <irc://irc.mozilla.org/instantbird>`__!  And as always,
please file any bugs you see in our `bug
tracker <https://bugzilla.instantbird.org>`__.
