Facebook Chat Issues
####################
:date: 2016-01-26 21:37:26
:author: nhnt11
:category: Support
:tags: facebook, status update
:slug: facebook-chat-issues
:status: published

Recently we’ve received many questions from users whose Facebook Chat accounts
will no longer connect in Instantbird.

Facebook `officially deprecated its XMPP gateway`_ on April 30th, 2015, but it
continued to function until recently. Unfortunately it appears this is no longer
the case.

After investigating the issue, we have been unable to find a workaround to keep
it working. However, since Facebook deprecated the gateway, it’s surprising it
even worked for this long!

Meanwhile, libpurple has a new protocol plugin that uses Facebook’s proprietary
chat API, which we are considering offering as part of a future release of
Instantbird.

Stay tuned!

.. _officially deprecated its XMPP gateway: https://developers.facebook.com/docs/chat
