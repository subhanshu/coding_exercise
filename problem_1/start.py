from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
import io


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive']


creds = None
# The file token.pickle stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

#declare google services
drive_service = build('drive', 'v3', credentials=creds)
sheets_service = build('sheets', 'v4', credentials=creds)

def download_file(file_id):
    if type(file_id) not in [str, unicode]:
        raise TypeError("Invalid File ID")
    result=False
    request = drive_service.files().export_media(fileId=file_id,
                                                mimeType='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    try:
        while done is False:
            status, done = downloader.next_chunk()
            print("Download %d%%.", int(status.progress() * 100))
    except:
        raise IOError("Unable to download files")
    try:
        with open('downloaded_excel.xlsx', 'wb') as f:
            f.write(fh.getvalue())
        result = True
        
    except:
        raise IOError("unable to write file to disk")
    
    return result


def upload_file(filename):
    file_metadata = {'name': filename, 'mimeType': 'application/vnd.google-apps.spreadsheet'}
    try:
        media = MediaFileUpload(filename)
        file = drive_service.files().create(body=file_metadata,
                                            media_body=media,
                                            fields='id').execute()
    except:
        raise IOError("Error uploading file")
    file_id = file.get('id')
    print('File ID:', file_id)
    return file_id




def main():
    file_id = upload_file('sample_excel.xlsx')
    download_file(file_id)


if __name__ == '__main__':
    main()
