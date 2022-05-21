import json 
import pandas as pd
from io import StringIO

import sys
sys.path.append('../project_ny_crime')

from g_drive import search_file

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive 

# f = open('/home/ra-terminal/api_keys/pydrive/client_secrets.json')
# client_secrets_file = json.load(f)
# print(client_secrets_file)

gauth = GoogleAuth()
# gauth.CommandLineAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

# file1 = drive.CreateFile({'title': 'Helloooooo.txt'}) #CREATE GOOGLEDRIVE
# file1.SetContentString('HELLOOOOOUHWUHDAOFAIEFEHBEBFSWF')
# file1.Upload()

def get_file(filename):
    file_metadata = search_file(filename)
    # file_id = file_metadata['id']
    # file_name = file_metadata['name']
    # mimeType = file_metadata['mimeType']
    target_file = drive.CreateFile({'id':file_metadata['id']})
    print("Target file is: -------------->>>", target_file)
    target_download = target_file.GetContentString(file_metadata['name'])
    return target_download

def read_in_pandas(filename):
    return pd.read_csv(get_file(filename), encoding='utf8')



# df = read_in_pandas('NYPD_Complaint_Data_Historic.csv')
# df2 = pd.DataFrame({"a":[1,2,3,4],
#                     "b":[4,5,6,7]})
# # df3 = read_in_pandas('NYPD_Complaint_Data_Historic.csv')

if __name__ == "__main__":
    df = read_in_pandas('NYPD_Complaint_Data_Historic.csv')
    df_sub = df.head(50)
    print(df)
    print('complete run')
    pass