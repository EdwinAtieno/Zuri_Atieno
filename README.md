# [Django: Getting Started]

##Create a new Python virtual environment.

 

` Initialize it, and install Django in it.`

 

*Create a new Django project. Use your ZuriBoard username as the name of the project.*

Push your project to a new Public GitHub repository and submit the URL.


To run the local development server with your settings/local.py settings file:

`python manage.py runserver --settings=config.settings.local`



_Acceptance Criteria:
successful registration of user
generation of pin
validation of inputted data_

Tools & Libraries:
Celery - to run tasks asynchronously
Redis - To store queue messages
Flower - web-based monitoring tool for Celery
Faker - for faking/ mocking data during testing

