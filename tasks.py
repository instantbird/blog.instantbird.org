# -*- coding: utf-8 -*-

import os
import sys

from invoke import run, task

from pelican.server import ComplexHTTPRequestHandler, RootedHTTPServer

# local path configuration (can be absolute or relative to tasks)
env = {
    'deploy_path': 'output',
    'port': 8000,
}


@task
def clean(ctx):
    """Delete any built output."""
    if os.path.isdir(env.get('deploy_path')):
        run('rm -rf {deploy_path}'.format(**env))
        run('mkdir {deploy_path}'.format(**env))


@task
def build(ctx):
    """Build the blog."""
    run('pelican -s pelicanconf.py content')


@task
def regenerate(ctx):
    """Watch files and continually build the blog as changes occur."""
    run('pelican -r -s pelicanconf.py content', pty=True)


@task
def serve(ctx):
    """Serve site at http://localhost:$PORT/ (default port is 8000)"""

    class AddressReuseTCPServer(RootedHTTPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(
        env['deploy_path'],
        ('', env['port']),
        ComplexHTTPRequestHandler)

    sys.stderr.write('Serving on port {port} ...\n'.format(**env))
    server.serve_forever()



@task
def preview(ctx):
    """Clean then build with the publish config."""
    clean(ctx)
    run('pelican -s publishconf.py content', pty=True)


@task
def publish(ctx):
    """Build with the publish config and push to the remote server."""
    preview(ctx)
    run('ghp-import -p -b master {deploy_path}'.format(**env))


@task
def import_wordpress(ctx):
    run('pelican-import --wpfile -o contents -m rst --dir-page bloginstantbirdorg.wordpress.2017-04-07.xml')
