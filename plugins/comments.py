"""
Customzied pelican comment system to do do the following:

* Add the gravatar to each comment.
* Do not use the extension when calculating the slug.

"""
import hashlib
import os

from pelican import signals

import six

from pelican_comment_system.comment import Comment


def pelican_initialized(pelican):
    def __init__(self, content, metadata, settings, source_path, context):
        super(Comment, self).__init__(content, metadata, settings, source_path,
                                      context)

        self.replies = []

        # Based on the gravatar plugin.
        if 'email' in metadata.keys():
            email_bytes = six.b(metadata['email']).lower()
            gravatar_url = "https://www.gravatar.com/avatar/" + \
                           hashlib.md5(email_bytes).hexdigest()
            self.avatar = gravatar_url
        else:
            self.avatar = 'woot woot'

        self.title = "Posted by:  {}".format(metadata['author'])

    Comment.__init__ = __init__


def register():
    signals.initialized.connect(pelican_initialized)
