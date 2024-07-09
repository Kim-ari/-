from dotenv import load_dotenv
import os
import json
import requests
from pprint import pprint
from urllib import request

load_dotenv()

Access_Token = os.getenv('Access_Token')

# url = f'https://openapi.band.us/v2.1/bands?access_token={Access_Token}'
# req = request.Request(url)
# res = request.urlopen(req)
# decoded = res.read().decode("utf8")
# json_dict = json.loads(decoded)

# print(json_dict)
# #{'result_code': 1, ... 'band_key': 'AAA_8_wzQg67qwzwke2SA0P8'}]}}

def Bend(url, parameters):
    resp = requests.post(url, parameters)
    json.loads(resp.text)

Access_Token = os.getenv('Bend_Access_Token')
Band_key = os.environ.get('Band_key')
Content = "https://band.us/band/95471774/post/11"

url = "https://openapi.band.us/v2.2/band/post/create"
parameters = {"access_token" : Access_Token, "band_key" : Band_key, "content" : Content, "do_push" : True}

Bend(url, parameters)