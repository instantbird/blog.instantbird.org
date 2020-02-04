"""
Customzied pelican comment system to do do the following:

* Add the gravatar to each comment.
* Do not use the extension when calculating the slug.

"""
import hashlib
import os
from urllib.parse import urlencode

from pelican import signals

from pelican_comment_system.comment import Comment


def get_gravatar_url(email, size, default_image, rating='G'):
    """See https://en.gravatar.com/site/implement/images/."""
    # Based on the gravatar plugin.
    email_bytes = email.strip().lower().encode('ascii')

    # Configure some parameters.
    query = {
        's': size,
        'd': default_image,
        'r': rating,
    }

    # Generate the URL.
    return 'https://www.gravatar.com/avatar/' + hashlib.md5(email_bytes).hexdigest() + '?' + urlencode(query)


def pelican_initialized(pelican):
    def __init__(self, content, metadata, settings, source_path, context):
        super(Comment, self).__init__(content, metadata, settings, source_path,
                                      context)

        self.replies = []

        # Based on the gravatar plugin.
        self.avatar = get_gravatar_url(metadata.get('email', ''), 68, 'https://0.gravatar.com/avatar/ad516503a11cd5ca435acc9bb6523536?s=68')

        self.title = "Posted by:  {}".format(metadata['author'])

    Comment.__init__ = __init__


def register():
    signals.initialized.connect(pelican_initialized)
