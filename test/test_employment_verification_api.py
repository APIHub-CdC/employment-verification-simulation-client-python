# coding: utf-8

"""
    API Employment Verification Sandbox

    This API lets you verify a person employment status. If a person has a job it also returns the industrial sector and the industry COVID risk segment.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: api@circulodecredito.com.mx
"""


from __future__ import absolute_import

import unittest

import apihub_emplotmentverification_client
from apihub_emplotmentverification_client.api.employment_verification_api import EmploymentVerificationApi  # noqa: E501
from apihub_emplotmentverification_client.configuration import Configuration
from apihub_emplotmentverification_client.rest import ApiException
from apihub_emplotmentverification_client.models.employment_verification import EmploymentVerification


from pprint import pprint
import uuid


class TestEmploymentVerificationApi(unittest.TestCase):
    x_api_key = 'GKD25Kfmc6VeoxGLAGtlrbYgZobDdB7S'
    host = 'https://circulodecredito-dev.apigee.net/sandbox'
    subscription_id = '286aa08b-ba73-4f38-a74e-add9927aceee'
    inquiry_id=None


    def setUp(self):
        configuration =Configuration(host=self.host)   
        self.api = EmploymentVerificationApi(apihub_emplotmentverification_client.ApiClient(configuration))  # noqa: E501

    def test_get_employment_verifications(self):        
        try:     
            api_response =  self.api.get_employment_verifications(self.x_api_key, page=1,per_page=5)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling TestEmploymentVerificationApi->test_get_employment_verifications: %s\n" % e)
   
    def test_post_employment_verification(self):
        try:     
                
            request = EmploymentVerification(
                curp = "PUPJ970229HDFZZG33",
                nss = None,
                email ="api33@circulodecredito.com.mx",
                employment_verification_request_id = str(uuid.uuid4()),
                subscription_id = self.subscription_id
            )  
           
            api_response =  self.api.post_employment_verification(self.x_api_key, request)
            pprint(api_response)
            if api_response != None:
                self.inquiry_id = api_response.inquiry_id
                self.get_employment_verification()
      

        except ApiException as e:
            print("Exception when calling TestEmploymentVerificationApi->test_post_employment_verification: %s\n" % e)

    def get_employment_verification(self):
        try:                
            api_response =  self.api.get_employment_verification(self.x_api_key, self.inquiry_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling TestEmploymentVerificationApi->get_employment_verification: %s\n" % e)


    


if __name__ == '__main__':
    unittest.main()
