
ibm_service_plan_info -- Retrieve IBM Cloud 'ibm_service_plan' resource
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_service_plan' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.3.0
- Terraform v0.12.20



Parameters
----------

  service (True, str, None)
    Service name for example, cloudantNoSQLDB


  plan (True, str, None)
    The plan type ex- shared


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to


  ibmcloud_zone (False, any, None)
    Denotes which IBM Cloud zone to connect to in multizone environment. This can also be provided via the environmental variable 'IC_ZONE'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

