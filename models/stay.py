import datetime
class Stay:
    def __init__(self, participant, accomodation,start,end,sleeping_type):
        """
        Initialize a stay.
        :param participant: the participant
        :param accomodation: the accomodation
        :param start: the start date of the stay
        :param end: the end date of the stay
        :param sleeping_type: the sleeping type of the stay
        """
        self.participant = participant
        self.accomodation = accomodation
        self.start = start
        self.end = end
        self.sleeping_type = sleeping_type

    def str_to_participant(self):
        """
        Return a string describing the stay to the participant.
        :return: string: the description of the stay
        """
        return f"- Du {self.start} au {self.end} : chez {self.accomodation.host_name} ({self.accomodation.host_phone}/{self.accomodation.host_email}), au {self.accomodation.address}, type de couchage : {self.sleeping_type}"

    def str_to_host(self):
        """
        Return a string describing the stay to the host.
        :return: string: the description of the stay
        """
        return f"- {self.participant.name} ({self.participant.email} / {self.participant.phone}) du groupe local de {self.participant.localgroup}, du {self.start} au {self.end}, type de couchage : {self.sleeping_type}"