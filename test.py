import pandas as pd
from spark_dir.spark_tables import crime_file_id
import requests
from g_drive import *
import io
# url= f'https://drive.google.com/file/d/{crime_file_id}/view?usp=sharing'
# dwn_url='https://drive.google.com/uc?id=' + crime_file_id

from io import StringIO

# file_id = "###"  # Please set the file ID of the CSV file.

# access_token = get_gtoken()
# url = "https://www.googleapis.com/drive/v3/files/" + crime_file_id + "?alt=media"
# res = requests.get(url, headers={"Authorization": "Bearer " + access_token})
# print(res.text)
# df = pd.read_csv(io.StringIO(res.text))

request = drive_service.files().get_media(fileId=crime_file_id)
fh = io.BytesIO()
downloader = MediaIoBaseDownload(fh, request)
done = False
while done is False:
    status, done = downloader.next_chunk()

    print("Download %d%%.", int(status.progress()*100))


