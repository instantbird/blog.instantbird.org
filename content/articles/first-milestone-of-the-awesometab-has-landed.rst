First Milestone of the Awesometab has landed!
#############################################
:date: 2013-07-22 09:00
:author: Benedikt P
:category: Community, Development, Features
:tags: community, GSoC
:slug: first-milestone-of-the-awesometab-has-landed
:status: published

*Awesometab* is the project name for a tab developed by `Nihanth Subramanya`_
during the `Google Summer of Code 2013`_ (via `Mozilla`_) which allows to
*quickly start the conversation you want to start*. The suggestions will be based
on several parameters like frequency and recency of previous conversations and
will show the most likely results when you open the new conversation-tab. It
will also include already ongoing conversations (*Switch to conversation*) and
suggestions for multi user chats such as IRC channels and XMPP chatrooms on the
servers that you’re connected to.

What’s this milestone that has landed already?
==============================================

After problems with the sheer size of the patch during last years GSoC project,
we decided to split this year’s projects into smaller parts that can land as
soon as they are ready.

So far a filterable contact list in a tab has landed that can easily be opened
using the common shortcut of *Ctrl+T* for *New Tab* (from both the contact list
or a conversation window) or by clicking the likewise familiar *New Tab*-button
in the tab bar.

.. class:: right

    |Awesometab|

    New conversation tab, list filtered for contacts starting with letter f

It features a search bar at top of the tab content which allows to refine the
results. It currently matches the entered name against each part of the
contact’s names but will do more later (see next section).

Contacts are displayed similar to results in Firefox’ awesomebar while retaining
the familiar look of the conversation header with the contact icon and status
indicator at the left and the contact name and status message to the right of
it. Additionally the tags of the contact are displayed, indicated by the same
icons as Firefox uses for tags on the Awesomebar.

Starting a conversation is as easy as single clicking on the result or selecting
an item with the keyboard and pressing Enter – a middle click opens the new
conversation in background instead while keeping the new conversation tab
visible, just in case that you need to start more than one conversation!

And what’s next?
================

The next step (already under development!) will be further improving this list
by integrating already ongoing conversations (*Switch to tab/conversation*).
We’d also like to include a way to filter the list by tags and to highlight the
text that matches the filter like the Awesomebar does.

Later on a ranking algorithm will be introduced and tweaked to show the most
important results first instead of the alphabetically sorted list that you
currently get when opening the tab.

These changes are most likely going to be integrated as soon as they are ready
and reviewed, so make sure you have a `nightly build`_ and update frequently!

I’m really happy to see how well this project is going, I’m already enjoying how
easy it became to start a conversation using the filterable contact list. I’m
looking forward to actually see the conversations I most likely want to start
right away!

Thanks, Nihanth, it’s really great work that you’re doing here!

.. _Nihanth Subramanya: http://awesometab.blogspot.de/
.. _Google Summer of Code 2013: http://www.google-melange.com/gsoc/homepage/google/gsoc2013
.. _Mozilla: http://blog.gerv.net/2013/06/gsoc-2013-project-list/
.. _nightly build: http://nightly.instantbird.im/

.. |Awesometab| image:: {static}/wp-content/uploads/2013/07/Awesomtab-blog-posting-Screen-Shot-2013-07-20-at-3.14.22-AM-300x232.png
    :width: 300px
    :height: 232px
    :target: {static}/wp-content/uploads/2013/07/Awesomtab-blog-posting-Screen-Shot-2013-07-20-at-3.14.22-AM.png
