import pdb
import requests
import os

URL_TO_MONITOR = "https://hokumrockfarm.com" #change this to the URL you want to monitor
BLUEBERRIES_UNCERTAIN_PHRASE = "We should know soon&nbsp;if we will be opening to the public this summer."


def blueberries_uncertain(): 
    """Returns true if we're not sure whether blueberries will be open."""
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Pragma': 'no-cache', 'Cache-Control': 'no-cache'}
    response = requests.get(URL_TO_MONITOR, headers=headers)
    if BLUEBERRIES_UNCERTAIN_PHRASE in response.text:
        return True
    return False

if __name__ == "__main__":
    if blueberries_uncertain():
        print("The blueberries are still uncertain.")
    else:
        print("The blueberries have decided!")