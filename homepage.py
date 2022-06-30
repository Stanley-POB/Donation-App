from xml.dom.xmlbuilder import DOMImplementationLS


def show_homepage():
    print("\n             ===  DonateMe Homepage  ===           \n")
    print("--------------------------------------------------")
    print("|    1.   Login         | 2.   Register           |")
    print("--------------------------------------------------")
    print("|    3.   Donate        | 4.   Show Donations     |")
    print("--------------------------------------------------")
    print("|                   5.   Exit                     |")
    print("--------------------------------------------------")


def donate(username):
    global donation_amt
    while True:
        donation_amt = float(input("Enter an amount to donate: $"))
        if donation_amt == 0 or donation_amt < 0:
            print("Retype amount")
        else:
            donation_string = f"{username} donated ${donation_amt}"
            print(donation_string)
            print("Thank you for your donation")
            return donation_string


def show_donations(donations):
    print("\n--- All Donations ---\n")
    if len(donations) == 0:
        print("Currently there are no donations")
    else:
        for donation_amt in donations:
            print(donation_amt)
