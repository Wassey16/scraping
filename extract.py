import requests
from bs4 import BeautifulSoup
import json

#headers used so webpage dosent detect scraping
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

def scrapper_json():
    url = "https://gbfs.citibikenyc.com/gbfs/en/station_information.json"
    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')

    #get the whole dump of the webpage in pretified form
    data = soup.prettify()
    #removing back slashes due to wraping
    json_string = json.dumps(data)
    mod_json_strings = json.loads(json_string)
    #writing the formated data in a file
    f = open("data.json", "w")
    f.write(mod_json_strings)
    f.close()

if __name__ == '__main__':
    scrapper_json()




