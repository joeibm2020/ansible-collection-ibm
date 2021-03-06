
ibm_certificate_manager_import -- Configure IBM Cloud 'ibm_certificate_manager_import' resource
===============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_certificate_manager_import' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.3.0
- Terraform v0.12.20



Parameters
----------

  issuer (False, str, None)
    None


  imported (False, bool, None)
    None


  status (False, str, None)
    None


  has_previous (False, str, None)
    None


  algorithm (False, str, None)
    None


  expires_on (False, int, None)
    None


  key_algorithm (False, str, None)
    None


  certificate_manager_instance_id (False, str, None)
    (Required for new resource)


  name (False, str, None)
    (Required for new resource)


  data (False, dict, None)
    (Required for new resource)


  description (False, str, None)
    None


  begins_on (False, int, None)
    None


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to


  ibmcloud_zone (False, any, None)
    Denotes which IBM Cloud zone to connect to in multizone environment. This can also be provided via the environmental variable 'IC_ZONE'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

