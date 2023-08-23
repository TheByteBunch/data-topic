def add_channel(channel_name, subscribers, date):
    converted_date = date.date()
    return f"INSERT INTO channels (name, subscribers, dates) VALUES ('{channel_name}', Array[{subscribers}], Array[Date('{converted_date}')])"

def select_all():
    return f"SELECT * FROM channels"

def find_channel(user_input):
    return f"SELECT * FROM channels WHERE name = '{user_input}'"

def find_subscribers(user_input):
    return f"SELECT subscribers FROM channels WHERE name = '{user_input}'"

def delete_channel(user_input):
    return  f"DELETE FROM channels WHERE name = '{user_input}'"
    