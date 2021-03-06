#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_compute_vm_instance
short_description: Configure IBM Cloud 'ibm_compute_vm_instance' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_compute_vm_instance' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.3.0
    - Terraform v0.12.20

options:
    bulk_vms:
        description:
            - None
        required: False
        type: list
        elements: dict
    public_interface_id:
        description:
            - None
        required: False
        type: int
    private_vlan_id:
        description:
            - None
        required: False
        type: int
    ipv6_address_id:
        description:
            - None
        required: False
        type: int
    ssh_key_ids:
        description:
            - None
        required: False
        type: list
        elements: int
    hourly_billing:
        description:
            - None
        required: False
        type: bool
        default: True
    private_subnet_id:
        description:
            - None
        required: False
        type: int
    ipv6_static_enabled:
        description:
            - None
        required: False
        type: bool
        default: False
    block_storage_ids:
        description:
            - None
        required: False
        type: list
        elements: int
    placement_group_name:
        description:
            - The placement group name
        required: False
        type: str
    placement_group_id:
        description:
            - The placement group id
        required: False
        type: int
    flavor_key_name:
        description:
            - Flavor key name used to provision vm.
        required: False
        type: str
    ipv6_enabled:
        description:
            - None
        required: False
        type: bool
        default: False
    hostname:
        description:
            - None
        required: False
        type: str
    domain:
        description:
            - None
        required: False
        type: str
    ip_address_id_private:
        description:
            - None
        required: False
        type: int
    datacenter_choice:
        description:
            - The user provided datacenter options
        required: False
        type: list
        elements: dict
    secondary_ip_count:
        description:
            - None
        required: False
        type: int
    tags:
        description:
            - None
        required: False
        type: list
        elements: str
    public_subnet:
        description:
            - None
        required: False
        type: str
    public_security_group_ids:
        description:
            - None
        required: False
        type: list
        elements: int
    post_install_script_uri:
        description:
            - None
        required: False
        type: str
    image_id:
        description:
            - None
        required: False
        type: int
    private_network_only:
        description:
            - None
        required: False
        type: bool
        default: False
    dedicated_host_id:
        description:
            - None
        required: False
        type: int
    user_metadata:
        description:
            - None
        required: False
        type: str
    dedicated_host_name:
        description:
            - None
        required: False
        type: str
    private_security_group_ids:
        description:
            - None
        required: False
        type: list
        elements: int
    os_reference_code:
        description:
            - None
        required: False
        type: str
    transient:
        description:
            - None
        required: False
        type: bool
    public_vlan_id:
        description:
            - None
        required: False
        type: int
    wait_time_minutes:
        description:
            - None
        required: False
        type: int
        default: 90
    evault:
        description:
            - None
        required: False
        type: int
    ipv4_address:
        description:
            - None
        required: False
        type: str
    secondary_ip_addresses:
        description:
            - None
        required: False
        type: list
        elements: str
    file_storage_ids:
        description:
            - None
        required: False
        type: list
        elements: int
    public_bandwidth_limited:
        description:
            - None
        required: False
        type: int
    memory:
        description:
            - None
        required: False
        type: int
    public_subnet_id:
        description:
            - None
        required: False
        type: int
    local_disk:
        description:
            - None
        required: False
        type: bool
        default: True
    ip_address_id:
        description:
            - None
        required: False
        type: int
    ipv6_address:
        description:
            - None
        required: False
        type: str
    notes:
        description:
            - None
        required: False
        type: str
    public_bandwidth_unlimited:
        description:
            - None
        required: False
        type: bool
        default: False
    resource_status:
        description:
            - The status of the resource
        required: False
        type: str
    datacenter:
        description:
            - None
        required: False
        type: str
    private_subnet:
        description:
            - None
        required: False
        type: str
    disks:
        description:
            - None
        required: False
        type: list
        elements: int
    resource_controller_url:
        description:
            - The URL of the IBM Cloud dashboard that can be used to explore and view details about this instance
        required: False
        type: str
    public_ipv6_subnet:
        description:
            - None
        required: False
        type: str
    public_ipv6_subnet_id:
        description:
            - None
        required: False
        type: str
    resource_name:
        description:
            - The name of the resource
        required: False
        type: str
    cores:
        description:
            - None
        required: False
        type: int
    ipv4_address_private:
        description:
            - None
        required: False
        type: str
    dedicated_acct_host_only:
        description:
            - None
        required: False
        type: bool
    private_interface_id:
        description:
            - None
        required: False
        type: int
    network_speed:
        description:
            - None
        required: False
        type: int
        default: 100
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
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'bulk_vms',
    'public_interface_id',
    'private_vlan_id',
    'ipv6_address_id',
    'ssh_key_ids',
    'hourly_billing',
    'private_subnet_id',
    'ipv6_static_enabled',
    'block_storage_ids',
    'placement_group_name',
    'placement_group_id',
    'flavor_key_name',
    'ipv6_enabled',
    'hostname',
    'domain',
    'ip_address_id_private',
    'datacenter_choice',
    'secondary_ip_count',
    'tags',
    'public_subnet',
    'public_security_group_ids',
    'post_install_script_uri',
    'image_id',
    'private_network_only',
    'dedicated_host_id',
    'user_metadata',
    'dedicated_host_name',
    'private_security_group_ids',
    'os_reference_code',
    'transient',
    'public_vlan_id',
    'wait_time_minutes',
    'evault',
    'ipv4_address',
    'secondary_ip_addresses',
    'file_storage_ids',
    'public_bandwidth_limited',
    'memory',
    'public_subnet_id',
    'local_disk',
    'ip_address_id',
    'ipv6_address',
    'notes',
    'public_bandwidth_unlimited',
    'resource_status',
    'datacenter',
    'private_subnet',
    'disks',
    'resource_controller_url',
    'public_ipv6_subnet',
    'public_ipv6_subnet_id',
    'resource_name',
    'cores',
    'ipv4_address_private',
    'dedicated_acct_host_only',
    'private_interface_id',
    'network_speed',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    bulk_vms=dict(
        required=False,
        elements='',
        type='list'),
    public_interface_id=dict(
        required=False,
        type='int'),
    private_vlan_id=dict(
        required=False,
        type='int'),
    ipv6_address_id=dict(
        required=False,
        type='int'),
    ssh_key_ids=dict(
        required=False,
        elements='',
        type='list'),
    hourly_billing=dict(
        default=True,
        type='bool'),
    private_subnet_id=dict(
        required=False,
        type='int'),
    ipv6_static_enabled=dict(
        default=False,
        type='bool'),
    block_storage_ids=dict(
        required=False,
        elements='',
        type='list'),
    placement_group_name=dict(
        required=False,
        type='str'),
    placement_group_id=dict(
        required=False,
        type='int'),
    flavor_key_name=dict(
        required=False,
        type='str'),
    ipv6_enabled=dict(
        default=False,
        type='bool'),
    hostname=dict(
        required=False,
        type='str'),
    domain=dict(
        required=False,
        type='str'),
    ip_address_id_private=dict(
        required=False,
        type='int'),
    datacenter_choice=dict(
        required=False,
        elements='',
        type='list'),
    secondary_ip_count=dict(
        required=False,
        type='int'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    public_subnet=dict(
        required=False,
        type='str'),
    public_security_group_ids=dict(
        required=False,
        elements='',
        type='list'),
    post_install_script_uri=dict(
        required=False,
        type='str'),
    image_id=dict(
        required=False,
        type='int'),
    private_network_only=dict(
        default=False,
        type='bool'),
    dedicated_host_id=dict(
        required=False,
        type='int'),
    user_metadata=dict(
        required=False,
        type='str'),
    dedicated_host_name=dict(
        required=False,
        type='str'),
    private_security_group_ids=dict(
        required=False,
        elements='',
        type='list'),
    os_reference_code=dict(
        required=False,
        type='str'),
    transient=dict(
        required=False,
        type='bool'),
    public_vlan_id=dict(
        required=False,
        type='int'),
    wait_time_minutes=dict(
        default=90,
        type='int'),
    evault=dict(
        required=False,
        type='int'),
    ipv4_address=dict(
        required=False,
        type='str'),
    secondary_ip_addresses=dict(
        required=False,
        elements='',
        type='list'),
    file_storage_ids=dict(
        required=False,
        elements='',
        type='list'),
    public_bandwidth_limited=dict(
        required=False,
        type='int'),
    memory=dict(
        required=False,
        type='int'),
    public_subnet_id=dict(
        required=False,
        type='int'),
    local_disk=dict(
        default=True,
        type='bool'),
    ip_address_id=dict(
        required=False,
        type='int'),
    ipv6_address=dict(
        required=False,
        type='str'),
    notes=dict(
        required=False,
        type='str'),
    public_bandwidth_unlimited=dict(
        default=False,
        type='bool'),
    resource_status=dict(
        required=False,
        type='str'),
    datacenter=dict(
        required=False,
        type='str'),
    private_subnet=dict(
        required=False,
        type='str'),
    disks=dict(
        required=False,
        elements='',
        type='list'),
    resource_controller_url=dict(
        required=False,
        type='str'),
    public_ipv6_subnet=dict(
        required=False,
        type='str'),
    public_ipv6_subnet_id=dict(
        required=False,
        type='str'),
    resource_name=dict(
        required=False,
        type='str'),
    cores=dict(
        required=False,
        type='int'),
    ipv4_address_private=dict(
        required=False,
        type='str'),
    dedicated_acct_host_only=dict(
        required=False,
        type='bool'),
    private_interface_id=dict(
        required=False,
        type='int'),
    network_speed=dict(
        default=100,
        type='int'),
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
        resource_type='ibm_compute_vm_instance',
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
