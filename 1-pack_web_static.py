#!/usr/bin/env python3
""" 
Fabric script that generates a .tgz archive from the contents of the web_static
folder of the AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """ Generates a .tgz archive from the contents `web_static/`
    in AirBnB clone repo.

    Retruns:
        (str): path to archive if it's successfully generated, none otherwise
    """
    timestamp = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    archive_path = f'versions/web_static_{timestamp}.tgz'

    if not os.path.exists("versions"):
        os.makedirs("versions")

    result = local('tar -cvzf {} web_static'.format(archive_path))
    if result.succeeded:
        return archive_path
    else:
        return None
