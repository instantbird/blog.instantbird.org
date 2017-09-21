Instantbird 1.5 Released!
#########################
:date: 2013-12-20 21:12
:author: clokep
:category: Downloads
:tags: 1.5, announce, downloads
:slug: instantbird-1-5-released
:status: published

Instantbird 1.5 has been released: go `grab your copy now`_! There are a ton of
new features and bugs fixed for this new release, but we’d like to highlight a
couple of new features below.

.. class:: right

    |awesometab|

An exciting new feature you’ll find in Instantbird 1.5 is the New Conversation
tab. It displays a list of your contacts, ordered based on how frequently and
recently you’ve talked to them. Starting a conversation has never been easier!
No longer will you have to open a separate window and scroll through your
contact list to find a person. Just click the “+” button or press Ctrl/Cmd+T,
start typing the name of the contact, and you should see your contact appear at
the top of the list after typing only a few letters! You can then press enter
and your conversation opens! The first time you open the tab, Instantbird will
load your chat logs and learn who you talk to most often in order to offer
accurate suggestions. New friends might not show up at the top immediately, but
keep talking to them and they’ll reorder themselves. Don’t worry though, this
ranking data is kept only on your own computer and is not transmitted or shared
in any way!

Additionally, if you use Instantbird for IRC, the New Conversation tab will
automatically query your servers to download the list of channels that are
available to you. (This is generally known as LIST in IRC jargon.) Just like
with your contacts, you can type in the name of a channel and it’ll bubble to
the top of the list. Sometimes you don’t always know the channel name (that’s
why you’re searching, right?): we’ve got you covered there too! Instantbird will
search the channel topics in addition to channel names so you can quickly find
new channels to join!

.. class:: left

    |new-tooltips|

A very visible user interface improvement that was included for Instantbird 1.5
is redone tooltips that fit more into the visual style of the rest of the user
interface. They should be immediately familiar to Instantbird users as they’re
modeled after the conversation header! Hopefully this will help you find
information quickly and easily whether conversing with your contacts or just
checking their status.

For Linux users out there, we are still only offering 32-bit builds, although we
hope to change that soon! If you are running a 64-bit Linux distribution,
previously you’d have to install the ia32-libs (see our FAQ), but this has
changed in recent versions of Ubuntu which no longer offer this package. The
procedure now is to run:

.. code-block:: bash

    sudo apt-get install libgtk2.0-0:i386 libpangox-1.0-0:i386 libpangoxft-1.0-0:i386 libidn11:i386 libglu1-mesa:i386 libxt-dev:i386 libasound-dev:i386

If you’d like to see a complete list of what’s new in Instantbird 1.5, please
view the `release notes`_.

.. _grab your copy now: http://www.instantbird.com/download-all.html
.. _release notes: http://www.instantbird.com/release-notes.html

.. |awesometab| image:: {filename}/wp-content/uploads/2013/12/awesometab-300x217.png
    :class: alignnone size-full wp-image-395
    :width: 300px
    :height: 217px
    :target: {filename}/wp-content/uploads/2013/12/awesometab.png

.. |new-tooltips| image:: {filename}/wp-content/uploads/2013/12/new-tooltips-300x101.png
    :class: alignnone size-full wp-image-395
    :width: 300px
    :height: 101px
    :target: {filename}/wp-content/uploads/2013/12/new-tooltips-300x101.png
