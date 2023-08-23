import traceback

def handle_errors(e):
    if e == "PSQL":
        print("> PSQL ERROR!")
    elif e == "YOUTUBE":
        print("> YOUTUBE ERROR!")
    else:
        print("> ERROR!")

    traceback.print_exc(e)
    