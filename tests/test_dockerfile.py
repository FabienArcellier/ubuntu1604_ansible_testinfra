import os
SCRIPT_DIR = os.path.realpath(os.path.join(__file__, '..'))

def test_pytest_is_installed(host):
    assert host.exists("py.test")

def test_ansible_run_on_localhost(host):
    cmd = host.run("ansible-playbook {0}/fixture/validate_ansible.yml".format(SCRIPT_DIR))
    assert cmd.rc == 0, print(cmd.stdout)