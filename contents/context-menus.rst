Context Menus
#############
:date: 2010-07-08 14:32
:author: flo
:category: Features
:tags: 0.2, preview, user interface
:slug: context-menus
:status: published

Context menus (opened with a "right click") are a common and expected
part of the user interface. It can be very frustrating when they are
missing, so in Instantbird 0.2 we tried to add one wherever users are
likely to expect one.

In the buddy list, the context menu of contacts can be used to start a
conversation (although pressing enter or double clicking is usually
faster), show the conversation history, rename a contact, move the
contact to a different group or remove it from the list:

|Buddy context menu|\ 

The context menu is usable anywhere in the buddy list to toggle the
display of offline buddies:

|Buddy list context menu|

A context menu was added in the account manager too. There, it proposes
all the possible actions for an account. Since Instantbird 0.2, it's
possible to reorder the accounts in the list (this is also possible with
drag & drop using the mouse or with the keyboard using shift + the up or
down arrow).

|Account context menu|

A context menu is available on conversation tabs, with actions related
to that tab (opening it in a new window, closing it, ...) and to the
conversation, like showing the history of previous conversations with
the same contact.

|Tab context menu|

Last but not least, there's a context menu in conversation content. This
is the most "contextual" context menu we have added. The proposed
actions will vary depending on whether there is a selection or if the
context click was done over a link.

|Content context menu|

When selecting some text from a conversation, a common action is to copy
it to the clipboard and then paste it in a browser to use it as the
query in search engine. We have included search engine items directly in
the context menus to reduce the number of clicks needed for this common
case.

Written the 2010-07-11 at 19:04:37 by
`Florian <mailto:florian@instantbird.org>`__ in `Feature
preview <http://blog.instantbird.org/t4-context-menus.html>`__. `*3
comments* <http://blog.instantbird.org/a24-context-menus.html>`__

Cleaner UI
==========

In Instantbird 0.2 a lot of visual bloat has been removed from all
windows. Some margins have been reduced, borders that weren't useful for
clarity have been removed, and alignments have been improved. All of
this contributes to a better use of the available space on the screen,
and to a better perceived impression of simplicity in the user
interface.

To illustrate this, let's compare the conversation window before and
after:

|Conversation windows in Instantbird 0.2 and 0.1.3|

The buddy list has also been improved:

|Buddy list windows in Instantbird 0.2 and 0.1.3|

The status can now be changed directly from the top of the buddy list
instead of having to interact with a poor popup dialog. (Note that for
the users who hate clicking, the status can also be changed quickly
using commands from conversation windows: ``/away`` ``/dnd`` ``/back``
``/offline``.)

The account manager has also been simplified a lot, and is now usable in
a much smaller window:

|Account manager windows in Instantbird 0.2 and 0.1.3|

.. |Buddy context menu| image:: http://blog.instantbird.org/images/buddy_context-menu2.png
.. |Buddy list context menu| image:: http://blog.instantbird.org/images/blist_context-menu2.png
.. |Account context menu| image:: http://blog.instantbird.org/images/account_context-menu2.png
.. |Tab context menu| image:: http://blog.instantbird.org/images/tab_context-menu2.png
.. |Content context menu| image:: http://blog.instantbird.org/images/text_context-menu2.png
.. |Conversation windows in Instantbird 0.2 and 0.1.3| image:: http://blog.instantbird.org/images/conv_before-after.png
.. |Buddy list windows in Instantbird 0.2 and 0.1.3| image:: http://blog.instantbird.org/images/blist_before-after.png
.. |Account manager windows in Instantbird 0.2 and 0.1.3| image:: http://blog.instantbird.org/images/am_before-after.png

