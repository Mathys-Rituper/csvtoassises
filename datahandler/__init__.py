import pandas

from models.accomodation import Accomodation
from models.participant import Participant
from models.stay import Stay


class DataHandler:
    def __init__(self):
        """
        Initialize the data handler constants and lists.
        """

        self.PARTICIPANTS_FILE = "./data/participants.csv"
        self.HOSTS_FILE = "./data/hosts.csv"
        self.PAIRING_FILE = "./data/pairing.csv"

        self.PARTICIPANT_ID = "#"
        self.PARTICIPANT_NAME = "pseudo"
        self.PARTICIPANT_LOCALGROUP = "GL"
        self.PARTICIPANT_PRONOUNS = "pronoms"
        self.PARTICIPANT_PHONE = "tel"
        self.PARTICIPANT_EMAIL = "mail"

        self.ACCOMODATION_ID = "id"
        self.ACCOMODATION_HOSTNAME = "name"
        self.ACCOMODATION_HOSTEMAIL = "mail"
        self.ACCOMODATION_HOSTPHONE = "phone"
        self.ACCOMODATION_ADDRESS = "adresse"

        self.STAY_PARTICIPANT_ID = "id_participant"
        self.STAY_ACCOMODATION_ID = "id_logeureuse"
        self.STAY_START = "jour_arrivee"
        self.STAY_END = "jour_depart"
        self.STAY_BED_TYPE = "type_couchage"

        self.participants = []
        self.accomodations = []

    def load_paticipants(self):
        """
        Load the participants from the data file set in the class constants.
        :return: None
        """
        print("Accessing data file...")
        data = pandas.read_csv(self.PARTICIPANTS_FILE).to_dict(orient='records')

        print("Creating participant objects...")
        for record in data:
            self.participants.append(
                Participant(record[self.PARTICIPANT_ID], record[self.PARTICIPANT_NAME], record[self.PARTICIPANT_LOCALGROUP],
                            record[self.PARTICIPANT_PRONOUNS], record[self.PARTICIPANT_EMAIL], record[self.PARTICIPANT_PHONE]))

        print("Participant objects created.")

    def load_accomodations(self):
        """
        Load the accomodations from the data file set in the class constants.
        :return: None
        """
        print("Accessing data file...")
        data = pandas.read_csv(self.HOSTS_FILE).to_dict(orient='records')

        print("Creating accomodation objects...")
        for record in data:
            self.accomodations.append(
                Accomodation(record[self.ACCOMODATION_ID], record[self.ACCOMODATION_HOSTNAME], record[self.ACCOMODATION_HOSTEMAIL],
                             record[self.ACCOMODATION_HOSTPHONE], record[self.ACCOMODATION_ADDRESS]))

    def get_participant_from_id(self, id):
        """
        Get a participant from the list of participants.
        :param id: id of the participant
        :return: participant object with given id
        """
        for participant in self.participants:
            if participant.id == id:
                return participant
        raise ValueError(f"Participant with given id {id} was not found in the list")

    def get_accomodation_from_id(self, id):
        """
        Get an accomodation from the list of accomodations.
        :param id: id of the accomodation
        :return: accomodation object with given id
        """
        for accomodation in self.accomodations:
            if accomodation.id == id:
                return accomodation
        raise ValueError(f"Accomodation with given id {id} was not found in the list")

    def add_stay(self, participant_id, accomodation_id, start, end, bed_type):
        """
        Create a stay and add it to the participant and the accomodation.
        :param participant_id:
        :param accomodation_id:
        :param start:
        :param end:
        :param bed_type:
        :return: Stay object
        """
        participant = self.get_participant_from_id(participant_id)
        accomodation = self.get_accomodation_from_id(accomodation_id)
        stay = Stay(participant, accomodation, start, end, bed_type)
        participant.add_stay(stay)
        accomodation.add_stay(stay)
        return stay

    def load_stays(self):
        """
        Load the stays from the data file set in the class constants.
        :return: None
        """
        print("Accessing data file...")
        data = pandas.read_csv(self.PAIRING_FILE).to_dict(orient='records')

        print("Creating stay objects...")
        for record in data:
            self.add_stay(record[self.STAY_PARTICIPANT_ID], record[self.STAY_ACCOMODATION_ID], record[self.STAY_START], record[self.STAY_END], record[self.STAY_BED_TYPE])

    def get_participants(self):
        """
        Get the list of participants.
        :return: list of participants
        """
        return self.participants

    def get_accomodations(self):
        """
        Get the list of accomodations.
        :return: list of accomodations
        """
        return self.accomodations
