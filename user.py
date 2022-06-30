def login(database, username, password):

    if username in database.keys() and password == database[username]:
        print("Welcome", username)
        return username

    if username in database and password != database[username]:
        print("Inccorrect password for", username)
        return ""

    else:
        print(username, "not found in database. Please register.")
        return ""


def register(database, username):
    if username in database.keys():
        print("Username already registered")
        return ""
    else:
        print(username, "has been registered")
        return username
