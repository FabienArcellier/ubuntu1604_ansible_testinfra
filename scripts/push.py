#!/usr/bin/env python
# On CI, you can pass the logging and the password of dockerhub through
# the environment variables DOCKER_USERNAME and DOCKER_PASSWORD

import getpass
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

    docker_username = os.environ.get('DOCKER_USERNAME', None)
    if docker_username is None:
        docker_username = input('docker hub user (DOCKER_USERNAME) ? ')

    docker_password = os.environ.get('DOCKER_PASSWORD', None)
    if docker_password is None:
        docker_password = getpass.getpass('docker hub password (DOCKER_PASSWORD) ? ')

    _system('docker login -u {0} -p {1}'.format(docker_username, docker_password), logged=False)

    for docker_file, docker_image in docker:
        _system('docker build -f {0} -t {1} {2}'.format(docker_file, docker_image, ROOT_DIR))

    for _, docker_image in docker:
        _system('docker tag {0} {1}/{0}'.format(docker_image, docker_username))
        _system('docker push {1}/{0}'.format(docker_image, docker_username))

def _system(cmd, logged = True):
    if logged:
        print('$ {0}'.format(cmd))
    if os.system(cmd) > 0:
        raise OSError()

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))