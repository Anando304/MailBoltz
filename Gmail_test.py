'''
Program: GMail API tests
Author: Anando Zaman
Description: Experimenting with Gmail API for email extraction/modification
'''

from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import requests
import json

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly',
          'https://www.googleapis.com/auth/gmail.labels']

def main():

    '****Authentication flow****'
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

    service = build('gmail', 'v1', credentials=creds)

    '****Using the API****'
    # Call the Gmail API
    # Fetch all Gmail labels for the account that was authorized.
    # The data is saved to the results variable
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])
    print(labels)
    # setup dict object
    Label = MakeLabel("TESTING")
    # Create label on Gmail
    LabelCreated = CreateLabel(service,'me',Label)

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])

#Create and return Label object(JSON).
def MakeLabel(label_name, mlv='show', llv='labelShow'):

  label = {'messageListVisibility': mlv,
           'name': label_name,
           'labelListVisibility': llv}
  return label


def CreateLabel(service, user_id, label_object):
  """Creates a new label within user's mailbox, also prints Label ID.
  """
  try:
    # Using the Google API for request
    label = service.users().labels().create(userId=user_id,body=label_object).execute()
    print(label)
    return label
  except Exception as e:
    print(f"Error occured: {e}")


def DeleteLabel(service, user_id, label_id):
  """Creates a new label within user's mailbox, also prints Label ID.
  """
  try:
    # Using the Google API for request
    service.users().labels().delete(userId=user_id, id=label_id).execute()
  except Exception as e:
    print(f"Error occured: {e}")





if __name__ == '__main__':
    main()