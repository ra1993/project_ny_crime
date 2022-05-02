from apiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools

import json
import pickle
import os
import pandas as pd
import requests
import io

# from googleapiclient.discover import build
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request
# from tabulate import tabulate

#defining path variables:
client_secret_file_path = '/home/ra-terminal/api_keys/google_key/credentials/client_secret_key.googleusercontent.com.json'
credentials_file_path = '/home/ra-terminal/api_keys/google_key/credentials/credentials.json'

#define api scope
SCOPE = 'https://www.googleapis.com/auth/drive'
SCOPE2 = 'https://www.googleapis.com/auth/drive.readonly'

# define store
store = file.Storage(credentials_file_path)
#get access token
credentials = store.get()

# define API service
http = credentials.authorize(Http())
drive = discovery.build('drive', 'v3', http=http)

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

def get_gtoken():
    with open('/home/ra-terminal/api_keys/google_key/credentials/credentials.json') as f_obj:
        cred = json.load(f_obj)
    
    return cred['access_token']

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

def read_csv_file(file_name):
    file = search_file('NYPD_Complaint_Data_Historic.csv')
    crime_file_id = file['id']

    access_token = get_gtoken()
    url = "https://googleapis.com/drive/v3/files/" + crime_file_id + "?alt=media"
    res = requests.get(url, headers={"Authorization": "Bearer" + access_token})
    print(res.text)
    df = pd.read_csv(io.StringIO(res.text))
    return df 

# def get_g_file():
#     file = driv
#     request = drive_service.files().get_media(fileId=crime_file_id)
#     fh = io.BytesIO()
#     downloader = MediaIoBaseDownload(fh, request)
#     done = False
#     while done is False:
#         status, done = downloader.next_chunk()

#         print("Download %d%%.", int(status.progress()*100))

if __name__ == "__main__":
    credentials = get_cred_access(credentials, client_secret_file_path, credentials_file_path)
    # get_all_files(drive)
    # print(search_file('NYPD_Complaint_Data_Historic.csv'))
    print(read_csv_file('NYPD_Complaint_Data_Historic.csv'))