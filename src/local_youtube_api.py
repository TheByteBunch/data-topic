from googleapiclient.discovery import build
from dotenv import load_dotenv
import os
import datetime

load_dotenv()
API_KEY = os.getenv("YOUTUBE_API_KEY")

youtube = build('youtube', 'v3', developerKey=API_KEY)

def request_channel(channelName):
    requests = youtube.channels().list(
        part='statistics',
        forUsername=channelName
    )
    return requests.execute()

def get_subscriber_count(channelName):
    request = request_channel(channelName)
    subscriber_count = request['items'][0]['statistics']['subscriberCount']
    return subscriber_count

def create_add_channel_query_params(channelName):
    subscribers = get_subscriber_count(channelName)
    return channelName, subscribers, datetime.datetime.now()