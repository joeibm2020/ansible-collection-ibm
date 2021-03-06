#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_cis_origin_pool
short_description: Configure IBM Cloud 'ibm_cis_origin_pool' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_cis_origin_pool' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.3.0
    - Terraform v0.12.20

options:
    cis_id:
        description:
            - (Required for new resource) CIS instance crn
        required: False
        type: str
    name:
        description:
            - (Required for new resource) name
        required: False
        type: str
    check_regions:
        description:
            - (Required for new resource) 
        required: False
        type: list
        elements: str
    monitor:
        description:
            - None
        required: False
        type: str
    origins:
        description:
            - (Required for new resource) 
        required: False
        type: list
        elements: dict
    created_on:
        description:
            - None
        required: False
        type: str
    modified_on:
        description:
            - None
        required: False
        type: str
    description:
        description:
            - None
        required: False
        type: str
    enabled:
        description:
            - (Required for new resource) 
        required: False
        type: bool
    minimum_origins:
        description:
            - None
        required: False
        type: int
        default: 1
    notification_email:
        description:
            - None
        required: False
        type: str
    healthy:
        description:
            - None
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
    ibmcloud_api_key:
        description:
            - The API Key used for authentification. This can also be
              provided via the environment variable 'IC_API_KEY'.
        required: True
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
    ('cis_id', 'str'),
    ('name', 'str'),
    ('check_regions', 'list'),
    ('origins', 'list'),
    ('enabled', 'bool'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'cis_id',
    'name',
    'check_regions',
    'monitor',
    'origins',
    'created_on',
    'modified_on',
    'description',
    'enabled',
    'minimum_origins',
    'notification_email',
    'healthy',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    cis_id=dict(
        required=False,
        type='str'),
    name=dict(
        required=False,
        type='str'),
    check_regions=dict(
        required=False,
        elements='',
        type='list'),
    monitor=dict(
        required=False,
        type='str'),
    origins=dict(
        required=False,
        elements='',
        type='list'),
    created_on=dict(
        required=False,
        type='str'),
    modified_on=dict(
        required=False,
        type='str'),
    description=dict(
        required=False,
        type='str'),
    enabled=dict(
        required=False,
        type='bool'),
    minimum_origins=dict(
        default=1,
        type='int'),
    notification_email=dict(
        required=False,
        type='str'),
    healthy=dict(
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
    ibmcloud_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IC_API_KEY']),
        required=True),
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

    result = ibmcloud.ibmcloud_terraform(
        resource_type='ibm_cis_origin_pool',
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
