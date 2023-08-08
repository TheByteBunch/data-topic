
import psycopg2
import local_youtube_api
import local_psql

def extract_channel_info(channel_data):
    subscriber_count = channel_data['items'][0]['statistics']['subscriberCount']
    view_count = channel_data['items'][0]['statistics']['viewCount']
    video_count = channel_data['items'][0]['statistics']['videoCount']
    return subscriber_count, view_count, video_count

channels = ['Google','Schafer5']
for channel in channels:
    result = local_youtube_api.request_channel(channel)
    data = extract_channel_info(result)
    print(data)
    # psql.query_sql("query here")



#channel_id , channel_name, subscriber_count, view_count  ### sql table names


#INSERT INTO youtube_channels VALUES (#)