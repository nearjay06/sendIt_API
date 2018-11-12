[![Build Status](https://travis-ci.org/nearjay06/sendIt_API.svg?branch=master)](https://travis-ci.org/nearjay06/sendIt_API)








PROJECT TITLE: SENDIT PROJECT - CHALLENGE 2

SendIT is a courier service api.


GETTING STARTED:

To start the project, requirement is a github repository.

PREREQUISITES
- A text editor such as VS Code
- Web browser such as Google Chrome, Opera Mini
- Create a virtual environment in VS Code terminal

FEATURES

-Users can create a parcel delivery order
-Users can get all parcel delivery orders
-Users can get a specific parcel delivery order
-Users can cancel a parcel delivery order

LANGUAGES
-Python

INSTALLATIONS
-Install Flask i.e "pip install Flask"
-Install pytest i.e "pip install pytest"
-Install coveralls i.e "pip install coveralls"
-Install coverage i.e "pip install coverage"
-Install gunicorn i.e "pip install gunicorn"

ENDPOINTS

- GET /parcels to fetch all parcel delivery orders
- GET /parcels/<parcel_id>	 to fetch a specific parcel delivery orde
- GET /users/<user_id>/parcels	Fetch all parcel delivery orders by a specific user
- PUT /parcels/<parcel_id>/cancel	Cancel the specific parcel delivery order
- POST /parcels	Create a parcel delivery order


RUNNING TESTS
- Run the server by typing "run.py"
- Run tests for the api by typing the command  "pip -m unittest"
- Run tests for the api by typing  "pytest" in the virtual environment

DEPLOY the SENDIT api:

-Use TravisCI for Continuous Integration in repository (with ReadMe badge).
-Use coveralls for the test coverage reporting with badge in the ReadMe.
-Obtain CI badges from Code Climate and Coveralls and add to ReadMe.
-Host the app on Heroku



PROJECT OWNER

- Okecho Joan

ACKNOWLEDGEMENTS

- Andela