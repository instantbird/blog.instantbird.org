Stability
#########
:date: 2010-07-04 20:43
:author: flo
:category: Development
:tags: 0.2, quality control
:slug: stability
:status: published

We care a lot about the stability of Instantbird. Again, the Mozilla
platform has some great tools to help us here.

Crash Reporting
---------------

In the unfortunate event of a crash, a window apologizing for the
interruption in your work flow will pop up, and suggest you send some
anonymous information about this issue to our servers. We can then
analyze it and fix it for a later version, to make Instantbird more
stable for you.

|Instantbird Crash Reporter dialog|

This crash reporting system has already helped us a lot to improve the
overall stability of Instantbird.

Crash detection and protection
------------------------------

In previous releases, the worst stability problem that occurred was a
crash during start up (while automatically connecting accounts). This
was very annoying since it was not possible to use the graphical user
interface to change the configuration of the accounts likely to be
related to the crash.

In Instantbird 0.2, we have addressed this issue by detecting if the
last connection attempt finished correctly, that is, without the
application being quit unexpectedly.

Start up crashes are very rare and you will most likely never run into
one, but if it does occur to you: don't worry! At the next start up, you
will see the account manager pop up with a message explaining the
situation and inviting you to either retry connecting or edit the
configuration of your accounts:

|Account manager with automatic connection disabled and an error message
explaining the problem|

If the crash occurred after you added an account or changed the
configuration of an account, this account will be the only one that
won't connect at the next startup, and the message in the account
manager will look like this:

|Account manager where an account was disabled because of a crash during
the last connection attempt.|

Updates
-------

When we identify the cause of common crashes, or when a serious issue is
discovered (for example, an IM network no longer works), we try to
quickly release a new minor version including a fix for the issue.

Instantbird will periodically check for updates and notify you
automatically if a newer version is available. If you accept the update,
it will then be downloaded automatically and applied during the next
start up.

|Dialog prompting the user to accept a security and stability update|

If you expect a new version, you can also force Instantbird to check now
for an updates, using the "Check for updates" menu item:

|Check for updates menu item|

Nightly builds
--------------

People who want to very closely follow the development of Instantbird
can decide to receive the `latest development
version <http://ftp.instantbird.com/instantbird/nightly/latest-trunk/>`__
daily through this update system. We call these versions the "nightly
builds." These builds are produced automatically every day so that new
issues can be detected early on, before they creep up into release
builds.

|About dialog of a Nightly build of Instantbird|

Feel free to use them, but watch out! They may not be stable, and if you
decide to use them, you are expected to do so to help us test the
bleeding edge features, not just be a cool kid who's got the new toy
first. So if there are bugs, please `report
them <http://bugzilla.instantbird.org/>`__ (`Filing a
bug <https://wiki.instantbird.org/Instantbird:Bugzilla>`__: what a bug
report should contain) instead of complaining.

.. |Instantbird Crash Reporter dialog| image:: {filename}/images/crash-breakpad.png
.. |Account manager with automatic connection disabled and an error message explaining the problem| image:: {filename}/images/autologin-crash-global.png
.. |Account manager where an account was disabled because of a crash during the last connection attempt.| image:: {filename}/images/autologin-crash-account.png
.. |Dialog prompting the user to accept a security and stability update| image:: {filename}/images/update1.png
.. |Check for updates menu item| image:: {filename}/images/update6.png
.. |About dialog of a Nightly build of Instantbird| image:: {filename}/images/nightly2.png

