Status Update: February 25, 2012
################################
:date: 2012-02-25 20:17:03
:author: clokep
:category: Development
:tags: status update
:slug: status-update-february-25-2012
:status: published

We've been awful at posting updates to our blog about what has been
going on! It's too late now to even blame it on the holidays, but we owe
you all an update about what’s been happening and here it is!  We do,
generally, still have status meetings on Monday’s at 6:00 PM Paris time
(that’s noon EST) in #instantbird on irc.mozilla.org.  Feel free to stop
by and tell us what you love or what you hate or anything else!

What’s New?
===========

-  Tab completion is now smarter: “active” nicknames are now favored in
   completions and your own nickname is avoided in completions unless
   it’s the only match.
-  The JavaScript XMPP protocol implementation developed by Varuna
   JAYASIRI for Google Summer of Code 2011 is now used for Facebook Chat
   and Google Talk accounts. It can’t yet fully replace the libpurple
   implementation until DNS SRV is supported.
-  You can now scroll to the first unread message after opening a
   conversation that was on hold by pressing Alt+Page Up (you can also
   scroll to the top of the conversation by pressing Alt+Page Up again
   after that)!
-  When opening a conversation on hold, the UI is now updated
   asynchronously if there are a lot of messages to restore. You may
   notice a progress bar has replaced the UI freeze we used to have in
   this situation.
-  Conversations are now logged in a JSON format to allow more
   information than the old plaintext logs.
-  You can now delete Twitter messages.
-  Passwords are now stored in the Mozilla password manager! Previous
   saved passwords will be migrated to the password manager
   automatically, but the old saved password in the preference system is
   not yet deleted.  This will be handled in a future update.
-  Buddy authorization requests have been rewritten to remove the
   (awful) modal dialogue!
-  Mozilla was updated to 9.0.1 and libpurple was updated to 2.10.1.
-  Various crashers have been fixed.
-  Additionally, a lot of code reorganization has occurred for ongoing
   work of sharing code with Thunderbird.

What’s Coming Soon / Being Worked On?
=====================================

-  Our JavaScript implementation of IRC should be landing in the nightly
   builds soon, which should have feature parity to the libpurple
   implementation.  Please test this out!  You can find more information
   in `bug
   507 <https://bugzilla.instantbird.org/show_bug.cgi?id=507>`__.
-  Integrate SIPE (`bug
   976 <https://bugzilla.instantbird.org/show_bug.cgi?id=976>`__).
-  Add a reading position marker to quickly find the last read message
   in a conversation, `bug
   860 <https://bugzilla.instantbird.org/show_bug.cgi?id=860>`__.
-  Upgrade to Mozilla 10.

What’s up with Instantbird 1.2?
===============================

We were hoping to release Instantbird 1.2 near the end of January,
2012.  Unfortunately there are a few blockers / regressions that have
been found, causing us to be unable to release.  Everything slated as
wanted or blocking Instantbird 1.2 can be seen on our
`Bugzilla <https://bugzilla.instantbird.org/buglist.cgi?quicksearch=sw%3A1.2>`__.

-  The l10n scripts need to be updated and translations need to be
   updated.
-  Decide whether to drop QQ (we need to support showing captchas to
   keep it): `bug
   1021 <https://bugzilla.instantbird.org/show_bug.cgi?id=1021>`__.
-  Finish the JavaScript XMPP work (not all of these necessarily need to
   be done for Instantbird 1.2):

   -  Handle setting a user’s icon.
   -  Allow adding/removing tags from a buddy.
   -  DNS SRV (not required for Facebook Chat or Google Talk): `Mozilla
      bug 14328 <https://bugzilla.mozilla.org/show_bug.cgi?id=14328>`__.
   -  Receiving formatted messages (`bug
      1231 <https://bugzilla.instantbird.org/show_bug.cgi?id=1231>`__).
   -  Sending private messages to MUC participants.
   -  MUC topics need to be supported.

-  Currently a contact will disappear and not reappear when their name
   changes for some reason, `bug
   1178 <https://bugzilla.instantbird.org/show_bug.cgi?id=1178>`__.
-  Conversations should show the history in new windows, `bug
   958 <https://bugzilla.instantbird.org/show_bug.cgi?id=958>`__.
-  All message styles (not just Bubbles) should support context
   messages, `bug
   1074 <https://bugzilla.instantbird.org/show_bug.cgi?id=1074>`__.

Again, please accept our sincerest apologies for not providing any
updates in the past couple of months about the progress we’ve made with
Instantbird.  We’re really excited about Instantbird 1.2 and can
hopefully get it out to everyone as soon as possible!  As always,
Instantbird is made great by the community and we’d love to have more
help in working on it!  If you have any ideas (or no ideas, but some
free time!) stop by #instantbird on irc.mozilla.org and we can have some
discussions or point you to ways to help you!
