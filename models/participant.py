class Participant:
    def __init__(self, id, name, localgroup, pronouns, email, phone):
        """
        Create a participant.
        :param id: the id of the participant
        :param name: the name of the participant.
        :param localgroup: the local group of the participant.
        :param pronouns: the pronouns of the participant.
        :param email: the email address of the participant.
        :param phone: the phone number of the participant.
        """
        self.id = id
        self.name = name
        self.localgroup = localgroup
        self.pronouns = pronouns
        self.email = email
        self.phone = phone
        self.stays = []

    def __str__(self):
        return f"{self.name} ({self.pronouns}) du groupe local de {self.localgroup} (adresse email : {self.email}, " \
               f"numéro de téléphone : {self.phone}) "

    def add_stay(self, stay):
        self.stays.append(stay)

    def stays_to_string(self):
        if len(self.stays) == 0:
            return "Tu as déclaré que tu te logeras par tes propres moyens lors de ton inscription, par conséquent aucun logement ne t'a été atrribué. Si cela est une erreur, merci de prendre contact avec nous au plus vite !"
        else:
            message = "Voici le(s) logement(s) qui t'a(ont) été attribué(s) pour ta venue :\n"
            for stay in self.stays:
                message = message + stay.str_to_participant() + '\n'
                message = message + "Les personnes suivantes seront logées là bas en même temps que vous :\n"
                for stay2 in stay.accomodation.stays:
                    if stay2.participant.id != self.id :
                        message = message + f"{stay2.participant.name} du groupe local de {stay2.participant.localgroup} \n"
            message += "Merci de contacter rapidement votre/vos logeur.euse(s) pour vous présenter et vous assurer que tout est ok de vôtre côté et du leur. En cas de problème, contacte-nous !" + '\n'
            return message