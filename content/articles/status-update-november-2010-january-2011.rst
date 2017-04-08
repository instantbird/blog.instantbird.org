Status Update: November 2010 - January 2011
###########################################
:date: 2011-01-31 20:45
:author: clokep
:category: Development
:tags: status update
:slug: status-update-november-2010-january-2011
:status: published

It's been over two months from our last status update and a lot of
changes and updates have occurred (from
`changeset <http://hg.instantbird.org/instantbird/rev/02d87017c8ca>`__
to
`changeset <http://hg.instantbird.org/instantbird/rev/70d4ef408f3e>`__).
Below we list changes for the nightly trunk builds of Instantbird
(0.3a1pre).

Done:
-----

-  Basic support for Twitter was added (`bug
   598 <https://bugzilla.instantbird.org/show_bug.cgi?id=598>`__).
   When the twitter account is connected, a timeline conversation
   automatically opens. If the conversation is closed by the user, it's
   reopened automatically when new messages arrive. The user should
   disconnect the account from the account manager to prevent new
   messages from being displayed.
   There's a "track" advanced option that allows to specify keywords to
   track. This is a comma separated list of keywords. Comma means OR,
   space inside a keyword means AND.
-  The conversation UI has received a slight update:
   On Mac the splitter between the conversation and input boxes was
   `reduced <http://hg.instantbird.org/instantbird/rev/9616e11f0a4f>`__.
   For all operating systems, the status bar of the conversation window
   is now `automatically hidden when the window is made
   small <http://hg.instantbird.org/instantbird/rev/a2687b36dadd>`__.
-  After quite a lot of debate, the wording of the option for when to
   create a new conversation window was updated (`bug
   387 <https://bugzilla.instantbird.org/show_bug.cgi?id=387>`__).
-  An old regression where the new JavaScript logger used \*nix style
   line breaks on all systems was fixed so Windows logs can be viewed in
   Notepad (`bug
   473 <https://bugzilla.instantbird.org/show_bug.cgi?id=473>`__).
-  The conversation window can now be minimized with the ESC key (`bug
   441 <https://bugzilla.instantbird.org/show_bug.cgi?id=441>`__).
-  Support for `Windows CE was
   dropped <http://hg.instantbird.org/instantbird/rev/f2cd3e499f8d>`__.
-  The themes preference pane now shows if themes are disabled or
   incompatible (`bug
   364 <https://bugzilla.instantbird.org/show_bug.cgi?id=364>`__).
-  Multi-user chats now show an disconnected icon when offline or after
   leaving a room (`bug
   520 <https://bugzilla.instantbird.org/show_bug.cgi?id=520>`__).
-  libpurple has been updated to
   `2.7.9 <http://hg.instantbird.org/instantbird/rev/b9b12560d425>`__
   (from 2.7.3)
-  Localized strings with a keyboard accelerator were not localized
   properly in the 'Join Chat' dialog (`bug
   655 <https://bugzilla.instantbird.org/show_bug.cgi?id=655>`__).
-  For Developers:

   -  The menus are no longer created with a preprocessor directive and
      are now included via a XUL overlay (`bug
      622 <https://bugzilla.instantbird.org/show_bug.cgi?id=622>`__).
   -  A `large number of updates have occurred in
      jsProtoHelper.jsm <http://hg.instantbird.org/instantbird/log/82123845bacf/purple/purplexpcom/src/jsProtoHelper.jsm>`__,
      used to simplify the creation of JavaScript protocols. They are
      now able to access account-specific preferences (`bug
      495 <https://bugzilla.instantbird.org/show_bug.cgi?id=495>`__),
      handle username splits (`bug
      647 <https://bugzilla.instantbird.org/show_bug.cgi?id=647>`__),
      join chat rooms (`bug
      648 <https://bugzilla.instantbird.org/show_bug.cgi?id=648>`__). In
      addition, some bugs were fixed to ignore the libpurple proxy
      structure (`bug
      649 <https://bugzilla.instantbird.org/show_bug.cgi?id=649>`__),
      automatically highlight messages containing the user's nick in
      multi-user chats (`bug
      661 <https://bugzilla.instantbird.org/show_bug.cgi?id=661>`__),
      and `some clean up
      occurred <http://hg.instantbird.org/instantbird/rev/035f7d8d7f78>`__.

Next:
-----

-  Release 0.3 alpha 1.
-  Florian is attending
   `FOSDEM <https://wiki.mozilla.org/Fosdem:2011>`__, where he'll show
   Instantbird on `Sunday, February 6\ :sup:`th`,
   2011 <https://wiki.mozilla.org/Fosdem:2011/Schedule>`__ in a talk
   about XULRunner Applications entitled "Instantbird and Conkeror -- A
   view from the authors" (Axel Beckert will be discussing Conkeror).
-  Research into setting up a non-profit organization.

By the way... Happy new year! Yeah... we are late |;)|.

.. |;)| image:: http://blog.instantbird.org/smileys/clin_d%27oeil.png

