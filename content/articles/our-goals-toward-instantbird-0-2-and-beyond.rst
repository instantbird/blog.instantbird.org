Our goals: toward Instantbird 0.2 and beyond
############################################
:date: 2010-06-29 14:21:45
:author: flo
:category: Development
:tags: 0.2, philosophy
:slug: our-goals-toward-instantbird-0-2-and-beyond
:status: published

As you may already know, Instantbird 0.2 will be released soon. The
development of this version has been going on for more than a year
already! While we have been busy adding new features or polishing
existing ones, we may have missed a few opportunities to communicate
about what we were doing, what we had already done, where we are going,
and why. And when we did write something about our new features, the
announcements lacked screenshots, and probably didn't convey much of our
enthusiasm.

The last few days before the 0.2 release are an opportunity for us make
up for our lack of communication.

The way toward Instantbird 1.0
------------------------------

Let's begin with a clarification about the way we are slowly but surely
going to our future 1.0 release. Our `initial
roadmap <http://wiki.instantbird.org/Instantbird:Initial_Roadmap>`__
contained the somewhat misleading claim that our goal for 1.0 was to
reach "feature parity" with `Pidgin <http://pidgin.im/>`__. This led
some people to believe that we were basically copying the Pidgin
graphical user interface and reimplementing it in XUL. Although this
could have held some truth for the earlier goal of Instantbird - which
was to provide the extensibility that is loved in Firefox and features
similar to those found in Pidgin - this is no longer the case.

When we implement a new feature in Instantbird, we carefully consider
how it is likely to be used. We think about the use cases. We look at
how the same problem has been handled by other existing IM clients, so
that we can benefit from what others have done before us. Sometimes we
take inspiration and implement something in a similar way to another
client (for instance the `message theme
system <http://wiki.instantbird.org/Instantbird:Message_Styles_reference>`__
that we have borrowed from `Adium <http://adium.im/>`__), but sometimes
things don't look satisfying and we have to look for a better solution.
We especially try to avoid exposing the user to new popup dialogs that
interrupt the user but don't seem absolutely necessary.

Once something is implemented, we do our best to take advantage of the
early feedback we get from our `nightly`_ testers.

So why are we doing this? Copying the interface of an existing
application as quickly as possible would be easier, and would lead to a
fast result. But it would be worthless. We don't need another Pidgin,
Adium, ... (insert the name of your favorite multi-protocol IM
application here). These applications already exist and are mostly
great, there's no point in cloning them. What we do care about is our
users: our current users of course, but also future users. We believe
instant messaging should be less frustrating. We want to build an
all-in-one instant messaging application that is as easy as possible to
use, yet powerful. We value simplicity and ease of use in the default
configuration, and at the same time we want to allow advanced
customizations. Developers with an idea should be able to easily
customize their IM client, like they can already do with their web
browser.

We value privacy, and respect your data. Instant messages often have
confidential or intimate content. We believe that our users should have
the power to decide how this information is used, and where it is
stored. This is the reason why even though more and more users decide to
use web applications like Gmail, Facebook or Meebo for their IM needs,
we believe that it is still relevant in 2010 to build an IM application
that runs directly on the computer you own.

We don't know yet how Instantbird 1.0 will be, it will need to be
discussed. With You. At this point we are discussing which improvements
will compose the 0.3 release. If you want to take part in this
discussion or have questions related to our long term goals, don't
hesitate to `get in touch <http://instantbird.com/contact.html>`__ with
us.

What's next?
------------

We are confident that if you have tried a release from the Instantbird
0.1.\* series, you will see Instantbird 0.2 as major improvement. And if
you haven't used Instantbird before, then the 0.2 release is a great
time to start! In the next few days, we will detail a few of the
features that already make Instantbird 0.2 a very usable instant
messaging application, despite its low version number.

.. _nightly: {filename}/articles/nightly-builds-available.rst
