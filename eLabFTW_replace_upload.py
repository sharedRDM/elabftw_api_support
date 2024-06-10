import os
import elabapi_python
from eLabFTW_config_api2 import Helper_elabftw

helper = Helper_elabftw()
api_client = helper.api_client

# create an instance of Experiments and another for Uploads
experimentsApi = elabapi_python.ExperimentsApi(api_client)
uploadsApi = elabapi_python.UploadsApi(api_client)

# define a file in a specific directory for a existing experiment entry (e.g. with ID 2359)
local_file_path = r"C:\path\to\file"
# read all uploads (attachements) of entry
response = uploadsApi.read_uploads('experiments', 2359)

# Get ID of first uploaded attachement in experiment entry
upload_id = response[0].id
print(upload_id)

# Get ID of all uploaded attachements in experiment entry
# for upload in response:
#     id_value = upload.id
#     print(id_value)

# Replace existing upload with a new one
uploadsApi.post_upload_replace('experiments', 2359, upload_id, file=local_file_path)