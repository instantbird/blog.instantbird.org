Tab completion in Instantbird 1.2
#################################
:date: 2012-08-01 10:00:16
:author: aleth
:category: Features
:tags: 1.2, preview, tab complete, user interface
:slug: tab-completion-in-instantbird-1-2
:status: published

We've made some major improvements to the tab completion of nicknames
in IRC channels (and other chatrooms). The goal, as always, is to make it
"just work" (so you can think about more important things!).

Simply press |TAB| to complete the first couple of letters you have typed:

|image0|

To undo the completion, just press |Backspace| as usual.

If there is no unique nick that fits the bill, Instantbird tries to
guess which nick you mean from the context. For example, if you have
recently been pinged by someone, that nick is preferred. Otherwise it
just completes as much as possible, and shows you a list of
alternative completions:

|image1|

You can then always press |TAB| again to cycle through these candidate
nicks until you get the right one:

|image2|

(|Shift+TAB| will cycle through the list in the opposite direction.)

Notice how Instantbird automatically added a colon after the nick, as
we were addressing someone at the start of a message. And if you add
another nick, you get a comma-separated list:

|image3|

Of course, sometimes that may not be what you intended. So if you
delete the trailing colon by pressing |Backspace|, the punctuation
adjusts accordingly:

|image4|

Don't forget you can also reply to any message by double-clicking it!
This will add the sender's nick to the beginning of the message.

.. |TAB| raw:: html

    <span style="background: Gainsboro;border: 1px outset Ghostwhite;padding: 2px;font-size: smaller">TAB</span>

.. |Backspace| raw:: html

    <span style="background: Gainsboro;border: 1px outset Ghostwhite;padding: 2px;font-size: smaller">Backspace</span>

.. |Shift+Tab| raw:: html

    <span style="background: Gainsboro;border: 1px outset Ghostwhite;padding: 2px;font-size: smaller">Shift</span>+<span style="background: Gainsboro;border: 1px outset Ghostwhite;padding: 2px;font-size: smaller">TAB</span>

.. |image0| image:: {static}/wp-content/uploads/2013/07/tabc4.png
   :class: alignnone size-full
   :width: 406px
   :height: 95px
   :target: {static}/wp-content/uploads/2013/07/tabc4.png
.. |image1| image:: {static}/wp-content/uploads/2013/07/tc4-2.png
   :class: alignnone size-full
   :width: 597px
   :height: 150px
   :target: {static}/wp-content/uploads/2013/07/tc4-2.png
.. |image2| image:: {static}/wp-content/uploads/2013/07/tc6-6.png
   :class: alignnone size-full
   :width: 605px
   :height: 127px
   :target: {static}/wp-content/uploads/2013/07/tc6-6.png
.. |image3| image:: {static}/wp-content/uploads/2013/07/tc8-6.png
   :class: aligncenter size-full
   :width: 211px
   :height: 101px
   :target: {static}/wp-content/uploads/2013/07/tc8-6.png
.. |image4| image:: {static}/wp-content/uploads/2013/07/tc9-4.png
   :class: aligncenter size-full
   :width: 211px
   :height: 101px
   :target: {static}/wp-content/uploads/2013/07/tc9-4.png
