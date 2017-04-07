Nightlies fixed and with upgraded libpurple
###########################################
:date: 2010-09-24 19:35
:author: flo
:category: Development
:tags: libpurple, nightly
:slug: nightlies-fixed-and-with-upgraded-libpurple
:status: published

-  We have nightly builds again on all 3 OSes.

   -  We have had issues on the physical machine that hosts our Windows
      and Linux compilation virtual machines. *Even* has been hard at
      work to get them back online as quickly as possible.
   -  Additionally, our Windows builds failed with the obscure
      ``gklayout.lib : fatal error LNK1106: invalid file or disk full: cannot seek to 0x2000D93C``
      error message. No, the disk wasn't full, that would be too easy to
      understand... After a lot of wasted effort trying to figure out
      what had changed in the configuration of that machine or in the
      code, we finally got the solution on IRC from *khuey* and *ted*
      (thanks!): reboot with the ``/3GB`` switch to extend the address
      space.

-  The add-ons manager is usable again on nightlies. We got tired of
   `bug 591801 <https://bugzilla.mozilla.org/show_bug.cgi?id=591801>`__
   and pushed for Instantbird a partial backout of the patch from `bug
   562797 <https://bugzilla.mozilla.org/show_bug.cgi?id=562797>`__. (I
   haven't attached it in the bug because this is clearly not a fix, but
   if other xulrunner application developers want to use it, it's
   `here <https://hg.instantbird.org/instantbird/file/97e5db711d11/tools/patches/partial-backout-bug-562797.patch>`__.
   I know Daniel was very happy to have it for
   `BlueGriffon <http://bluegriffon.org/>`__.)
-  Known issue: Message Styles currently don't work without `being
   unpacked in the profile
   folder <http://blog.mozilla.com/addons/2010/09/23/changes-to-how-extensions-are-installed-in-firefox-4/>`__.
   This means that even though the add-on manager now works, if you
   install Message Styles with it in your new nightly, they won't work.
   Message Styles that were already installed will continue to work even
   if you upgrade your nightly.
-  We have upgraded libpurple from version 2.6.6 to 2.7.3:

   -  No big disaster has been reported, so nightly testers probably
      don't need to fear the update.
   -  We are tracking the crash reports: we have seen some new reports
      related to the MSN protocol; we will investigate soon.
   -  The Gadu-Gadu protocol support has improved, but is not as fixed
      as we hoped it would be. We will see if we can find ways to fix
      it.
   -  Our translators may be interested in taking strings from
      translation files generated based on this new version to help them
      in the process of upgrading their locale. These new converted
      files are available
      `here <http://queze.net/goinfre/l10n/libpurple-2.7.3/>`__.

-  The patches for minor issues that had been waiting in bugzilla for
   quite a bit of time (because we didn't want to land them just before
   releasing 0.2 or in the middle of the ``js-proto`` and ``mozilla2``
   branch merges) have landed.
-  We have welcomed translators for two new locales: Chinese and Hebrew!
   |:)|
-  We have created an ``experiments``\ mercurial repository where
   contributors from our community are enthusiastically experimenting
   with projects that we look forward to integrating in the default
   Instantbird code base once they are ready:

   -  *Mic* is working on adapting Firefox Sync to work with
      Instantbird.
   -  *clokep* is working on a readable implementation of the IRC
      protocols in JavaScript, leveraging the work that has been done in
      the last few months on the ``js-proto`` branch.

-  I plan to start rewriting the backend of our buddy list next week.
   The goals of this work are to simplify the code, make it work
   correctly with protocol plugins implemented in JavaScript, and give
   us the necessary APIs to implement the contact and tag features we
   plan add for the 0.3 release.

As always, don't hesitate to `file
bugs <https://bugzilla.instantbird.org/enter_bug.cgi>`__ if you come
across them! You are also welcome to join us on IRC (in
`#instantbird <irc://irc.mozilla.org/#instantbird>`__, where we have
been more than 20 a few times this week!)

.. |:)| image:: http://blog.instantbird.org/smileys/sourire.png

