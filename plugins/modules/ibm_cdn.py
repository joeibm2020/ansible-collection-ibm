#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_cdn
short_description: Configure IBM Cloud 'ibm_cdn' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_cdn' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.3.0
    - Terraform v0.12.20

options:
    bucket_name:
        description:
            - None
        required: False
        type: str
    header:
        description:
            - None
        required: False
        type: str
    performance_configuration:
        description:
            - None
        required: False
        type: str
        default: General web delivery
    host_name:
        description:
            - (Required for new resource) 
        required: False
        type: str
    origin_address:
        description:
            - (Required for new resource) 
        required: False
        type: str
    cache_key_query_rule:
        description:
            - None
        required: False
        type: str
        default: include-all
    path:
        description:
            - None
        required: False
        type: str
        default: /*
    cname:
        description:
            - None
        required: False
        type: str
    certificate_type:
        description:
            - None
        required: False
        type: str
    protocol:
        description:
            - None
        required: False
        type: str
        default: HTTP
    http_port:
        description:
            - None
        required: False
        type: int
        default: 80
    status:
        description:
            - None
        required: False
        type: str
    https_port:
        description:
            - None
        required: False
        type: int
        default: 443
    respect_headers:
        description:
            - None
        required: False
        type: bool
        default: True
    file_extension:
        description:
            - None
        required: False
        type: str
        default: 
    vendor_name:
        description:
            - None
        required: False
        type: str
        default: akamai
    origin_type:
        description:
            - None
        required: False
        type: str
        default: HOST_SERVER
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
    ('host_name', 'str'),
    ('origin_address', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'bucket_name',
    'header',
    'performance_configuration',
    'host_name',
    'origin_address',
    'cache_key_query_rule',
    'path',
    'cname',
    'certificate_type',
    'protocol',
    'http_port',
    'status',
    'https_port',
    'respect_headers',
    'file_extension',
    'vendor_name',
    'origin_type',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    bucket_name=dict(
        required=False,
        type='str'),
    header=dict(
        required=False,
        type='str'),
    performance_configuration=dict(
        default='General web delivery',
        type='str'),
    host_name=dict(
        required=False,
        type='str'),
    origin_address=dict(
        required=False,
        type='str'),
    cache_key_query_rule=dict(
        default='include-all',
        type='str'),
    path=dict(
        default='/*',
        type='str'),
    cname=dict(
        required=False,
        type='str'),
    certificate_type=dict(
        required=False,
        type='str'),
    protocol=dict(
        default='HTTP',
        type='str'),
    http_port=dict(
        default=80,
        type='int'),
    status=dict(
        required=False,
        type='str'),
    https_port=dict(
        default=443,
        type='int'),
    respect_headers=dict(
        default=True,
        type='bool'),
    file_extension=dict(
        default='',
        type='str'),
    vendor_name=dict(
        default='akamai',
        type='str'),
    origin_type=dict(
        default='HOST_SERVER',
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
        resource_type='ibm_cdn',
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
