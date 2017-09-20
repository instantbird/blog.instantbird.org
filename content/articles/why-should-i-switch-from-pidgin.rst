"Why should I switch from Pidgin?"
##################################
:date: 2011-07-09 00:17
:author: flo
:category: Community
:tags: libpurple, pidgin
:slug: why-should-i-switch-from-pidgin
:status: published

This is a question people keep asking us. With some variations ("Why
should I switch from Adium?"), or sometimes without the question mark
("There's nothing more than Pidgin").

We are not competing...
-----------------------

I think people ask us this question because they perceive us as
competing with Pidgin/Adium/[insert the name of your favorite open
source IM client]. But there's no good answer to that question, because
we are not competing, here is why:

-  we share values. We believe that instant messaging technologies
   should be freely accessible and open: people should not be locked in
   closed systems.
-  we share a technology stand point: we think that to empower people to
   increasingly use the open IM technologies that we like, we need to
   offer people a tool that makes it easy to access both promising open
   technologies and legacy networks.
-  we share code. Instantbird, like Adium, relies on libpurple, which is
   at the heart of Pidgin, to connect to legacy networks. We take this
   code, but we also give back: several changes made to libpurple to
   improve its reliability in Instantbird are now part of Pidgin. We are
   working together, and Instantbird developers are definitely part of
   the Pidgin developer community.

... but we offer an alternative
-------------------------------

I can easily understand why people think we compete though, as we do
provide an alternative. I assume people who ask the previously mentioned
question actually wanted the answer to another question: How is
Instantbird different from Pidgin? Now, this is a question we can
answer!

I will actually provide several different answers: the first will
satisfy technically oriented people, the others should be understandable
by everybody. Most of my points compares Instantbird to Pidgin, but are
still applicable when comparing Instantbird to other IM clients.

Technical differences
---------------------

The biggest technical difference between Pidgin and Instantbird is that
Pidgin uses GTK+ and Instantbird uses the Mozilla XUL platform to
display its user interface.

The Mozilla platform has advantages compared to GTK+:

-  The Mozilla platform is well known for its awesome extensibility.
   Add-ons can modify almost anything that is part of the Instantbird
   user interface, and the skills required to build add-ons are similar
   to the skills required to create a website, as the technologies are
   basically the same: HTML, CSS, JavaScript, XML, ... Instantbird
   add-ons are easy to install, some can even be installed without
   restarting the application! (To be fair, Pidgin also supports
   plugins, but writing them in C requires much more programming
   knowledge and to compile them for each platform. Pidgin also has
   Python (via D-Bus) and Perl scripting APIs, but I'm not sure they are
   actually usable on Windows.)
-  While a GTK+ user interface is native on some Linux desktop operating
   systems (typically those based on Gnome or XFCE), a XUL user
   interface also acts native on Windows (we even included some Aero
   Glass effects for Windows 7) and Mac OS X where GTK may not fit as
   well.
-  Thanks to the Mozilla accessibility effort, the XUL platform is very
   accessible and we have received a lot of enthusiastic feedback from
   users of assistive technologies who love Instantbird.

Developing on top of Mozilla also has some (perceived) downsides:

-  We need to ship the whole Mozilla toolkit, which makes us package
   megabytes of compiled code we didn't write. This means for example
   that the Instantbird installer for Windows weights 9.9MB. Some people
   (especially some Miranda fans) seem to think this is huge, but while
   I like to find ways to reduce the size of the installer we ship, I
   tend to think at this point it is mostly a non-issue. Just for
   comparison, the Pidgin installer weights 9.5MB without GTK, and
   32.4MB with all its dependencies included.
-  The Mozilla platform has the reputation of using more resources than
   other browsers/toolkits. The good news is, some bright people are
   currently making a `huge
   effort <https://wiki.mozilla.org/Performance/MemShrink>`__ to reduce
   the memory usage, so this will be mitigated in future releases. Plus
   the situation is not as bad as some people pretend it to be: the
   memory usage measurements we see in comments about Instantbird aren't
   that scary, some people start to complain when an application uses
   40MB of memory. Hey come on, we are in 2011, new machines have been
   shipping with gigabytes of memory for years already...
-  I heard from some Linux packagers that the Mozilla build system is
   not easy to work with for them. While there may be some pain points
   here, it doesn't really affect the end user.

We make Instantbird for you!
----------------------------

Some developers make their programs the best for themselves and share it
with you, for free. These programs are the result of people's hard work
which they offer you as a gift, and so these people deserve respect for
that! Unfortunately, it is not unusual that if somehow the product
doesn't work out for you, it's your problem, not theirs, and you are
free: to fix it, to report the issue and hope someone will fix it, or to
look for a greener pasture. Your comments are valued if they help
developers make their program better for everybody, for example if it
helps fixing bugs that lots of people suffer from. Your opinions and
wishes may not be taken into account, however, unless you intend to
actually start working on them: patches are welcome, not additional work
(people are busy already).

We work to make Instantbird the best for you. We look forward to
gathering your feedback and acting upon it to make Instantbird even
better, for you. We assume that when someone takes the trouble to come
and talk with us to complain about something, there's a valid concern.
Even when it's well hidden behind factually inexact assertions that we
can't agree with. If people cannot express themselves clearly, there's a
reason why they are confused, and if a confusion is common, we should
find its cause and fix it.

As this difference may be a bit theoretical, I'm going to give a
concrete example in the next point: the way we deal with stability
issues.

Stability
---------

Crash reports
~~~~~~~~~~~~~

Let's see what happens in the unfortunate event of the user being hit by
a bug resulting in a crash of the application:

If you are using Pidgin and want to help get the bug fixed, you need to
`get a backtrace <http://developer.pidgin.im/wiki/GetABacktrace>`__ (on
Unix systems) or to have `installed the debug symbols before the
crash <http://developer.pidgin.im/wiki/TipsForBugReports#WhattodoifPidgincrashes>`__
so that a crash report could be dumped to the disk (on Windows). Then
you need to open a ticket on trac and give all the info you have. As
this process may be a bit scary for most end-users, I'm afraid valuable
feedback could get lost.

| If the same issue happens with Instantbird, first we apologize:
| |Instantbird crash reporter|

Then all you have to do to send us the technical information about the
crash is a single click in this crash reporter dialog. We collect all
these crash reports and analyze them to improve the stability of the
next version of Instantbird.

Nightly testing
~~~~~~~~~~~~~~~

In addition to collecting crash reports, another thing we do to maintain
a high stability level for Instantbird is that we encourage early
adopters to run with nightly builds of Instantbird which are updated
almost daily with the very latest version of our source code. Therefore,
if something we changed degrades the stability, we receive crash reports
way before the defective change ends up in a release you may use.

If some change feels a bit risky to us, we push it to our testers at
least a week before releasing, or we delay it so that it gets
appropriate testing before being included in the next release.

Just as a comparison, Pidgin's currently in development code is tested
only by developers and `others people are discouraged from attempting to
use
it <http://developer.pidgin.im/wiki/Installing%20Pidgin#WhydoyoualwayssaynottouseMTN>`__.

Learn more about our `stability efforts`_.

Changing
--------

We keep seeing comments of people (who have not actually tried
Instantbird) who think we should go improve Pidgin instead of "wasting
time" on Instantbird.

In the page of our website where we explain `why we create
Instantbird <http://www.instantbird.org/>`__, we conclude:

    It's time to bring back innovation!

To do this, we need to be able to change things easily. As Instantbird
is still a young project, we can change fast.

Pidgin on the other hand is already a mature project with policies about
when it's acceptable to change APIs or when they are frozen: it's
basically impossible to change an API in Pidgin until a new major
version is released (so after the Pidgin 2.0.0 release, the API changes
have to wait until Pidgin 3.0.0 comes out to be included: currently
Pidgin 2.0.0 was released over four years ago!). This is a good thing to
ensure the plugins stay compatible, but it slows down the changes to the
application.

Different feature sets
----------------------

This is my last point even though most people would expect to see it
first. Instantbird and Pidgin have different feature sets.

On one hand, Pidgin has some features that Instantbird doesn't have.
Some that we will have in the future. Some that we don't want to have.
I'm not going to give a full list here because I don't actually have a
list of all Pidgin features to compare and check what we have and what
we don't have. We are neither trying to copy Pidgin nor to directly
compete against it, so such a list would be irrelevant anyway.

On the other hand, Instantbird has some features that Pidgin doesn't
have (message themes, automatic updates, inline search, ...) and even
some unique features (for two examples, see my blog posts introducing
`Time Bubbles`_ and `Magic copy`_).

Conclusion
----------

So, should you switch to Instantbird? If I were you, I would. But I'm
not you. Deciding which IM client you use is your choice, based on your
taste, your needs, your feelings. It's your decision, really!

If you like what you currently have and see nothing you like in what
Instantbird offers, just keep using what you like.

If you love Instantbird, then, obviously you should use it.

If you are in the middle and like Instantbird but for some reason can't
use it because something you really need is missing or doesn't work,
please tell us about it, we are eager to receive your feedback! And
maybe there's already an add-on to customize Instantbird to do what you
wanted that we can point you to.

In any case, we are not going to try to force you to switch from Pidgin
or whatever IM client you may be using right now to Instantbird. We
respect your freedom, we respect your choices, we love you!

.. |Instantbird crash reporter| image:: {filename}/images/crash-breakpad.png
.. _stability efforts: {filename}/articles/stability.rst
.. _Time Bubbles: {filename}/articles/introducing-time-bubbles.rst
.. _Magic copy: {filename}/articles/introducing-magic-copy.rst
