Status Update: April 17, 2012
#############################
:date: 2012-04-17 13:52
:author: clokep
:category: Development
:tags: irc, mozilla, status update
:slug: status-update-april-17-2012
:status: published

A lot has happened in the past two months since our last post: we've
been quite busy trying to fix `the list of blockers for Instantbird
1.2 <https://bugzilla.instantbird.org/buglist.cgi?quicksearch=sw%3A1.2-blocking&list_id=1120>`__!

We've again joined Mozilla as part of their application for `Google
Summer of
Code <http://www.google-melange.com/gsoc/homepage/google/gsoc2012>`__.
You can see some of our ideas on `Mozilla's
wiki <https://wiki.mozilla.org/Community:SummerOfCode12#Instantbird>`__.
(We should find out soon whether Instantbird will be doing any projects
or not this year!)

What's New?
===========

.. raw:: html

   <ul>
   <li>

The JavaScript IRC implementation has landed! Many minor bugs were also
fixed. The behavior is mostly the same as the old libpurple
implementations, but there are differences. If you see issues, please
`file a bug <https://bugzilla.instantbird.org/enter_bug.cgi>`__! This
will allow for better IRC support in the future.

.. raw:: html

   </li>
   <li>

The tab completion algorithm has been made smarter:

.. raw:: html

   </li>

-  It now prefers the last person to have pinged you if there are
   multiple possible completions.
-  Addressing multiple participants is now handled gracefully.

.. raw:: html

   <li>

There is now a reading position marker to show which messages arrived
since you last viewed a conversation.

.. raw:: html

   </li>
   <li>

Updated to Mozilla 11.

.. raw:: html

   </li>
   <li>

A few crashers have been fixed.

.. raw:: html

   </li>
   </ul>

What’s Coming Soon / Being Worked On?
=====================================

-  Minor IRC fixes: see `known IRC
   bugs <https://bugzilla.instantbird.org/buglist.cgi?quicksearch=component%3AIRC&list_id=1122>`__
   (in particular, better error handling).
-  `Upgrade to libpurple
   2.10.3 <https://bugzilla.instantbird.org/show_bug.cgi?id=1337>`__.
-  Other `Instantbird 1.2
   blockers <https://bugzilla.instantbird.org/buglist.cgi?quicksearch=sw%3A1.2-blocking&list_id=1120>`__!

What's this I hear about Thunderbird integrating instant messaging code from Instantbird?
=========================================================================================

You
`may <http://www.rumblingedge.com/2012/03/13/instant-messaging-in-thunderbird-just-got-landed-should-appear-in-tomorrows-nightlies/>`__
`have <https://wiki.mozilla.org/Features/Thunderbird/Instant_messaging_in_Thunderbird>`__
heard that instant messaging was recently added to Thunderbird. This
work was done by our very own Florian Quèze! Don't panic though! This
doesn't mean that Instantbird development is stopping, we strongly
believe there is a place for both a standalone instant messenger and a
more integrated approach with email. This is a mutually beneficial
relationship between Instantbird and Thunderbird where we share code,
benefit from more testing and get a set of new people -- and ideas --
involved in making instant messaging easier and more about how you --
the user -- wants it!

For those curious, approximately `one-third of the Instantbird
codebase <http://lxr.instantbird.org/instantbird/source/chat>`__ is now
`in Thunderbird's
Daily <http://mxr.mozilla.org/comm-central/source/chat/>`__ and
Earlybird builds.  Feel free to give it a try and file any bugs in
`Mozilla's
bugtracker <https://bugzilla.mozilla.org/enter_bug.cgi?product=Thunderbird&component=Instant%20Messaging>`__.
Currently it looks like this feature will likely appear in Thunderbird
15.

We're getting close to the Instantbird 1.2 release and we think there's
been a lot of great improvements that will make it easier and more
natural to instant message with your friends, family, co-workers and
others!
