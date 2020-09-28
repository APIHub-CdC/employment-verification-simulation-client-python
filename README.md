# swagger-client
This API lets you verify a person employment status. If a person has a job it also returns the industrial sector and the industry COVID risk segment.

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import apihub_emplotmentverification_client
```

## Getting Started
##### Step 1. Get your x-api-key
Get your ```x-api-key``` Following step 1, 2 and 3 the start guide https://developer.circulodecredito.com.mx/guia-de-inicio

##### Step 2. Change url and request data

The following data to modify can be found in ```/test/test_employment_verification_api.py ``` It is important change of initializing the url and host. Modify the URL ```host=the_url```  and ```x_api_key = 'your_api_key'```, as shown in the following code snippet:

```python
class TestEmploymentVerificationApi(unittest.TestCase):
    x_api_key = 'your_api_key'
    host = 'the_url'
    subscription_id =None
    inquiry_id=None

    def setUp(self):
        configuration =Configuration(host=self.host)   
        self.api = EmploymentVerificationApi(apihub_emplotmentverification_client.ApiClient(configuration))  # noqa: E501

    ...
    def test_post_employment_verification(self):
        try:     
            request = EmploymentVerification(
                curp = "CURP",
                nss = None,
                email ="email@email.com.mx",
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

    ...

```

##### Step 3 Run the unit test

Having the previous steps, all that remains is to run the unit test, with the following command:

```sh
python3 test_employment_verification_api.py
```
## Author

api@circulodecredito.com.mx

