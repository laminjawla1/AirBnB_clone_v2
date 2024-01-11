#!/usr/bin/python3
"""
Compress all files fom web_static directory, generates a .tgz archive file
and deploy the archive file to a remote server
"""
import time
from fabric.api import local, run, put


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


def do_deploy(archive_path):
    """
    Deploy the archive file to the remote web server
    """
    try:
        archived_file = archive_path[9:]
        version = "/data/web_static/releases/" + archived_file[:-4]
        archived_file = "/tmp" + archived_file

        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(newest_version))
        run("sudo tar -xzf {} -C {}/".format(
            archived_file, newest_version))
        run("sudo rm {}".format(archived_file))
        run("sudo mv {}/web_static/* {}".format(
            newest_version, newest_version))
        run("sudo rm -rf {}/web_static".format(newest_version))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(
            newest_version))

        print("Version {} is succesfully deployed!".format(version))
        return True
    except Exception as e:
        return False
