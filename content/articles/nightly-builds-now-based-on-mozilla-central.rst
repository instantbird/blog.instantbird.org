Nightly builds now based on mozilla-central
###########################################
:date: 2010-09-13 16:24
:author: flo
:category: Development
:tags: mozilla, nightly
:slug: nightly-builds-now-based-on-mozilla-central
:status: published

In late July, I started working on making Instantbird use the Mozilla
2.0 platform (which the recently released Firefox 4 betas are based on).
This work, which started in a branch, has recently reached a point where
we believe it could benefit from wider testing. The ``mozilla2`` branch
was merged Friday, September 10th, 2010.

This didn't happen as smoothly as I would have hoped, but after 10 (!)
bustage fixes, yesterday we were able to provide the first set of
Instantbird nightly builds based on Mozilla 2.0. Our slowly growing
community on `#instantbird <irc://irc.mozilla.org/#instantbird>`__ has
jumped on them, and quickly reported a few significant issues. Thanks to
their awesome help, those are fixed, and today we have a new set of
nightly builds.

Additional help to test these new builds (`Windows and
Linux <http://ftp.instantbird.com/instantbird/nightly/2010/09/2010-09-13-04-instantbird/>`__,
`Mac <http://ftp.instantbird.com/instantbird/nightly/2010/09/2010-09-13-09-instantbird/>`__),
will be greatly appreciated.

Known issues of this set of builds:

-  The 'Show Logs' menuitems don't work (already fixed and will work
   tomorrow).
-  The Add-ons manager is broken. This is `bug
   591801 <https://bugzilla.mozilla.org/show_bug.cgi?id=591801>`__.
-  The 'Instantbird' checkbox in the 'Update' pane of the 'Advanced'
   panel of the preference Window is disabled (already fixed and will
   work tomorrow).
