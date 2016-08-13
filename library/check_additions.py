#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
from subprocess import Popen
from subprocess import PIPE

def check_guest_additions():
    p1 = Popen(['ps', 'aux'], stdout=PIPE)
    p2 = Popen(['grep', 'VBoxService'], stdin=p1.stdout, stdout=PIPE)
    p1.stdout.close()
    output = p2.communicate()[0]
    
    if '/usr/sbin/VBoxService' in output:
        return True
    else:
        return False

def main():
    module = AnsibleModule(argument_spec = dict())

    if check_guest_additions() == True:
        chg = False
    else:
        chg = True

    module.exit_json(
        changed=chg,
        ansible_facts=dict(additions_is_installed=check_guest_additions())
    )

if __name__ == '__main__':
    main()
