Feedback received
#################
:date: 2011-09-06 19:29
:author: clokep
:category: Support
:tags: feedback
:slug: feedback-received
:status: published

Following the release of Instantbird 1.0, we've received a variety of
great feedback (if you haven't read some of our other posts: we love to
receive feedback, although we might not always agree) via our `contact
email
address <http://groups.google.com/group/instantbird-contact/topics>`__,
`our IRC channel <irc://irc.mozilla.org/instantbird>`__, our `bug
tracker <https://bugzilla.instantbird.org/>`__,
`Twitter <http://twitter.com/instantbird>`__ and what ever other ways
there are to communicate with us. We'd like to take some time to respond
to some of the popular requests we've got (or at the very least, point
you to the bug where you can follow any progress).

\ **File transfer support**: something we definitely want, but we also
want to give a good user experience. Unfortunately most protocols do not
transfer files efficiently or quickly (and many times they break when
behind firewalls, etc.), thus we wish to offer an alternative to using
the protocol file transfer before providing support for it: see `bug
9 <https://bugzilla.instantbird.org/show_bug.cgi?id=9>`__.

**Grouping buddies first by protocol then by group**: this has been
requested by multiple individuals, but we don't feel it would fit well
into Instantbird. Instantbird is a multi-protocol instant messaging
client that aims to integrate all of your accounts together (therefore
it doesn't make sense to separate your accounts on the contact list).

For example, is your "Friend" not your friend whether it's your MSN
account, your AIM account or your Facebook account? Of course they still
are! But perhaps you have different groups of friends on MSN than on AIM
(maybe one is your online gaming buddies and one is your high school
friends); well our suggestion is to move them to tags that make more
sense (i.e. make an "Online Gaming Buddies" tag for all your MSN friends
and a "School Friends" tag for all your AIM friends, in this example).

When asking people why they want this, the response usually is "that's
what <another IM client> does". Well, ok but we wish that you take more
of a 'contact level view' of people: `Combine your contacts that are the
same person`_ and
group them according to how you know them. (You can even put them in
multiple tags, if someone is your online gaming buddy AND from school!)

If there's a usecase that we're not covering here, please let us know!
(And don't forget that Instantbird is fully extensible, so you could
certainly write an extension to display the contacts grouped first by
protocol if you really need that feature.)

**Blocking buddies at the protocol level**: unfortunately support for
this isn't great depending on the protocol, but libpurple does support
it. We have two bugs on file; one is to `block individual
users <https://bugzilla.instantbird.org/show_bug.cgi?id=135>`__ and
another to `block all buddies not on your buddy
list <https://bugzilla.instantbird.org/show_bug.cgi?id=704>`__, which
might not be supported by all protocols.

**Blocking spam**: although this is similar to blocking buddies, it's
different in that you do not wish to block ALL people not on your buddy
list, but of course you still want to ignore the obvious spam messages!
See `bug 288 <https://bugzilla.instantbird.org/show_bug.cgi?id=288>`__
and `bug 887 <https://bugzilla.instantbird.org/show_bug.cgi?id=887>`__
for two ideas on how to implement this.

**Start with the operating system**: many people expect an IM client to
start with their operating system and although most operating systems
provide a way to manually make a program start on boot, it would be
convenient for Instantbird to provide an option to do this. This was
requested in `bug
376 <https://bugzilla.instantbird.org/show_bug.cgi?id=376>`__.

**Facebook "Not Authorized" error**: we added the solution to the
`FAQ <http://instantbird.com/faq.html#facebookauthorization>`__.

**Voice/video**: we'd love to support voice/video too! But libpurple
does not yet support voice/video on Windows or Mac, you can see `bug
568 <https://bugzilla.instantbird.org/show_bug.cgi?id=568>`__ for some
information on how we could support it in JavaScript protocols.

**OTR (off the record messaging)**: private messaging is something we
believe is useful, but it needs to be convenient and transparent to the
users (after authentication, of course!). Encrypted chat is not a
trivial task, especially when the protocols don't support it, but
there's a library (called Off the Record) which handles this for us, we
have a bug about integrating it: `bug
877 <https://bugzilla.instantbird.org/show_bug.cgi?id=877>`__.

**People want 64-bit Linux versions**: we actually currently `supply
unsupported 64-bit
builds <http://ftp.instantbird.org/instantbird/releases/1.0/contrib/>`__,
and there's a bug about making them official (`bug
395 <https://bugzilla.instantbird.org/show_bug.cgi?id=395>`__).

**Instantbird interrupts you**: if you receive a new IM window
Instantbird rudely pops to the front, this is mostly noticeable when
using another application as a fullscreen window (`bug
926 <https://bugzilla.instantbird.org/show_bug.cgi?id=926>`__). Luckily
for now, there's currently an easy workaround: keep a conversation
window opened and minimized, so that a new conversation appears in a tab
of the existing window instead of a new window.

**Being able to search/filter the contacts** would be helpful: we agree!
In fact we filed a bug about it: `bug
631 <https://bugzilla.instantbird.org/show_bug.cgi?id=631>`__.

| **System tray issues**:
| **Persist the tray icon**: the system tray icon should stay visible
  even when the buddy list is restored, see `bug
  749 <https://bugzilla.instantbird.org/show_bug.cgi?id=749>`__.
| **Single click to restore the tray icon**: `an
  extension <https://addons.instantbird.org/en-US/instantbird/addon/291/>`__
  was created to support this and by default the next version of
  Instantbird will use single click on Linux and double click on Windows
  (see `bug
  870 <https://bugzilla.instantbird.org/show_bug.cgi?id=870>`__).
| **Expand the system tray context menu to change the status**: this
  would be helpful and would match what was added to the jumplists for
  Windows 7, see `bug
  750 <https://bugzilla.instantbird.org/show_bug.cgi?id=750>`__ about
  any work on this.

| We've heard that **some protocols are having problems**:
| **QQ does not work**: we've had reports of QQ not connecting (QQ was
  actually dropped from Pidgin and spun off into a separate project
  (`libqq <http://code.google.com/p/libqq-pidgin/>`__), which we `intend
  to include <https://bugzilla.instantbird.org/show_bug.cgi?id=1021>`__.
| **ICQ does not connect with default settings**: we have begun to
  investigate this in `bug
  894 <https://bugzilla.instantbird.org/show_bug.cgi?id=894>`__, but it
  seems that SSL is broken for now.
| **Twitter has a variety of issues** and needs more work, including:
  retweeting and replying to messages, direct messaging and showing a
  list of who you follow and who follows you.
| A few suggestions to **replace the libpurple MSN with msn-pecan**: we
  actually have still not updated to the newest MSN code from libpurple
  2.9.0 (as it was causing crashes for one of our developers), see `bug
  907 <https://bugzilla.instantbird.org/show_bug.cgi?id=907>`__ for the
  details.

| People want **more protocols**:
| **IBM Lotus Sametime**: we've actually `added
  support <https://bugzilla.instantbird.org/show_bug.cgi?id=102>`__ for
  this in the nightly builds and it'll be included in the next version!
| **Bonjour**: this should be fairly easy to add on Mac, but Windows and
  Linux would require an extra library from Apple to support Bonjour. If
  you're interested in adding it, see `bug
  944 <https://bugzilla.instantbird.org/show_bug.cgi?id=944>`__.
| **SIPE (Microsoft Office Communicator)**: one of our developers has
  started working on this in `bug
  976 <https://bugzilla.instantbird.org/show_bug.cgi?id=976>`__.
| **Skype**: supporting Skype is non-trivial and requires Skype to be
  running in the background, use of (the non-free) SkypeKit or reverse
  engineering the protocol, see `bug
  563 <https://bugzilla.instantbird.org/show_bug.cgi?id=563>`__ for some
  ideas.

Lots of positive feedback! Including that Instantbird works great with
screen readers! We've received TONS of other great feedback as well,
this is just a summary of the popular feedback we've received.

Please remember that one of the team's goals is to keep Instantbird as
light as possible, and for that reason, we are trying to encourage the
idea of creating add-ons for things that may not seem as a core
necessity for the larger audience.

Development of Instantbird 1.1 is already well underway. We have a
tentative
`roadmap <https://wiki.instantbird.org/Instantbird:Roadmap:1.1>`__ for
it. We definitely plan to release faster than we used to do before
Instantbird 1.0. Our current target date for the next release is the end
of September!

.. _Combine your contacts that are the same person: {filename}/articles/better-contact-list.rst
