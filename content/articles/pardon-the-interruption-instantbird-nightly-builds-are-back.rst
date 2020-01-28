Pardon the Interruption! Instantbird nightly builds are back!
#############################################################
:date: 2014-03-03 12:21:35
:author: clokep
:category: Development, Mozilla
:tags: mozilla, nightly, status update
:slug: pardon-the-interruption-instantbird-nightly-builds-are-back
:status: published

As of today, March 3rd, 2014, Instantbird nightly builds (1.6a1pre) are being
built again. We last had nightly builds on January 9th, 2014 and they have been
broken since due to a series of a large infrastructure change we’ve been going
through to merge the Instantbird Bugzilla and code repository with Mozilla’s.
Unfortunately, getting nightly builds working again took us longer than expected
as it involved many related issues: updating Instantbird to work with newer
versions of Mozilla, reconfiguring our buildbot and working on getting libpurple
to build as an extension.

The results of this is that Instantbird is now building out of the
“comm-central” code repository (the same place the code for Thunderbird is
stored). What does this mean for you?

*   Instantbird nightlies are now built using comm-central/mozilla-central: bugs
    fixed in Mozilla will be reflected in the next Instantbird nightly.
*   Instantbird 1.6a1pre is currently based on Mozilla 30, this is a bit of a
    jump from Instantbird 1.5 (Mozilla 25). There might be an influx of bugs as
    any issues caused by this jump are worked out. Please report any issues you
    see!
*   (Not entirely related) Bugs for Instantbird can now be reported on
    `bugzilla.mozilla.org`_ under the “Instantbird” and “Chat Core” (for bugs
    shared with Thunderbird Chat) products.
*   Current nightly builds are located at on `our ftp site`_, but automatic
    updating from older nightlies should still work.

Again, sorry for any interruption. Regular development should be continuing now. Thanks for all the concerned emails telling us our builds had stopped!

.. _bugzilla.mozilla.org: https://bugzilla.mozilla.org/
.. _our ftp site: http://ftp.instantbird.com/instantbird/nightly/latest-1.6a1pre/
