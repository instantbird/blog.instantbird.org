The Interruptions Manager
#########################
:date: 2011-10-15 00:24:52
:author: clokep
:category: Features
:tags: 1.1, addons, irc, preview
:slug: the-interruptions-manage
:status: published

For Instantbird 1.1, which will be released soon, we realized a weak
spot in our API was the ability to control whether events should be
shown to a user or cancelled under certain conditions.  This fits in as
part of our mission about giving control of instant messaging to the
user: the user should only be interrupted by events that deserve their
attention.  If you're wondering how this is useful; extensions now have
great control over how Instantbird is allowed to interact with the
user.  For example, extensions could: keep conversations from opening
(i.e. spam guards), quiet sounds during a full screen video, or even
stop new conversations from opening if the user has set their status as
Unavailable.

Extensions are able to simply register themselves with the interruptions
manager and they will automatically be notified if certain events
happen, including when Instantbird wants to: get your attention (e.g.
flash the task bar), open a new conversation, play a sound or show a
message notification.

The API is really easy to use and we've created some example add-ons
that use it!  We have created an an add-on to not allow the NickServ
from IRC accounts to open
(`source <http://hg.instantbird.org/addons/file/015cf6b699bc/nickservkiller>`__),
an update of
`NickServKiller <https://addons.instantbird.org/en-US/instantbird/addon/209>`__. 
Additionally there is an add-on to force auto-joined chats to be held on
the buddy list
(`source <http://hg.instantbird.org/addons/file/015cf6b699bc/hideautojoins>`__),
allowing you to give them your attention when you want to.  Another
example of a great add-on is the Do Not Disturb add-on, which does not
allow Instantbird to disturb the user while their status is set to
Unavailable, really allowing you to concentrate on something more
important
(`source <http://hg.instantbird.org/addons/file/ca4ba6af0b8a/donotdisturb>`__).

There's also a skeleton for an anti-spam add-on (an often requested
feature!) that is just waiting to be finished!  Contact us on
`#instantbird on irc.mozilla.org <irc://irc.mozilla.org/instantbird>`__
if you're interested in helping out.  And don't worry, these extensions
will be available on
`addons.instantbird.org <http://addons.instantbird.org>`__ soon!

We think this is a great addition for add-on developers working on
Instantbird and can't wait to see what exciting ideas people come up
with!
