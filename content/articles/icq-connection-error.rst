ICQ connection error
####################
:date: 2010-11-17 00:29:54
:author: clokep
:category: Support
:tags: icq
:slug: icq-connection-error
:status: published

Recently users started to get an error ("Error: Unknown reason") while
attempting to connect to ICQ. This is being tracked in `bug
582 <https://bugzilla.instantbird.org/show_bug.cgi?id=582>`__. This will
occur using Instantbird 0.2 or 0.3a1pre nightly builds, if you are not
seeing this error then the rest of this post can be disregarded.

Luckily there is an easy work around for now:

#. Open the account manager ("Tools" > "Accounts")
#. Select your ICQ account and click "Properties"
#. On the "Advanced Options" tab

   -  change the "Server" to "login.icq.com"
   -  deselect "Use SSL"
   -  deselect "Use clientLogin"

`Other <http://developer.pidgin.im/wiki/ChangeLog>`__
`third <http://forums.cocoaforge.com/viewtopic.php?f=13&t=22834&sid=e56d3b94a0f337e49d37a4b9a5400076#p127686>`__
party instant messaging clients using one of the "old" login servers
were also affected.
