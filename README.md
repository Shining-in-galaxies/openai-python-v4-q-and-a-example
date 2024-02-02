# OpenAI API v4 Quickstart - Python Crawler, Q&A Example App

## Introduction

An AI consultation service built with Flask and OpenAI v4 API, designed to answer site-related questions by crawling and analyzing the target website, openai.com, excluding unrelated queries.

## Features

- Web crawling for data collection
- Training text generation with OpenAI embeddings
- Q&A model for answering site-related questions

## Tech Stack

- Python
- Flask
- OpenAI API v4

## Environment

Developed and tested for Linux.

## Installation and Setup

1. Check Python Version
   Ensure you have Python 3 installed by running:
   `python3 --version`
   If Python is not installed, follow the instructions here: [Install Python on Ubuntu](https://www.makeuseof.com/install-python-ubuntu/).

2. Update your package list and install pip:
   `sudo apt update`
   `sudo apt install python3-pip`

3. Install virtual environment tools:
   `sudo apt install virtualenv virtualenvwrapper`

4. Configure the virtual environment:

   - Open file:
     `nano ~/.bashrc`
   - Add the following lines to the end of the file:
     `WORKON_HOME=$HOME/.virtualenvs`
     `VIRTUAL_ENVWRAPPER_PYTHON=/usr/bin/python3`
     `source /usr/share/virtualenvwrapper/virtualenvwrapper.sh`

5. Create a new virtual environment:
   `mkvirtualenv example`

6. Work on virtual environment:
   `workon example`

7. Clone this repository.

8. Navigate into the project directory:
   `cd openai-python-v4-q-and-a-example`

9. Install the requirements:
   `pip install -r requirements.txt`

10. [OpenAI Migration](https://github.com/openai/openai-python/discussions/742):
    `openai migrate`

11. [Get your API key](https://beta.openai.com/account/api-keys)

12. Add OpenAI API Key to the Virtual Environment`s Environment Variables

    - Open or create an .env file within your virtual environment:
      `nano .env`
    - In the .env file, enter the following line, replacing your_api_key_here with your actual OpenAI API key:
      `OPENAI_API_KEY=your_api_key_here`
    - Activate the environment variables in your current session:
      `source .env`
    - Test if the OpenAI API Key was successfully added by printing it:
      `echo $OPENAI_API_KEY`
      If the command prints your API key, it has been successfully added to the environment variables.

13. Running the Application

    - Run the crawler program:
      `python3 crawler.py`
      This will generate a `txt` folder in your directory.

    - Run the embeddings program:
      `python3 embeddings.py`
      This will generate a `processed` folder in your directory.

    - Run Flask:
      `python3 app.py`
      At this point, you can access the application by going to [http://localhost:5000](http://localhost:5000).

    For subsequent launches, you only need to execute:
    `python3 app.py`
