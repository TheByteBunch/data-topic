import os
import psycopg2
import local_youtube_api
import local_psql
import datetime

# random change
# def extract_channel_info(channel_name, channel_data):
#     subscriber_count = channel_data['items'][0]['statistics']['subscriberCount']
#     view_count = channel_data['items'][0]['statistics']['viewCount']
#     video_count = channel_data['items'][0]['statistics']['videoCount']
#     return channel_name, subscriber_count, view_count, video_count

# result = local_youtube_api.request_channel(print_result)
# data = extract_channel_info(print_result, result)
# channel_name = str(data[0])
# subscriber_count = data[1]
# view_count = data[2]
# video_count = data[3]
# message = f"INSERT INTO channels (name, subscribers, views, video_count) VALUES ('{channel_name}', {subscriber_count}, {view_count}, {video_count})"
# print(message)

def view_channels_query():
    print("viewing query")
    query = f"SELECT * FROM channels"
    results = local_psql.query_sql_fetchall(query)
    for channel in results:
        print(channel)

def add_channel_query(user_input):
    # check if channel already exists
    check_query = f"SELECT * FROM channels WHERE name = '{user_input}'"
    result = local_psql.query_sql_fetchall(check_query)
    
    if result:
        print("Channel already exists")
    else:
        (channel_name, subscribers, date) = local_youtube_api.create_add_channel_query_params(user_input)
        converted_date = date.date()
        query = f"INSERT INTO channels (name, subscribers, dates) VALUES ('{channel_name}', Array[{subscribers}], Array[Date('{converted_date}')])"
        result = local_psql.query_sql(query)
################## ADD a call to the DB to check it was added succesfully

def delete_channel_query(user_input):
    check_query = f"SELECT * FROM channels WHERE name = '{user_input}'"
    result = local_psql.query_sql_fetchall(check_query)
    if not result :
        print("Channel does not exist!")

    delete_query = f"DELETE FROM channels WHERE name = '{user_input}'"
    local_psql.query_sql(delete_query)

def update_channel():
    pass

def start():
    os.system("clear")
    user_input = 0
    while user_input != 1 and user_input != 2 and user_input != 3 and user_input != 4:
        print('Please select one of the options:')
        print('(1) View Channels')
        print('(2) Add Channel')
        print('(3) Delete Channel')
        print('(4) Exit')
        user_input = int(input())

    if user_input == 1:
        view_channels()
    elif user_input == 2:
        add_channel()
    elif user_input == 3:
        delete_channel()
    elif user_input == 4:
        exit()

def view_channels():
    view_channels_query()

def add_channel():
    print('Please enter the channel name to add it')
    user_input = str(input())
    add_channel_query(user_input)

def delete_channel():
    print('Please enter the channel name to delete it')
    user_input = str(input())
    delete_channel_query(user_input)

def exit():
    pass

start()
# (1) VIEW CHANNELS
# (2) ADD CHANNEL FIX THE TIMESTAMP
# (4) EXIT


# TERMINAL PROGRAM
# TERMINAL PROGRAM
# TERMINAL PROGRAM
# update player_scores set round_scores = array_append(round_scores, 100);


# TOMMOROW:
# FINISH WRITING FOR ALL THE OTHER 4 COMMANDS
# WORRY ABOUT GRAPH FROM VIEW CHANNELS LATER

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