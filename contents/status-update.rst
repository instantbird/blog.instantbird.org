Status update
#############
:date: 2010-08-11 00:05
:author: flo
:category: Development
:tags: status update
:slug: status-update
:status: published

We've been a bit quiet since the `0.2
release <http://blog.instantbird.org/a25-instantbird-0-2-released.html>`__,
but we haven't slept all of this time, so let's do another status
update!

After some time spent polishing the `new
website <http://www.instantbird.com/>`__ and dealing with post-release
work (like testing and enabling `major
updates <http://blog.instantbird.org/a27-major-update-to-instantbird-0-2.html>`__),
we have started working toward Instantbird 0.3:

-  Some major refactoring work to allow protocol plugins to be written
   fully in JavaScript had started a long time before the final 0.2
   release. This work was being done in the ``js-proto`` branch. The
   branch has been merged so that our nightly testers can help spot new
   issues in 0.3a1pre nightly builds. They have been super helpful, and
   have found 2 regressions, which are now fixed.
-  Instantbird 0.2 is based on the mozilla-1.9.2 platform. Instantbird
   0.3 will be based on Mozilla 2.0. The work to switch to using code
   from mozilla-central is almost completed. This involved updating our
   build system (which is a copy of the comm-central one), changing the
   way our XPCOM components are registered, and other adjustments to
   make Instantbird's code work with a newer Mozilla. This work has
   happened in a ``mozilla2`` branch in our repository. The branch isn't
   merged yet because there remains a serious regression that we need to
   fix (JavaScript code included in message styles isn't executed).
-  We have welcomed new translators, who have enthusiastically started
   translations of Instantbird into 7 new locales (Czech, Dutch,
   Estonian, Italian, Slovak, Spanish and Ukrainian)!

Development is slower than usual this month, because some members of the
team, including myself, are taking some time away from the Internet.

In the relatively near future, we will finish the work to switch to
Mozilla 2.0, and upgrade libpurple to the latest released version
(2.7.\*).
