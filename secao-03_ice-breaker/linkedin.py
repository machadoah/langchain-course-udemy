import os

import requests
from dotenv import load_dotenv


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """scrape information from linkedin profiles"""

    if mock:
        linkedin_profile_url = os.getenv('SCRAPIN_GIST')
        response = requests.get(linkedin_profile_url, timeout=20)

    else:
        params = {
            'apikey': os.getenv('SCRAPIN_API_KEY'),
            'linkedInUrl': linkedin_profile_url,
        }

        response = requests.get(
            os.getenv('SCRAPIN_API_ENDPOINT'), params=params, timeout=20
        )

    return response.json().get('person')


if __name__ == '__main__':
    load_dotenv()

    print(
        scrape_linkedin_profile(
            linkedin_profile_url='https://linkedin.com/in/machadoah/',
            mock=True,
        )
    )
