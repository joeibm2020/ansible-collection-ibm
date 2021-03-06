#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_function_action_info
short_description: Retrieve IBM Cloud 'ibm_function_action' resource

version_added: "2.8"

description:
    - Retrieve an IBM Cloud 'ibm_function_action' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.3.0
    - Terraform v0.12.20

options:
    annotations:
        description:
            - All annotations set on action by user and those set by the IBM Cloud Function backend/API.
        required: False
        type: str
    parameters:
        description:
            - All paramters set on action by user and those set by the IBM Cloud Function backend/API.
        required: False
        type: str
    name:
        description:
            - Name of action.
        required: True
        type: str
    limits:
        description:
            - None
        required: False
        type: list
        elements: dict
    exec:
        description:
            - None
        required: False
        type: list
        elements: dict
    publish:
        description:
            - Action visibilty.
        required: False
        type: bool
    version:
        description:
            - Semantic version of the item.
        required: False
        type: str
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
    ('name', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'annotations',
    'parameters',
    'name',
    'limits',
    'exec',
    'publish',
    'version',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    annotations=dict(
        required=False,
        type='str'),
    parameters=dict(
        required=False,
        type='str'),
    name=dict(
        required=True,
        type='str'),
    limits=dict(
        required=False,
        elements='',
        type='list'),
    exec=dict(
        required=False,
        elements='',
        type='list'),
    publish=dict(
        required=False,
        type='bool'),
    version=dict(
        required=False,
        type='str'),
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

    result = ibmcloud.ibmcloud_terraform(
        resource_type='ibm_function_action',
        tf_type='data',
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
