Version number change
#####################
:date: 2011-06-27 19:35
:author: flo
:category: Development
:slug: version-number-change
:status: published

The current system
------------------

Since the beginning of the Instantbird project, we have released
versions numbered ``0.x.y.z``:

-  ``0.`` indicates that the initial goals of the project haven't been
   reached yet.
-  ``x`` is the major version number. For example, Instantbird 0.2 was a
   major version for which we made very significant changes.
-  ``y`` is the minor version number, incremented when a release is very
   similar to the previous one, but with some new features. We released
   Instantbird 0.1.1, 0.1.2 and 0.1.3 which were minor new versions.
-  ``z`` was used only for emergency bugfix releases. For example we
   released 0.1.2.1 a day after 0.1.2 because of a very common crash on
   Windows with some MSN accounts (not those we used during our testing
   of course). We also released Instantbird 0.1.3.1 when Instantbird
   0.1.3 was no longer able to connect to the ICQ network.

This version numbering scheme made a lot of sense when the project was
initially a "XUL UI for Pidgin" and the goal was to reach "feature
parity" with Pidgin for Instantbird 1.0. We have, however, supported
features that Pidgin doesn't have for a long time, thus defining the
completion of Instantbird 1.0 as a comparison with Pidgin doesn't make
sense any more. Actually, our roadmap has stated for a long time already
that the 1.0 goal is a "Simple, usable and extensible user interface."

In addition to the 0.x.y.z version number, we are using "aN" and "bN"
suffixes for alpha and beta releases (0.3b1 for example), so the version
number in itself has nothing to do with stability (actually, our testers
report that even our nightly builds are stable!). 0.<something> only
means that we haven't reached our initial goals, not that the version
isn't stable.

Received feedback
-----------------

While linux enthusiasts are used to have great software with a
not-yet-1.0 version number, on Windows a 0.\* version number was a bit
misleading and we received mostly 2 kinds of feedback about the version
number:

-  "Wow, I can't believe it's so stable and featureful with such a low
   version number!" (user who has downloaded and tested it)
-  "Oh, it looks cool, but with such a low version number, it's a
   pre-alpha, it can't be stable, I'll give it a try when it reaches
   1.0."

Disappointing, isn't it? |;-)|

Next
----

We are about to release Instantbird 0.3. This is a major version of
Instantbird, with more changes than any previous release. With the
current changes in the Mozilla release cycle, we are very unlikely to
ever release again a version containing so many changes at once (more
details on how we will adapt to release much more frequently in the
future in another post soon after the release). When releasing
Instantbird 0.2, we hesitated between incrementing the major version
number by only one (which is what we did), or skipping a few version
numbers to go straight to 0.5, because we felt we were half way through
on our goals of delivering a simple, easy to use, cross-platform,
multi-protocol, extensible instant messaging application. After the
fact, given the feedback related to the low version number that we
received, we regretted that we didn't go ahead and release it as
Instantbird 0.5.

What we called Instantbird 0.3 up to now is most likely the last major
release in which we change important things in every parts of the code
base at once. We don't feel that we're only "half way through", so this
time we won't have regrets: It's going to be released as **Instantbird
1.0**. Tomorrow!

.. |;-)| image:: {static}/smileys/clin_d'oeil.png

