# csv2assises

This project consists in a set of tools intended to be used in situation of event organization where data manipulation, contact with participants and other logistical tasks need to be automated.

A CSV data file is used as a basis for participant information.

## Modules :

- CSV reader and processor : anonymization, auto-cleanup, projections, ... to be used as data source for other modules (TODO)
- Automated Protonmail email sender : based on https://github.com/nichcuta/Proton-Mail with scalability improvements 
- Automatic badge generator

## Python dependencies and other requirements :

### Pip modules :
- selenium
- pyvirtualdisplay (for non-GUI use)
- pillow
- pandas

### Other requirements :
Obviously a Proton Mail Account is also required.

You may need to run the following command to install dependencies for pyvirtualdisplay to run properly (required for mail component), although please note the solution was only tested on Pop!_OS 20.10 :  

```apt update && apt install xvfb firefox-geckodriver && pip3 install pyvirtualdisplay && pip install pyvirtualdisplay```

PS: If script is used in a non GUI environment, uncomment the commented lines for it to work properly.

## Badge generator
In current code, the template must be placed in the same repository as the script, named "empty_badge.png". Badge sizes and PDF export layouts are encoded for 90x57mm templates, but it can easily be changed in the core functions of badges.py.

You may need to create an "output" repository at the root of the project to store the results produced by the generator.

## Mailer

Protonmail credentials should be located in credentials.json in the same folder as the script and follow the following structure :
 ```
{
  "email": "youremail@provider.com",
  "password": "yourpassword"
}
```

## Contributing

Contributions are welcome. Main axis of improvement to be made is in user friendliness to adapt the program to other data schemes