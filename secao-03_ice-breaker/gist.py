import os
from pprint import pprint

import requests
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()

    pprint(requests.get(os.getenv('SCRAPIN_GIST')))
