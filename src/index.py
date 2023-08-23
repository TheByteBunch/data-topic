import os
import time
import psycopg2
import datetime

import utils
import graph
import errors
import queries
import local_psql
import local_youtube_api

### FIND A WAY TO AUTOMATICALLY UPDATE CHANNEL STATS
def view_channels_query():
    try:
        results = local_psql.query_sql_fetchall(queries.select_all())
    except:
        print("Failed to connect to database...")
    utils.return_to_menu(start)

def plot_channel_query(user_input):
    try:
        result = local_psql.query_sql_fetchall(queries.find_subscribers(user_input))
        result = result[0][0]
        if result:
            graph.plot_channel_function(result)
        else:
            print("Channel doesn´t exists")
    except Exception as e:
        errors.handle_errors(e)

def add_channel_query(user_input):
    # check if channel already exists
    try:
        result = local_psql.query_sql_fetchall(queries.find_channel(user_input))
        if result:
            print("Channel already exists")
        else:
            (channel_name, subscribers, date) = local_youtube_api.create_add_channel_query_params(user_input)
            result = local_psql.query_sql(queries.add_channel(channel_name, subscribers, date))
    except Exception as e:
        errors.handle_errors(e)
    utils.return_to_menu(start)


def delete_channel_query(user_input):
    try: 
        result = local_psql.query_sql_fetchall(queries.find_channel(user_input))
        if not result :
            print("Channel does not exist!")
        local_psql.query_sql_fetchall(queries.delete_channel(user_input))
    except Exception as e:
        errors.handle_errors(e)
    utils.return_to_menu(start)


def update_channel():
    pass

def start():
    os.system("clear")
    print("start")
    user_input = 0
    while user_input != 1 and user_input != 2 and user_input != 3 and user_input != 4 and user_input != 5:
        print('Please select one of the options:')
        print('(1) View Channels')
        print('(2) Plot Channel')
        print('(3) Add Channel')
        print('(4) Delete Channel')
        print('(5) Exit')
        user_input = int(input())

    os.system("clear")
    if user_input == 1:
        view_channels()
    elif user_input == 2:
        plot_channel()        
    elif user_input == 3:
        add_channel()
    elif user_input == 4:
        delete_channel()
    elif user_input == 5:
        exit()

def view_channels():
    view_channels_query()

def plot_channel():
    print('Please enter the channel to plot it')
    user_input = str(input())
    plot_channel_query(user_input)

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

#
# TO-DO-LIST:
# UPDATE THE DATABASE DAILY, FROM THE DAILY SUBSCRIBER COUNT
# LIMIT CHANNEL GRAPH VIEW LIMIT FOR USER

# USER:
# INPUT SOME CHANNELS
# GOES INTO DATABASE
# LEAVE FOR SOME DAYS
# SO YOU CAN LOOK AT GRAPH AND DO SOME STATISTICS