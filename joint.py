import pandas as pd
from mail import *
import json
import time

#turns a raw data line into an intellegible paragraph for non-computer literate people to understand
def line_to_logeureuse_date(line):
    return f"""-    {line["pseudo"]} ({line["pronoms"].lower()}), groupe local de {line["groupe_local"]} : du {line["date_debut"]} au {line["date_fin"]}
    Type de couchage : {line["type_couchage"]}, numéro de téléphone : {line["tel"]}

"""

# turns a list of raw data lines into intellegible paragraphs for non-computer literate people to understand
def lines_to_logeureuse(lines):
    chars = ""
    for line in lines:
        if line["tel"][0] != "0":
            line["tel"] = "0" + line["tel"]
        chars += line_to_logeureuse_date(line)
    return chars


#Initiating mailer
with open('credentials.json') as json_file:
    creds = json.load(json_file)
email = creds['email']
password = creds['password']
#driver, display = connect_driver(email,password)

driver = connect_driver(email, password)  # connects to protonmail inbox

# send_email("foo@gmail.com","Test email","test",driver,display)

# Loading data from CSV
participants = pd.read_csv('assises_nationales_yfc_france_inscription_4.csv')
logeureuses = pd.read_csv('infos-logeureuses.csv')
jointure = pd.read_csv('repartition.csv').reset_index()

# 1st joint : participant data + association data
participants_jointure = pd.merge(participants, jointure, on=["email"], suffixes=["_participant", "_jointure"],
                                 how="left")

# 2nd joint : 1st joint + host data
participants_logeureuses = pd.merge(participants_jointure, logeureuses, on=["email_logeureuse"],
                                    suffixes=["", "_logeureuse"], how="left")

def send_email_logeureuses():
    # list of email adresses for hosts
    emails_logeureuses = participants_logeureuses['email_logeureuse'].unique()

    for email in emails_logeureuses:
        #exclude virtual hosts
        if type(email) == str and email != "salle1@mdp.fr" and email != "salle2@mdp.fr" and email != "salle3@mdp.fr" and email!="osmix@protonmail.com":

            # find participant data for each host
            logeureuse_rows = participants_logeureuses.loc[participants_logeureuses["email_logeureuse"] == email]
            rows = logeureuse_rows.to_dict(orient="records")

            # create email
            message = f"""message
    """
            print(f"====Email pour: {email} :=====")
            try :

                print(message)
                time.sleep(1)
            except Exception as e:
                status = (str(e), 'Error Origin: Email sender')
                print(status)
                exit(0)

    print("Fin des envois !")

def get_neighbours(email_participant,email_logeureuse,arrivee,depart):
    char="""Vous serez logé.e.x avec :
"""
    lines = participants_logeureuses.loc[(participants_logeureuses["email_logeureuse"] == email_logeureuse) & (participants_logeureuses["email"] != email_participant) & (participants_logeureuses["date_debut"]<=depart) & (participants_logeureuses["date_fin"] >=arrivee)].to_dict(orient='records')
    for line in lines:
        char += f"""{line["pseudo"]} ({line["pronoms"]}) du GL de {line["groupe_local"]}
"""
    return char

def line_to_participant(line):
    return f"""- Vous allez loger à / chez {line["nom_logeureuse"]} ({line["adresse"]}), : {line["classe"]}, du {line["date_debut"]} au {line["date_fin"]}
    Type de couchage : {line["type_couchage"]}, numéro de téléphone : {line["telephone_logeureuse"]}
{get_neighbours(line["email"],line["email_logeureuse"],line["date_debut"],line["date_fin"])}
"""

def lines_to_participant(lines):
    chars = ""
    if lines[0]["autonome_logement"] == "Non":
        for line in lines:
            if str(line["telephone_logeureuse"][0]) != "0":
                line["telephone_logeureuse"] = "0" + str(line["telephone_logeureuse"])
            chars += line_to_participant(line)
    else:
        chars = "Vous avez déclaré lors de votre inscription être autonome pour vous loger, aucun logement ne vous a donc été attribué. S'il s'agit d'une erreur, merci de nous contacter au plus vite !"
    return chars

def send_email_participants():
    emails_participants = participants_logeureuses['email'].unique()
    print(emails_participants)

    for email in emails_participants:
        if type(email) == str:
            print(f"==== Email pour {email} ====")
            participant_rows = participants_logeureuses.loc[participants_logeureuses["email"] == email]
            rows = participant_rows.to_dict(orient="records")

            message = f"""Messagee"""
            try :
                print(f"Envoi à {email}...")
                send_email(email,"Event France : logement et informations",message,driver)
                print(f"Envoi réussi à {email}")
            except Exception as e:
                status = (str(e), 'Error Origin: Email sender')
                print(status)
                exit(0)


send_email_participants()