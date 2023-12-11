#!/bin/usr/python3
"""script that generates a tgz archive
folder of the AirBnB Clone repo
"""
from datetime import datetime
from fabric.api import local
from os.path import isdir


@task
def do_pack():
    """generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        return None
