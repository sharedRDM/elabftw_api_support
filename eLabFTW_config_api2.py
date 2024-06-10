import os
import time
import datetime
import elabapi_python
from elabapi_python.rest import ApiException

#########################
#         CONFIG        #
#########################
API_HOST_URL = 'URL_eLabFTW_Instance/api/v2'
# replace with your api key
API_KEY = 'API_KEY'
#########################
#      END CONFIG       #
#########################
class Helper_elabftw:
    def __init__(self):
        # Configure the api client
        self.configuration = elabapi_python.Configuration()
        self.configuration.api_key['api_key'] = API_KEY
        self.configuration.api_key_prefix['api_key'] = 'Authorization'
        self.configuration.host = API_HOST_URL
        self.configuration.debug = False
        self.configuration.verify_ssl = True
        #create an instance of the API class
        self.api_client = elabapi_python.ApiClient(self.configuration)
        # fix issue with Authorization header not being properly set by the generated lib
        self.api_client.set_default_header(header_name='Authorization', header_value=API_KEY)