
import psycopg2
import local_youtube_api
import local_psql
import input
def extract_channel_info(channel_name, channel_data):
    subscriber_count = channel_data['items'][0]['statistics']['subscriberCount']
    view_count = channel_data['items'][0]['statistics']['viewCount']
    video_count = channel_data['items'][0]['statistics']['videoCount']
    return channel_name, subscriber_count, view_count, video_count

print_result = input.get_input()
print(print_result)
result = local_youtube_api.request_channel(print_result)
data = extract_channel_info(print_result, result)
channel_name = str(data[0])
subscriber_count = data[1]
view_count = data[2]
video_count = data[3]
message = f"INSERT INTO channels (name, subscribers, views, video_count) VALUES ('{channel_name}', {subscriber_count}, {view_count}, {video_count})"
print(message)
local_psql.query_sql(message)


"INSERT INTO channels (name, subscribers, views, video_count) VALUES ( X, 2, 4, 6);"

# TERMINAL PROGRAM
# TERMINAL PROGRAM
# TERMINAL PROGRAM

# TOMMOROW:
# LOOK UP ARRAYS PSQL
# MY BRAIN IS FRIED IDK WHAT NEXT WE WILL FIGURE IT OUT TROMMOROW

#
# TO-DO-LIST:
# UPDATE THE DATABASE DAILY, FROM THE DAILY SUBSCRIBER COUNT
# CREATE A GRAPH FROM THE DATAPOINTS OF THE DATABASE
# LIMIT CHANNEL GRAPH VIEW LIMIT FOR USER

# USER:
# INPUT SOME CHANNELS
# GOES INTO DATABASE
# LEAVE FOR SOME DAYS
# SO YOU CAN LOOK AT GRAPH AND DO SOME STATISTICS