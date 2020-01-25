Instantbird 1.0 release, 3 days later
#####################################
:date: 2011-07-02 03:15
:author: flo
:category: Community
:tags: 1.0, downloads
:slug: instantbird-1-0-release-3-days-later
:status: published

Servers load
------------

Instantbird 1.0 has been very quickly downloaded over ten thousand of
times. In fact, it happened so fast (especially immediately after we
have been `featured on
lifehacker <http://lifehacker.com/5816618/instantbird-is-a-lightweight-cross+platform-instant-messaging-app-with-sharp-looks>`__)
that our server couldn't handle the load.

We have very quickly been able to mirror our `main
website <http://www.instantbird.com/>`__ on another server, which
allowed people to keep discovering and downloading Instantbird 1.0, but
we had to close the add-ons website for a while as the load it couldn't
handle was also putting down other services that we really needed to
keep online, especially our `bug
database <https://bugzilla.instantbird.org/>`__.

We have tried to re-open the add-ons website at a quieter time, but the
server was unresponsive again within half an hour. This morning we tried
to improve the website's performance by adding some caching mechanism
and reopened again (at a time when most Americans are asleep) for a try.
Again it fall down.

Some people very kindly offered help and proposed to host the website on
their server, but it's difficult to trust someone we barely know to host
a website that requires our SSL certificate.

As the add-ons website had been closed for almost 2 days already (sorry
for the inconvenience!) and extensibility is a key differentiator of
Instantbird compared to other similar IM clients, we decided that this
situation couldn't last any longer and we solved the problem by throwing
money at it: we ordered a beefier server (Quad Core CPU, 16GB of RAM)
and migrated the add-ons website to it as quickly as we could. The
website reopened this afternoon, and our testing confirmed that the new
server can easily handle the load, even with more visitors than we had
when the previous server stopped responding. It's ready for a lot more
people coming! Don't hesitate to tell your friends to try Instantbird
|:)|.

Feedback
--------

We have received a massive amount of feedback since the release. Most
was positive or extremely positive. We received lots of encouragements.
We even received some love letters!

Some of the feedback showed there was some confusion, for example about
how we are different from Pidgin (which we will be the subject of
another post to clarify things). We also received constructive
criticism, good bug reports. The most common request is an easy way to
retweet or to reply to a tweet. We will work on that soon |:)|. Tab
completion of nick names is also commonly requested, but even though
it's clear we need to have this by default in the future, we can usually
satisfy the reporter by pointing to the great (restartless!) `Tab
Complete <https://addons.instantbird.org/en-US/instantbird/addon/276>`__
add-on.

Updates
-------

As no alarming issue has been reported in Instantbird 1.0 which is
already widely used, we have decided to turn on major updates from
Instantbird 0.2 to Instantbird 1.0.

Users of Instantbird 0.2 will be offered an update shortly with an
update prompt looking like this:

|Dialog offering a major update to Instantbird 1.0|

Users of our 0.3pre nightly builds will be offered an update to a
nightly build numbered 1.1a1pre in the next few days.

Conclusion
----------

All in all, it's been a great release and the last few days have been
exciting (even though they were also exhausting). We look forward to
continue hearing your feedback (and to actually act upon it!). Don't
hesitate to share Instantbird with your friends. Our servers are ready!

.. |:)| image:: {static}/smileys/sourire.png
.. |Dialog offering a major update to Instantbird 1.0| image:: {static}/images/major-update-1.0.png

