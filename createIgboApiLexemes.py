import tfsl
import requests
import json
import urllib.parse
from differentiateDuplicateNonDuplicate import differentiateDuplicateAndNonDuplicateLexemes

api_key_token = "aaa1b71a-6c34-4fab-b024-059e3ed23739"
headers = { 'X-API-Key' : api_key_token}
headerSet = {'Accept': 'application/json'}
base_url = "https://igboapi.com/api/v1/"
# keywordQueryParam = input("Enter keyword querying words:")
request_url = base_url + "/words?keyword=i&range=%5B1%2C%2020%5D&examples=true"

lexemeWordClasses = {
    "ADJ": "Q34698",
    "ADV": "Q380057",
    "AV": "Q24905",
    "MV": "Q24905",
    "PV": "Q54557461",
    "CJN": "Q36484",
    "DEM": "Q282301",
    "NM": "Q1084",
    "NNC": "Q1084",
    "NNP": "Q147276",
    "PREP": "Q4833830",
    "PRN": "Q36224",
    "WH": "Q12021746",
    "INTJ": "Q83034",
    "QTF": "Q1909485",
}

response = requests.get(request_url, headers=headers)
my_response = response.json()
# my_response = ""

def createIgboApiLexemes(ApiResponse):
    for item in ApiResponse:
        if item['wordClass'] in lexemeWordClasses.keys():
            usageExample = item['examples'][0]
            usageExampleIgbo = usageExample['igbo']
            parseWord = urllib.parse.quote_plus(item['word'])

            differentiateDuplicateAndNonDuplicateLexemes(item['word'], usageExampleIgbo, item['definitions'][0], parseWord, lexemeWordClasses, item['wordClass'])

createIgboApiLexemes(my_response)


