#!/usr/bin/python3
""" 0x03. AirBnB clone - Deploy static, task 1. Compress before sending
"""
from fabric.api import local, env
from os import path, makedirs, listdir
from datetime import datetime


def do_pack():
    """ Generates a .tgz archive from the contents `web_static/`
    in AirBnB clone repo.

    Retruns:
        (str): full path from current directory to `.tgz` archive created in
    `versions/`, or `None` on failure
    """
    if not path.isdir("./versions"):
        makedirs("./versions")

    now = datetime.now().strftime('%Y%m%d%H%M%S')
    filename = 'versions/web_static_{}.thz'.format(now)
    result = local('tar -cvzf {} web_static/'.format(filename))

    if result.failed:
        return None
    else:
        return filename


if __name__ == "__main__":
    do_pack()
