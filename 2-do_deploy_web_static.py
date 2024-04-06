#!/usr/bin/env python3
""" Fabric script to distribute an archive to a web server."""
from fabric.api import env
from fabric.api import put
from fabric.api import run
from os.path import exists

env.hosts = ["100.26.132.166", "100.25.179.168"]
env.user = '<03dde3405ef7>'


def do_deploy(archive_path):
    """Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if not exists(archive_path):
        return False
 
    try:
        # Upload the archive to /tmp/ directory on the web servers
        put(archive_path, '/tmp/')

        # Extract archive to /data/web_static/releases/
        archive_name = archive_path.split('/')[-1]
        folder_name = archive_name.split('.')[0]
        release_path = '/data/web_static/releases/{}'.format(folder_name)
        run('mkdir -p {}'.format(release_path))
        run('tar -xzf /tmp/{} -C {}'.format(archive_name, release_path))

        # Delete the archive from the web server
        run('rm /tmp/{}'.format(archive_name))

        # Move contents of the extracted folder to the releases folder
        run('mv {}/web_static/* {}'.format(release_path, release_path))

        # Remove the symbolic link /data/web_static/current
        current_link = '/data/web_static/current'
        if exists(current_link):
            run('rm -rf {}'.format(current_link))

        # Create a new symbolic link linked to the new version of code
        run('ln -s {} {}'.format(release_path, current_link))

        return True
    except Exception as e:
        print(e)
        return False
