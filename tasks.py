import os

from invoke import run, task

# local path configuration (can be absolute or relative to tasks)
env = {
    'deploy_path': 'output',
    'listen_port': 8000,
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
    """runly serve the blog."""
    run('cd {deploy_path} && python -m SimpleHTTP404Server {listen_port}'.format(**env), pty=True)


@task
def preview(ctx):
    """Clean then build with the publish config."""
    clean(ctx)
    run('pelican -s publishconf.py content', pty=True)


@task
def publish(ctx):
    """Build with the publish config and push to the remote server."""
    preview(ctx)
    run('ghp-import -p -b master output')
