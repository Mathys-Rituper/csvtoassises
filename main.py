import json
import pandas as pd
from mail import *
from badges import *


def create_badges():
    filename_list_to_pdf(generate_files_from_infolist(records),"badges.pdf")

def send_emails():
    with open('credentials.json') as json_file:
        creds = json.load(json_file)
    email = creds['email']
    password = creds['password']
    # driver, display = connect_driver(email,password)

    driver = connect_driver(email, password)  # connects to protonmail inbox

    # send_email("foo@gmail.com","Test email","test",driver,display)
    send_email("me@email.com", "Test email", "test", driver)
    sleep(1)
    send_email("recipient@foo.com", "Test email", "test", driver)

    # kill_driver(driver,display)
    kill_driver(driver)

if __name__ == "__main__":

    try:
        action = int(input("What do you want to do ? Type 1 for badges, 2 for emails"))
        if action == 1:
            data = pd.read_csv('data.csv')
            records = data.to_dict(orient='records')
            create_badges()
        elif action==2:
            data = pd.read_csv('data.csv')
            records = data.to_dict(orient='records')
            send_emails()
        else:
            print("Incorrect input, please try again")
    except ValueError as e:
        print(f"Erreur de valeur saisie ! ", e)


