Better contact list
###################
:date: 2011-06-23 18:48:12
:author: flo
:category: Features
:tags: contacts, preview, user interface
:slug: better-contact-list
:status: published

The contact list was identified as a weak area of Instantbird 0.2. It
has been dramatically improved for Instantbird 0.3 which we plan to
release next week.

Tags
----

Goodbye groups
~~~~~~~~~~~~~~

Like most IM clients, Instantbird 0.2 had each contact placed in a
group, leading users to organize contacts a bit like files are placed in
folders on the disk.

While this seems ok at first, placing contacts inside groups doesn't
work well when thinking of the contact as a person. Don't you have a
friend (group 'friend') who is also a coworker (group 'colleagues')?

For this reason, with Instantbird 0.3 we replaced the notion of
"Groups" with the notion of "Tags" throughout the user interface.
While groups used to be containers for your contacts (it was possible
to move a contact from one group into another), tags are additional
data attached to the contact (you can add or remove tags on a contact,
but no longer 'move' a contact) and thus a single contact can have
multiple tags. To change the tags attached to a contact, use the
"Tags..." context menu item of the contact; it shows a list of the
existing tags with a check mark next to the tags attached to the
selected contact. Checking/unchecking a tag in this list will
attach/detach a tag from the contact.

|Tags menu|

Hidden tags
~~~~~~~~~~~

It's pretty common when using several accounts of different protocols on
a multi-protocol client for the first time to have contacts scattered
around in lots of meaningless tags. These contacts are typically those
that have never been moved before and are still in whatever the default
group of the various previous clients were.

As moving each of these contacts out of these meaningless groups is
not really an interesting task, and sometimes is even impossible (if
the server doesn't allow us to move it), we have designed a more
efficient way to forget the annoyance caused by the pointless
resulting tags: when hovering a tag in the contact list, you will see
an [x] icon. Clicking it will hide the tag (after showing an
explanation the first time).

|Hide tag icon|

It's possible to manage the list of visible tags (to unhide a tag) from
the "Visible tags..." context menu item.

Contacts which haven't been associated with a visible tag will be
displayed in a special "Other Contacts" tag, always at the bottom of the
contact list.

Grouped contacts
----------------

If several networks are usable to IM the same person, you will no longer
be annoyed by seeing that person listed several times in your contact
list. Just drag and drop one of these contacts onto another and
Instantbird will know they are both ways to contact the same person.

During future conversations, if your contact suddenly starts talking to
you from a different network, the conversation will continue in the same
tab. A system message will be displayed in the conversation to
unobtrusively notify you of this change.

If you want to start talking to a different account of your contact,
you can do so easily with a click on the protocol icon at the top
right of the conversation UI:

|Talk using a different network|

When starting a conversation from the contact list, Instantbird will
automatically select the best way to reach your contact, based on
availability information and your preference with regard to the
various ways to contact this person. You can change this preference by
expanding a contact (with the down arrow icon) and then using drag and
drop to reorder the accounts.

|Expanded contact|

Other noticable changes
-----------------------

-  The contact list is now sorted: both tags and contacts inside a tag
   appear alphabetically sorted.
-  Changes in the displayed information are smoothly animated, making
   them at the same time easier to understand and less interrupting.
-  Closing the contact list window, which is not needed all the time,
   will no longer close Instantbird. On Windows and Linux it will be
   minimized to the system tray (this behavior can be customized in the
   Preference dialog); on Mac it can be easily reopened from the
   menubar.

.. |Tags menu| image:: {static}/images/tags-menu.png
.. |Hide tag icon| image:: {static}/images/hide-tag-button.png
.. |Talk using a different network| image:: {static}/images/conversation-targets-menu.png
.. |Expanded contact| image:: {static}/images/expanded-contact.png

