#!/usr/bin/python3
"""
Compress all files fom web_static directory, generates a .tgz archive file
and deploy the archive file to a remote server
"""

import os
from fabric.api import *
from datetime import datetime

env.hosts = ["54.160.88.197", "52.91.178.63"]
env.user = "ubuntu"


def do_pack():
    """
    Pack all all files in web_static directory into an archive file
    """

    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archived_f_path = "versions/web_static_{}.tgz".format(date)
    status = local("tar -cvzf {} web_static".format(archived_f_path))

    return archived_f_path if status.succeeded else None


def do_deploy(archive_path):
    """
    Deploy the archive file to the remote web server
    """
    if os.path.exists(archive_path):
        archived_file = archive_path[9:]
        newest_version = "/data/web_static/releases/" + archived_file[:-4]
        archived_file = "/tmp/" + archived_file
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(newest_version))
        run("sudo tar -xzf {} -C {}/".format(archived_file,
                                             newest_version))
        run("sudo rm {}".format(archived_file))
        run("sudo mv {}/web_static/* {}".format(newest_version,
                                                newest_version))
        run("sudo rm -rf {}/web_static".format(newest_version))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(newest_version))

        print("New version deployed!")
        return True

    return False
