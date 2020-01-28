Status Update: May 23, 2012
###########################
:date: 2012-05-23 15:37:27
:author: clokep
:category: Community, Development
:tags: GSoC, preview, status update
:slug: status-update-may-23-2012
:status: published

We've made quite a bit of improvements over the past few weeks. Although
a lot of the changes are behind the scenes or fixing regressions, there
are some exciting user facing changes, as detailed below! We've also
been working with our `Google Summer of Code 2012 student`_,
wnayes, quite a bit to get him up to speed of how things work in
Instantbird. He's made great progress on understanding the code and has
even fixed a bug (see the "top protocols" page, below)!

Landed Changes:
===============

.. class:: right

    |"Top Protocol" Page in the Account Wizard|

    "Top Protocol" Page in the Account Wizard"

* The account wizard now has a `"top protocols"
  page <https://bugzilla.instantbird.org/show_bug.cgi?id=1391>`__ to allow
  users to quickly set up accounts that are most applicable to them. This
  is localizable as different instant messaging networks are popular in
  different regions.
* Tab Completion improvements:

  * Will `no longer complete the same name multiple
    times <https://bugzilla.instantbird.org/show_bug.cgi?id=1393>`__.
  * You can now `cycle
    backwards <https://bugzilla.instantbird.org/show_bug.cgi?id=1395>`__
    through the list of completions by holding shift while pressing tab.
  * All matching names can be cycled through now, although they are
    `prioritized <https://bugzilla.instantbird.org/show_bug.cgi?id=1385>`__
    as:

    #. Names of people who have pinged you (i.e. said your name in the
       chat).
    #. Names of active participants.
    #. Names of inactive participants.

* IRC changes

  - IRC contacts (yes, you can add IRC nicks to your contacts list!) now
    have `tooltips which show the results of a WHOIS
    command <https://bugzilla.instantbird.org/show_bug.cgi?id=1123>`__.
  - Better support for `tracking if a nick is
    online/away/offline <https://bugzilla.instantbird.org/show_bug.cgi?id=1369>`__.
  - The `topic UI <https://bugzilla.instantbird.org/show_bug.cgi?id=318>`__ now
    reflects whether you have permission to edit it.
  - Many bugs were fixed and error messages were added as fallout to the
    landing of JavaScript-IRC. Thanks for filing bugs!

Google Summer of Code Status:
=============================

The past few weeks were the "bonding" period for Google Summer of Code
students and their respective communities; actual work has started this
week. As part of the "bonding" period, we asked wnayes to check out `bug
1391: adding the "top protocols" page to the account
wizard <https://bugzilla.instantbird.org/show_bug.cgi?id=1391>`__ (see
above for a screenshot!).  We thought this would be a great introduction
to our tools (mostly Bugzilla and Mercurial), our workflow (requesting
reviews and feedback, discussing why changes were made, etc.), some of
the languages that we use (XUL, XBL, CSS, and JavaScript) and to some of
the account manager code that he will be working on this summer! wnayes
has done a great job and the changes are already in the `nightly
builds <http://nightly.instantbird.im/>`__!

To follow along with what wnayes will be working on this summer, you can
read his
`blog <http://www.tc.umn.edu/~nayes006/blog/index.php/category/gsoc/>`__
(`RSS
feed <http://www.tc.umn.edu/~nayes006/blog/index.php/feed/rss2/category/gsoc/>`__)
and check out his `user
repository <http://hg.instantbird.org/users/wnayes/>`__. Additionally,
he's posted some `general
information <http://www.tc.umn.edu/~nayes006/gsoc2012/index.php>`__ (his
application, timeline and a series of links) that he'll be updating as
the summer continues. (And of course you can stop by our IRC channel,
#instantbird on irc.mozilla.org, and say "Hi!")

.. _Google Summer of Code 2012 student: {static}/articles/google-summer-of-code-2012.rst

.. |"Top Protocol" Page in the Account Wizard| image:: {static}/wp-content/uploads/2012/05/top-protocol-page-300x243.png
   :class: size-medium wp-image-342
   :width: 300px
   :height: 243px
   :target: {static}/wp-content/uploads/2012/05/top-protocol-page.png
