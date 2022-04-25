from apiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools

#defining path variables:
client_secret_file_path = '/home/ra-terminal/Desktop/projects/project_ny_crime/g_drive_dir/credentials/client_secret_995747802585-mnfn1n2ikepcgn9a0k8nh8s7qu2tno51.apps.googleusercontent.com.json'
credentials_file_path = '/home/ra-terminal/Desktop/projects/project_ny_crime/g_drive_dir/credentials/credentials.json'

#define api scope
SCOPE = 'https://www.googleapis.com/auth/drive'

# define store
store = file.Storage(credentials_file_path)
credentials = store.get()# get access token
if not credentials or credentials.invalid:
    flow = client.flow_from_clientsecrets(clientsecret_file_path, SCOPE)
    credentials = tools.run_flow(flow, store)
