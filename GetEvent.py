from _future_ import print_function
from dateGuess import get_date

import datetime
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def get_events(txt):
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    try:
        service = build('calendar', 'v3', credentials=creds)
        # Call the Calendar API
        date = str(get_date(txt)) + "T12:00:00+04:00"
        if date[0] == 'N':
            date = datetime.datetime.utcnow().isoformat("T") + "+04:00" # 'Z' indicates UTC time
	print(date)
        print('Getting the upcoming 3 events')
        events_result = service.events().list(calendarId='primary', timeMin=date,
                                              maxResults=3, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])
        if not events:
            print('No upcoming events found.')
            return "No upcoming events found."
	events_dict = {}
        # Prints the start and name of the next 3 events
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
	    start = datetime.datetime.strptime(start[:19], '%Y-%m-%dT%H:%M:%S')
	    start = start.strftime("%A %I:%M %p")
	    events_dict[event['summary']] = " on " + str(start)
            print(start, event['summary'])

        return "You have: ", events_dict
    except HttpError as error:
        print('An error occurred: %s' % error)

