Instantbird 1.2 Released!
#########################
:date: 2012-08-08 14:31:41
:author: clokep
:category: Downloads
:tags: 1.2, announce, downloads
:slug: instantbird-1-2-released
:status: published

We're very proud to release Instantbird 1.2, which has a huge number of
improvements!  If you love Instantbird 1.1, you'll definitely appreciate
the improvements made in this release; and if you don't use Instantbird
yet...well I'd suggest you `give it a
try <http://www.instantbird.com/download-all.html>`__! You can read the
full list of changes (403 to be precise) in the `release
notes <http://www.instantbird.com/release-notes.html>`__.

Instantbird 1.2 took way more time to finish (10 months!) than we
originally expected, and even though there's a very long list of
improved details, there's no major new features. So you may wonder...
what happened?!?

Well, the reason why it took so long is...
`Thunderbird <http://www.mozilla.org/en-US/thunderbird/>`__! The major
change that came with Instantbird 1.2 is that the chat back-end code is
now shared with Thunderbird, that will feature instant messaging support
in its version 15, to be released in a few weeks.

This forced us to give priority to some long standing side projects that
were interesting for Instantbird, but not immediately required: as
Thunderbird can't use libpurple which has an incompatible license, we
had to finish sooner, rather than later, some major architectural
changes to ensure that our chat back-end doesn't depend on libpurple at
all. That's right, Instantbird 1.2 is no longer based on libpurple (but
still uses it to support many protocols of course).

Our back-end working without libpurple wasn't enough for Thunderbird:
the only protocol plug-in shipped in Instantbird 1.0 and 1.1 that didn't
use libpurple was Twitter; more were obviously needed. Fortunately, we
were already cooking a JavaScript implementation of XMPP (started during
Google Summer of Code 2011) and IRC (it's been Patrick's side project
for years!). Our initial goal when we started working on these 2
protocol reimplementations in JavaScript was to gain full control of the
way these important protocols are handled by Instantbird, and to improve
their extensibility. For Thunderbird, finishing them became a priority,
and it's where we spent most of our time!

As I'm talking a lot about Thunderbird, you may be wondering if this
involvement of the Instantbird team in the Thunderbird project could
mean we are discontinuing the development of Instantbird as a
stand-alone application. Not at all! We believe both applications
complement each other very well, and have different use cases. While
Thunderbird, with integrated email and IM, may be better for users who
work all day long with their email client and IM the same contacts; we
believe lots of home users tend to use a webmail instead of a local
email client and would prefer to keep their IM application separate.

We're very excited that Instantbird is developing closer ties with
Mozilla, who we think shares a `similar <http://www.instantbird.org/>`__
`mission <http://www.mozilla.org/about/manifesto.en.html>`__ of allowing
users, YOU, to control their own privacy on the Internet! A few of our
developers are now "peers" of Mozilla's new `chat
module <https://wiki.mozilla.org/Modules/Chat>`__, and we are pursuing
more opportunities to bring Instantbird closer to Mozilla in the future.

We hope you'll enjoy using Instantbird 1.2 as much as we are and we
greatly look forward to the next version of Instantbird! As always, if
you see any bugs please `file a
bug <https://bugzilla.instantbird.org>`__, `catch us on
IRC <irc://irc.mozilla.org/#instantbird>`__ or `email
us <mailto:contact@instantbird.org>`__!
