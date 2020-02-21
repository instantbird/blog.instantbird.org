Introducing magic copy
######################
:date: 2011-06-16 16:35:21
:author: flo
:category: Features
:tags: adium, user interface
:slug: introducing-magic-copy
:status: published

The surprise and enthusiasm of a few people about the "magic copy"
feature I mentioned briefly at the end of `my previous post`_
introducing time bubbles reminded me that we forgot to introduce this
feature when it landed for Instantbird 0.2 as part of our implementation
of `the Adium message theme system`_.

We decided to use this theme system because it seemed nice overall and
was already used by a few other clients as well. However there was
something we really didn't like: using a customized message theme could
make copied data from the conversation really hard to read, to the point
that it would be unsuitable for sending a quote via email.

As this may not be very clear yet, let me give an example:

|Copying from a conversation without the 'magic copy' feature|

This is the text we get when copying the selection to the clipboard and
pasting it. This is without our "magic copy" feature of course.

I should also note that the Bubbles theme used for this screenshot is
not the worst in this regards. I've seen in the description of some
themes (not designed for Instantbird) that they were "clipboard
friendly", which indicates the theme author took this problem into
account and probably had to make some trade-offs between the visual
appearance and the usability of copied conversations.

As we were not satisfied with this situation (which either makes copying
from the conversation poorly usable or restricts theme authors'
creativity), we developed a different system that instead of serializing
the selected HTML attempts to detect which messages are selected, and to
"prettyprint" them based on what Instantbird knows about the message,
rather than what is visible and selected.

This is the result:

|Same conversation copied with magic copy|

If only a part of a single message was selected, the username and
timestamp won't be added to the copied strings, it will behave like a
normal text copy:

|Copying a part of a single message|

As we detect which messages are selected and even know if each message
was fully selected or only in part, we can nicely add an ellipsis when
a message was cut:

|Ellipsis are added where messages are cut|

This even works when using multiple-selections (press Ctrl on
Windows/Linux, and Command on Mac to do this):

|Copying parts of multiple messages|

A few technical details: the template used to serialize copied messages
is both localizable and customizable from about:config, it's also
possible to completely turn off this feature in case it ever causes some
trouble (look for the ``messenger.conversations.selections.*`` family of
preferences in about:config).

This feature has been turned on by default in Instantbird for over a
year and nobody complained about it. Actually, it's one of the features
that is barely noticed because it just works, but it is something that
is really missed if using another IM client after using Instantbird for
a while.

.. _my previous post: {static}/articles/introducing-time-bubbles.rst
.. _the Adium message theme system: {static}/articles/instantbird-0-2-feature-preview-conversations-customization.rst

.. |Copying from a conversation without the 'magic copy' feature| image:: {static}/images/copy-normal.png
.. |Same conversation copied with magic copy| image:: {static}/images/copy-magic.png
.. |Copying a part of a single message| image:: {static}/images/copy-part-of-one-message.png
.. |Ellipsis are added where messages are cut| image:: {static}/images/copy-ellipsis.png
.. |Copying parts of multiple messages| image:: {static}/images/copy-multi-select.png

