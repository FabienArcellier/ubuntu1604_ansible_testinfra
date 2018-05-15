Ubuntu LTS docker image that help to [write white-box testing](https://en.wikipedia.org/wiki/White-box_testing) on ansible role
 or shell script with [py.test or testinfra](https://testinfra.readthedocs.io/en/latest/).

Images are built for ubuntu 18.04 and 16.04. Ubuntu 14.04 is not supported yet.

More information
================

* [dockerhub](https://hub.docker.com/r/fabienarcellier/ubuntu_ansible_testinfra/)

Use the image for white-box testing
===================================

```bash
docker pull fabienarcellier/ubuntu_ansible_testinfra:18.04
docker run -v "${PWD}":/mnt ubuntu_ansible_testinfra:18.04 py.test /mnt/tests/test_dockerfile.py
```

[the test](tests/test_dockerfile.py) run on a docker process and check `py.test` command is available
and that `ansible-playbook` run by default on localhost.

Build your own images
=====================

* fork the repo
* change the Dockerfile or create a new one
* use `scripts/push.py` or dockerhub CI to build and publish your own images on Dockerhub

