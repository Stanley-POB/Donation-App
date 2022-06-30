from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register

database = {"admin": "password123"}
donations = []
total_donations = 0.0
authorized_user = ""

while True:
    show_homepage()
    if authorized_user == "":
        print("\nYou must be logged in to donate.\n")
    else:
        print("\nYou are logged in as:", authorized_user, "\n")

    option = input("Choose an option: ")

    if option == "1":
        username = input("Username: ")
        password = input("Password: ")
        authorized_user = login(database, username, password)

    if option == "2":
        username = input("Username: ")
        password = input("Password: ")
        authorized_user = register(database, username)
        if authorized_user != "":
            database[username] = password

    if option == "3":
        if authorized_user == "":
            print("You are not logged in")
        else:
            donation_string = donate(authorized_user)
            donations.append(donation_string)

    if option == "4":
        show_donations(donations)

    if option == "5":
        print("Thank you for visiting, goodbye", username)
        break
