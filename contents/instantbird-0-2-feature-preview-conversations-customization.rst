Instantbird 0.2 feature preview: conversations customization
############################################################
:date: 2009-07-20 23:17
:author: flo
:category: Development
:tags: 0.2, chatting, preview, user interface
:slug: instantbird-0-2-feature-preview-conversations-customization
:status: published

In our `roadmap <http://wiki.instantbird.org/Instantbird:Roadmap>`__ we
stated that for 0.2 we were going to improve the conversation window,
and especially make it customizable. Let's show you an overview of what
we did.

Smileys
-------

People are used to see little images like |:-)| in conversations instead
of the plain text version ``:-)``. Testers of Instantbird 0.1.\* have
probably noticed that this feature was missing. No more.

Instantbird 0.2 supports smileys, and has a theme system for them.
`Creating a new smiley
theme <http://wiki.instantbird.org/Instantbird:Creating_a_smiley_theme>`__
is easy: it is just a bunch of images and a file (JSON format)
describing how to use them, bundled into an XPI file.

Message styles
--------------

Selecting a smiley theme is not enough for you to feel comfortable when
looking at your conversations? Ok, we have more! We have borrowed the
message style system of Adium to let you fully customize the way your
conversations look.

An image is worth a thousand words so... I'm gonna give you a `thousand
of
images <http://screenshots.instantbird.org/message-styles-preview/>`__.
Ok, not really a thousand, but we took a few hundreds of screenshots to
show how Instantbird is doing with the hundreds of Adium message styles
downloadable from
`adiumxtra.com <http://adiumxtras.com/index.php?a=search&cat_id=5>`__.

The compatibility is not perfect because there are some `differences in
the way Instantbird and Adium handle
themes <http://wiki.instantbird.org/Instantbird:Message_Styles:Differences_with_Adium>`__,
and some Adium themes may use some webkit-specific features, but most
themes look right.

This theme system is very flexible, and quite easy to learn. The
technologies used (HTML, CSS, JavaScript) are well known by
web-developers and web-designers. If you are not happy with the existing
themes, go ahead an create your own. And don't hesitate to let your
creativity play with all the cool `new developer features of Firefox
3.5 <https://developer.mozilla.org/En/Firefox_3.5_for_developers>`__.

Extensibility
-------------

The eye candy is cool but... I'm a developer, I want to create
extensions and I want to be able to interact with the conversations!
Don't worry, we love you too. We added several new APIs for extension
developers. It is now easy, for example, to change the way we filter
incoming messages, modify the text before it is displayed (adding links
for instance), and more coming!

.. |:-)| image:: http://blog.instantbird.org/smileys/sourire.png

