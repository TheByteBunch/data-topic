from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("YOUTUBE_API_KEY")

youtube = build('youtube', 'v3', developerKey=API_KEY)

def request_channel(channelName):
    requests = youtube.channels().list(
        part='statistics',
        forUsername=channelName
    )
    return requests.execute()