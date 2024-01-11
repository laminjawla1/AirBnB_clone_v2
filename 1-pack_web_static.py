#!/usr/bin/python3
"""
Compress all files fom web_static directory and generates a .tgz archive file.
"""
import time
from fabric.api import local


def do_pack():
    """
    Pack all all files in web_static directory into an archive file
    """
    try:
        local("mkdir -p versions")
        local(
            "tar -cvzf versions/web_static_{}.tgz web_static/".format(
                time.strftime("%Y%m%d%H%M%S")
            )
        )
        return "versions/web_static_{}.tgz".format(
                time.strftime("%Y%m%d%H%M%S"))
    except Exception as e:
        return None
