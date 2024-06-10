import os
import elabapi_python
from eLabFTW_config_api2 import Helper_elabftw

helper = Helper_elabftw()
api_client = helper.api_client

# create an instance of Experiments and another for Uploads
experimentsApi = elabapi_python.ExperimentsApi(api_client)
uploadsApi = elabapi_python.UploadsApi(api_client)

# create a blank new experiment
# exp = experimentsApi.post_experiment()

# create a new experiment and get back additional information (e.g. ID)
response_body, status_code, response_headers = experimentsApi.post_experiment_with_http_info()

# Search for "Location" anf returns a URL, splits in several parts and looks for the last element, which is ID
id = response_headers["Location"].split("/")[-1]

# upload a file in a specific directory
local_file_path = r"C:\path\to\file"
uploadsApi.post_upload('experiments', id, file=local_file_path, comment='Uploaded with APIv2')

# upload the content of a folder in a specific directory
local_folder_path = r"C:\path\to\folder"
for filename in os.listdir(local_folder_path):
    local_file_path = os.path.join(local_folder_path, filename)
    if os.path.isfile(local_file_path):
        uploadsApi.post_upload('experiments', id, file=local_file_path, comment='Uploaded with APIv2')