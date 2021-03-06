#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_is_vpn_gateway_connection
short_description: Configure IBM Cloud 'ibm_is_vpn_gateway_connection' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_is_vpn_gateway_connection' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.3.0
    - Terraform v0.12.20

options:
    peer_address:
        description:
            - (Required for new resource) 
        required: False
        type: str
    admin_state_up:
        description:
            - None
        required: False
        type: bool
        default: False
    local_cidrs:
        description:
            - None
        required: False
        type: list
        elements: str
    peer_cidrs:
        description:
            - None
        required: False
        type: list
        elements: str
    action:
        description:
            - None
        required: False
        type: str
        default: none
    interval:
        description:
            - None
        required: False
        type: int
        default: 30
    timeout:
        description:
            - None
        required: False
        type: int
        default: 120
    name:
        description:
            - (Required for new resource) 
        required: False
        type: str
    ike_policy:
        description:
            - None
        required: False
        type: str
    status:
        description:
            - None
        required: False
        type: str
    ipsec_policy:
        description:
            - None
        required: False
        type: str
    preshared_key:
        description:
            - (Required for new resource) 
        required: False
        type: str
    vpn_gateway:
        description:
            - (Required for new resource) 
        required: False
        type: str
    id:
        description:
            - (Required when updating or destroying existing resource) IBM Cloud Resource ID.
        required: False
        type: str
    state:
        description:
            - State of resource
        choices:
            - available
            - absent
        default: available
        required: False
    generation:
        description:
            - IBM Cloud infrastructure generation.
        choices:
            - 1
            - 2
        default: 2
        required: False
    ibmcloud_api_key:
        description:
            - (Required when generation = 2) The API Key used for
              authentification. This can also be provided via the environment
              variable 'IC_API_KEY'.
        required: False
    iaas_classic_username:
        description:
            - (Required when generation = 1) The IBM Cloud Classic
              Infrastructure (SoftLayer) user name. This can also be provided
              via the environmental variable 'IAAS_CLASSIC_USERNAME'.
        required: False
    iaas_classic_api_key:
        description:
            - (Required when generation = 1) The IBM Cloud Classic
              Infrastructure API key. This can also be provided via the
              environmental variable 'IAAS_CLASSIC_API_KEY'.
        required: False

    ibmcloud_region:
        description:
            - Denotes which IBM Cloud region to connect to
        default: us-south
        required: False
    ibmcloud_zone:
        description:
            - Denotes which IBM Cloud zone to connect to in multizone
              environment. This can also be provided via the environmental
              variable 'IC_ZONE'.
        required: False

author:
    - Jay Carman (@jaywcarman)
'''

# Top level parameter keys required by Terraform module
TL_REQUIRED_PARAMETERS = [
    ('peer_address', 'str'),
    ('name', 'str'),
    ('preshared_key', 'str'),
    ('vpn_gateway', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'peer_address',
    'admin_state_up',
    'local_cidrs',
    'peer_cidrs',
    'action',
    'interval',
    'timeout',
    'name',
    'ike_policy',
    'status',
    'ipsec_policy',
    'preshared_key',
    'vpn_gateway',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    peer_address=dict(
        required=False,
        type='str'),
    admin_state_up=dict(
        default=False,
        type='bool'),
    local_cidrs=dict(
        required=False,
        elements='',
        type='list'),
    peer_cidrs=dict(
        required=False,
        elements='',
        type='list'),
    action=dict(
        default='none',
        type='str'),
    interval=dict(
        default=30,
        type='int'),
    timeout=dict(
        default=120,
        type='int'),
    name=dict(
        required=False,
        type='str'),
    ike_policy=dict(
        required=False,
        type='str'),
    status=dict(
        required=False,
        type='str'),
    ipsec_policy=dict(
        required=False,
        type='str'),
    preshared_key=dict(
        required=False,
        type='str'),
    vpn_gateway=dict(
        required=False,
        type='str'),
    id=dict(
        required=False,
        type='str'),
    state=dict(
        type='str',
        required=False,
        default='available',
        choices=(['available', 'absent'])),
    generation=dict(
        type='int',
        required=False,
        fallback=(env_fallback, ['IC_GENERATION']),
        default=2),
    ibmcloud_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IC_API_KEY']),
        required=False),
    iaas_classic_username=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IAAS_CLASSIC_USERNAME']),
        required=False),
    iaas_classic_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IAAS_CLASSIC_API_KEY']),
        required=False),
    ibmcloud_region=dict(
        type='str',
        fallback=(env_fallback, ['IC_REGION']),
        default='us-south'),
    ibmcloud_zone=dict(
        type='str',
        fallback=(env_fallback, ['IC_ZONE']))
)


def run_module():
    from ansible.module_utils.basic import AnsibleModule
    import ansible.module_utils.ibmcloud as ibmcloud

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    # New resource required arguments checks
    missing_args = []
    if module.params['id'] is None:
        for arg, _ in TL_REQUIRED_PARAMETERS:
            if module.params[arg] is None:
                missing_args.append(arg)
        if missing_args:
            module.fail_json(msg=(
                "missing required arguments: " + ", ".join(missing_args)))

    # VPC required arguments checks
    if module.params['generation'] == 1:
        missing_args = []
        if module.params['iaas_classic_username'] is None:
            missing_args.append('iaas_classic_username')
        if module.params['iaas_classic_api_key'] is None:
            missing_args.append('iaas_classic_api_key')
        if missing_args:
            module.fail_json(msg=(
                "VPC generation=1 missing required arguments: " +
                ", ".join(missing_args)))
    elif module.params['generation'] == 2:
        if module.params['ibmcloud_api_key'] is None:
            module.fail_json(
                msg=("VPC generation=2 missing required argument: "
                     "ibmcloud_api_key"))

    result = ibmcloud.ibmcloud_terraform(
        resource_type='ibm_is_vpn_gateway_connection',
        tf_type='resource',
        parameters=module.params,
        ibm_provider_version='1.3.0',
        tl_required_params=TL_REQUIRED_PARAMETERS,
        tl_all_params=TL_ALL_PARAMETERS)

    if result['rc'] > 0:
        module.fail_json(
            msg=ibmcloud.Terraform.parse_stderr(result['stderr']), **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
