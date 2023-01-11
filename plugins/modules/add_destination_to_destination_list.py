#!/usr/bin/python
from ansible.module_utils.basic import *
from ansible_collections.sceptyre.ansible_umbrella.plugins.module_utils import umbrellaclient

def main():
    args = {}
    args.update({
        "username"  : {"type": "str", "required": True},
        "password"  : {"type": "str", "required": True},

        "domain"    : {"type": "str", "required": True},
        "destination_list_id": {"type": "str", "required": True}
    })

    mod = AnsibleModule(argument_spec=args)

    try:
        c = umbrellaclient.UmbrellaClient(
            mod.params.get("username"),
            mod.params.get("password")
        )

        r = c.destination_lists.add_destination_list_destination(
            mod.params.get("destination_list_id"),
            mod.params.get("domain")
        )

        # Out
        mod.exit_json(changed=True, meta=r['data'])

    except Exception as err:
        mod.fail_json(msg=err.message)

if __name__ == '__main__':
    main()