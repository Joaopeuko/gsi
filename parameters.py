import os

import yaml
from dotenv import load_dotenv
from yaml.loader import SafeLoader


load_dotenv()

# Open the file and load the file
with open('config.yaml') as file:
    parameters = yaml.load(file, Loader=SafeLoader)


parameters['GITHUB_TOKEN'] = os.getenv('GITHUB_TOKEN')