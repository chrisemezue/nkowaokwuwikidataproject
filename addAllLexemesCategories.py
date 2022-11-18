import tfsl
import requests
import json
import urllib.parse
from duplicateForAllLexemes import filterAllNonDuplicateLexeme

api_key_token = "aaa1b71a-6c34-4fab-b024-059e3ed23739"
headers = { 'X-API-Key' : api_key_token}
headerSet = {'Accept': 'application/json'}
base_url = "https://igboapi.com/api/v1/"
request_url = base_url + "/words?keyword=a&range=%5B1%2C%2025%5D&examples=true"

lexemeCategoriesList = ['ADJ', 'ADV', 'AV', 'MV', 'PV', 'CJN', 'DEM', 'NM', 'NNC', 'NNP', 'PREP', 'PRN', 'WH', 'INTJ']

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
}

# lexemeWordClasses[item['wordClass']]

response = requests.get(request_url, headers=headers)
my_response = response.json()
# my_response = ""

def AddBulkIgboTestingWordsToWikidata(ApiResponse):
    # print(len(ApiResponse))
    for item in ApiResponse:
        # import pdb;pdb.set_trace()
        if item['wordClass'] in lexemeWordClasses.keys():
        # for x in lexemeWordClasses.keys():
            # if x in item['wordClass']:
            print('WordClass is', item['wordClass'], item['word'], item['definitions'][0])
            usageExample = item['examples'][0]
            usageExampleIgbo = usageExample['igbo']
            #creating senses
            #passedword
            parseWord = urllib.parse.quote_plus(item['word'])
            response2 = requests.get('https://lexeme-forms.toolforge.org/api/v1/duplicates/www/ig/' + item['word'], headers=headerSet)
            if response2.status_code == 200:
                duplicateResponseData = response2.json()
                print("This word is a duplicate lexeme = ", duplicateResponseData[0]['label'])
            elif response2.status_code == 204:
                filterAllNonDuplicateLexeme(item['word'], usageExampleIgbo, item['definitions'][0], parseWord, lexemeWordClasses, item['wordClass'])

            # else: 
            #     print('no match')


AddBulkIgboTestingWordsToWikidata(my_response)




