Context Menus
#############
:date: 2010-07-11 19:04:37
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

.. |Buddy context menu| image:: http://blog.instantbird.org/images/buddy_context-menu2.png
.. |Buddy list context menu| image:: http://blog.instantbird.org/images/blist_context-menu2.png
.. |Account context menu| image:: http://blog.instantbird.org/images/account_context-menu2.png
.. |Tab context menu| image:: http://blog.instantbird.org/images/tab_context-menu2.png
.. |Content context menu| image:: http://blog.instantbird.org/images/text_context-menu2.png
