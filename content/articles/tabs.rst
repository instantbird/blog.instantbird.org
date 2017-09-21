Tabs
####
:date: 2010-06-30 23:41
:author: flo
:category: Features
:tags: 0.2, preview, user interface
:slug: tabs
:status: published

During the 0.2 cycle, we spent a lot of time reworking the conversation
window. The conversation window will now feel more familiar to Firefox
users. That's because lots of parts have been borrowed and adapted. In
this post, and the next few posts, we will present features that are
already present in Firefox, but have been adapted for Instantbird.

Let's begin with tabs: conversations appear in tabs that work exactly
the same way as in Firefox 3.6.

Tab sizing
----------

Tabs are sized to take full advantage of the available space: when there
are only a few tabs, their width allows seeing most of the title of the
conversations, and a close button is visible on each tab, making it easy
to close a tab with a single click.

|Top of conversation window with 2 tabs and some free space|

If there are more tabs or if the window is smaller, the tabs shrink, and
the close button remains visible only on the selected tab to save space.

|Top of conversation window with 4 tabs, only one close button is
displayed|

If the space is really too limited to fit all the conversation tabs, the
tab bar becomes scrollable and a button appears to give the user a way
to display a list of all tabs at once.

|Top of conversation window with overflowing tabs, and the all tabs menu
opened|

All this makes very small conversation windows usable.

|Very small conversation window with 2 tabs|

Drag and drop
-------------

Tabs can be easily reordered, just drag a tab and drop it where you wish
it to be.

|dragging a tab, tab drop arrow visible in the same window|

Dropping a tab elsewhere detaches the tab to create a new window. The
new window appears where the tab was dropped.

|new window with only one tab|

Tabs can also be dragged between windows:

|dragging a tab, drop arrow visible in another window|

OS integration
--------------

On Mac OS X, the active conversation window is easy to distinguish from
the others, thanks to different colors of the tabs.

|An active and an inactive conversation window on Mac OS X|

.. |Top of conversation window with 2 tabs and some free space| image:: {filename}/images/tabs1-2tabsandfreespace.png
.. |Top of conversation window with 4 tabs, only one close button is displayed| image:: {filename}/images/tabs2-4tabs1closebutton.png
.. |Top of conversation window with overflowing tabs, and the all tabs menu opened| image:: {filename}/images/tabs3-overflowandalltabsmenu.png
.. |Very small conversation window with 2 tabs| image:: {filename}/images/tabs4-smallwindow.png
.. |dragging a tab, tab drop arrow visible in the same window| image:: {filename}/images/tabs5-reorder.png
.. |new window with only one tab| image:: {filename}/images/tabs6-detach.png
.. |dragging a tab, drop arrow visible in another window| image:: {filename}/images/tabs7-movebetweenwindows.png
.. |An active and an inactive conversation window on Mac OS X| image:: {filename}/images/tabs8-macosxactiveinactive.png

