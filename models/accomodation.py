class Accomodation:
    def __init__(self, id, host_name, host_email, host_phone, address):
        """
        Initialize a place of accomodation.
        :param id: the id of the accomodation place
        :param host_name: the name of the host.
        :param host_email: the email address of the host.
        :param host_phone: the phone number of the host.
        :param address: the address of the place of accomodation.
        """
        self.id = id
        self.host_name = host_name
        self.host_email = host_email
        self.host_phone = host_phone
        self.address = address
        self.stays = []

    def add_stay(self, stay):
        """
        Add a stay to the accomodation.
        :param stay: the stay to be added
        :return: None
        """
        self.stays.append(stay)

    def stays_to_string(self):
        """
        Return a string with all the stays of the accomodation.
        :return:
        """
        if len(self.stays) == 0:
            return "Personne n'a été attribué à votre logement pout le moment. A moins que nous vous recontactions en " \
                   "cas de changement, nous vous remercions chaleureusement d'avoir proposé votre aide pour héberger " \
                   "nos militant.es, mais nous avons réussi à loger tout le monde sans nécessité de vous déranger ! " \
                   "Vous pouvez donc ignorer la suite de cet email. "
        else:
            message = "Les personnes suivantes ont été attribuées à votre logement :\n"
            for stay in self.stays:
                message = message + stay.str_to_host() + '\n'
                message += "Les participant.es en question devraient prendre contact avec vous très prochainement " \
                           "pour faire connaissance avec vous et s'assurer que tout est ok de leur côté et du vôtre, " \
                           "néanmoins n'hésitez pas à prendre l'initative de les contacter sans attendre si vous le " \
                           "souhaitez ! En cas de problème, merci de nous contacter rapidement pour que nous " \
                           "puissions trouver des solutions ensemble.\n"
            return message