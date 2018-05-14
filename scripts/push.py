#!/usr/bin/env python

import os
import subprocess
import sys

from builtins import input

SCRIPT_DIR = os.path.realpath(os.path.join(__file__, '..'))
ROOT_DIR = os.path.realpath(os.path.join(SCRIPT_DIR, '..'))

def main(arguments):
    docker = [
        ('Dockerfile.ubuntu1804', 'ubuntu1804_ansible_testinfra'),
        ('Dockerfile.ubuntu1604', 'ubuntu1604_ansible_testinfra'),
    ]

    docker_user_id = os.environ.get('DOCKER_USER_ID', None)
    if docker_user_id is None:
        docker_user_id = input('docker hub user (DOCKER_USER_ID) ? ')

    _system('docker login')

    for docker_file, docker_image in docker:
        _system('docker build -f {0} -t {1} {2}'.format(docker_file, docker_image, ROOT_DIR))

    for _, docker_image in docker:
        _system('docker tag {0} {1}/{0}'.format(docker_image, docker_user_id))
        _system('docker push {1}/{0}'.format(docker_image, docker_user_id))

def _system(cmd):
    print('$ {0}'.format(cmd))
    if os.system(cmd) > 0:
        raise OSError()

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))