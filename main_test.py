import os

import pandas
import badges
from dotenv import load_dotenv

from models.participant import Participant
from models.stay import Stay
from models.accomodation import Accomodation
import smtpmailer
import datahandler

if __name__ == "__main__":

    data = datahandler.DataHandler()
    data.load_paticipants()
    data.load_accomodations()
    data.load_stays()

    quit = 1
    while quit:
        print("What do you want to do ? Type 1 for badges, 2 for emails, any other number to quit.")
        try:
            action = int(input())
            match action:
                case 1:
                    print("Creating participant badges...")
                    badges.filename_list_to_pdf(badges.generate_files_from_infolist(data.participants), "badges.pdf")
                    print("Participant badges created.")
                case 2:

                    load_dotenv()
                    #real variables
                    #mail_server = os.getenv('EMAIL_HOST')
                    #mail_port = os.getenv('EMAIL_PORT')
                    #mail_address = os.getenv('EMAIL_ADDRESS')
                    #password = os.getenv('EMAIL_PASSWORD')

                    #using a python test server
                    mail_server = "localhost"
                    mail_port = "1025"
                    mail_address="toto"
                    password="toto"

                    print("initiating email client...")
                    if mail_server == "localhost":
                        print("USING LOCAL SERVER FOR TESTING PURPOSES")
                    # get server, credentials and port from environment variables
                    email_client = smtpmailer.Mailer(mail_server, mail_port, mail_address, password)
                    print("email client initiated.")

                    # REFACTOR ME
                    # --- START OF THE SECTION TO BE REFACTORED ---
                    print("Sending to participants...")
                    for participant in data.participants:
                        email_content = f"Bonjour {participant.name},\n\n {participant.stays_to_string()}\nAu revoir"
                        email_client.send_email(participant.email, "Ta venue à ÉVÉNEMENT", email_content)
                    print("Emails sent to participants.")

                    print("Sending to accomodations...")
                    for accomodation in data.accomodations:
                        email_content = f"Bonjour {accomodation.name},\n\n {accomodation.stays_to_string()}\nAu revoir"
                        email_client.send_email(accomodation.email, "Accueil de participant.e.s de ÉVÉNEMENT à votre domicile", email_content)

                    print("Emails sent to accomodations.")

                    # --- END OF THE SECTION TO BE REFACTORED ---
                case _:
                    quit = 0
        except ValueError as e:
            print("Your input is not a number !")

    print("Bye bye !")
    print("exiting...")
