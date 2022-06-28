import json
import pandas as pd
from protonmail import *
from badges import *


def create_badges(data):
    filename_list_to_pdf(generate_files_from_infolist(data),"badges.pdf")

def send_emails():
    with open('credentials.json') as json_file:
        creds = json.load(json_file)
    email = creds['email']
    password = creds['password']
    # driver, display = connect_driver(email,password)

    driver = connect_driver(email, password)  # connects to protonmail inbox

    # kill_driver(driver,display)
    kill_driver(driver)

if __name__ == "__main__":

    try:
        action = int(input("What do you want to do ? Type 1 for badges, 2 for emails"))
        match action:
            case 1:
                data = pd.read_csv('data.csv')
                records = data.to_dict(orient='records')
                create_badges()
            case 2:
                data = pd.read_csv('data.csv')
                records = data.to_dict(orient='records')
                send_emails()
            case _:
                print("Incorrect input, please try again")
    except ValueError as e:
        print(f"Erreur de valeur saisie ! ", e)


