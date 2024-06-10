import os
import elabapi_python
from eLabFTW_config_api2 import Helper_elabftw

helper = Helper_elabftw()
api_client = helper.api_client

# create an instance of Experiments and another for Uploads
experimentsApi = elabapi_python.ExperimentsApi(api_client)
uploadsApi = elabapi_python.UploadsApi(api_client)

# upload a file in a specific directory to a existing experiment entry (e.g. with ID 399)
local_file_path = r"C:\path\to\file"
uploadsApi.post_upload('experiments', 399, file=local_file_path, comment='Uploaded with APIv2')

# upload the content of a folder in a specific directory
local_folder_path = r"C:\path\to\folder"
for filename in os.listdir(local_folder_path):
    local_file_path = os.path.join(local_folder_path, filename)
    if os.path.isfile(local_file_path):
        uploadsApi.post_upload('experiments', 399, file=local_file_path, comment='Uploaded with APIv2')