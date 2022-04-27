from apiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools

import json

#defining path variables:
client_secret_file_path = '/home/ra-terminal/api_keys/google_key/credentials/client_secret_key.googleusercontent.com.json'
credentials_file_path = '/home/ra-terminal/api_keys/google_key/credentials/credentials.json'

#define api scope
SCOPE = 'https://www.googleapis.com/auth/drive'
DATASET_DIR_ID = '1xqZTsmkulmx7I0rVvgGP250o8A4rbZGS' 

# define store
store = file.Storage(credentials_file_path)
#get access token
credentials = store.get()

def get_cred_access(credentials, client_secret_file_path, credentials_file_path):

    try:
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(client_secret_file_path, SCOPE)
            credentials = tools.run_flow(flow, store)
            # print("Successful Connection:","Flow:",flow, "Creds:",credentials)
    except ConnectionError.errno:
        print("Unable to get credential access to drive api")
    else:
        # print("Successful Connection: Creds:",credentials)
        return credentials

# define API service
http = credentials.authorize(Http())
drive = discovery.build('drive', 'v3', http=http)

# define a function to retrieve all files
def get_all_files(api_service):
    results = []
    page_token = None

    while True:
        try:
            param = {}
            if page_token:
                param['pageToken'] = page_token
            files = api_service.files().list(**param).execute()            # append the files from the current result page to our list
            results.extend(files.get('files'))            # Google Drive API shows our files in multiple pages when the number of files exceed 100
            page_token = files.get('nextPageToken')

            if not page_token:
                break
        except error.HttpError as error:
            print(f'An error has occurred: {error}')
            break    # output the file metadata to console
    
    #dumping results into json
    with open('/home/ra-terminal/Desktop/projects/project_ny_crime/g_drive_metadata.json', 'w') as f_obj:
        json.dump(results, f_obj, indent=2)
    return results

def search_file(file_target):

    with open('/home/ra-terminal/Desktop/projects/project_ny_crime/g_drive_metadata.json', 'r') as f_obj:
        data_files = json.load(f_obj)
    for file in data_files:
        if file.get('name') == file_target:
            # return file.get('kind'), file.get('id'), file.get('name'), file.get('mimeType')
            return file


if __name__ == "__main__":
    credentials = get_cred_access(credentials, client_secret_file_path, credentials_file_path)
    print(credentials)
