
# Setup

Copy .env.default to .env

Install [Poetry](https://python-poetry.org/).


# Email

Sign up for a mailgun account, create an api key. Should just be able to use a sandbox if you don't have your own domain. Grab credentials and plug them into the .env

# SMS

Sign up for Twilio and verify your phone number, grab credentials, and plug them into the .env


# Usage 

`poetry install`

`poetry run python run.py`

Set up as CRON job for repeated use.