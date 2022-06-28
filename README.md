# csvtoassises

This project consists in a set of tools intended to be used in situations of event organization where data manipulation, contact with participants, volunteer hosts and other logistical tasks need to be automated.

A CSV data file is used as a basis for participant information.

## Modules :

- Model classes to represent common entities used in event management : participants, accomodations,...
- A data handler to turn CSV data into the said model classes
- Automated Protonmail email sender : based on https://github.com/nichcuta/Proton-Mail with modularity improvements 
- Automated SMTP email sender
- Automatic badge generator

## Python dependencies and other requirements :

### Pip version must be 3.10.0 or higher

### Modules :

Install the necessary modules using :
```sh
pip3 install -r requirements.txt
```
### Useful models :
- Participant : used to represent the information about a participant : contact information, name, ... and their places of accomodation
- Accomodation : used to represent the information about a participant's accomodation : contact information, name, ... and who will be staying there
- Stay : a stay is a stay of a participant in a host's accomodation, with a start, an end and a type of bed

### DataHandler :
A class to help load and manipulate data from CSV to the models given above.
Set the constants in the `__init__` function to match your csv data.

### Other requirements :
Obviously a Proton Mail Account is required if you intend on using the protonmail module.

## Badge generator
In current code, the template must be placed in the same repository as the script, named "empty_badge.png". Badge sizes and PDF export layouts are encoded for 90x57mm templates, but it can easily be changed in the core functions of badges.py.

You may need to create an "output" repository at the root of the project to store the results produced by the generator.

## Generic SMTP Mailer

Your SMTP host server, port, username and password should be set in the .env file, as such
```
EMAIL_ADDRESS =your_email
EMAIL_PASSWORD =your_password
EMAIL_HOST =your_smtp_host
EMAIL_PORT =your_server_port
```

## ProtonMail Mailer

Protonmail credentials should be located in credentials.json in the same folder as the script and follow the following structure :
 ```
{
  "email": "youremail@provider.com",
  "password": "yourpassword"
}
```

## Contributing

Contributions are welcome. Main axis of improvement to be made is in user friendliness to adapt the program to other data schemes