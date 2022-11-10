import requests
import json
import schedule
import time
import urllib.parse

headerSet = {'Accept': 'application/json'}

word = "zọ ọkwagg"
parseWord = urllib.parse.quote_plus(word)

api_key_token = "aaa1b71a-6c34-4fab-b024-059e3ed23739"
headers = { 'X-API-Key' : api_key_token}
base_url = "https://igboapi.com/api/v1/"
request_url = base_url + "/words?keyword=a&range=%5B1%2C%2025%5D&examples=true"

response = requests.get(request_url, headers=headers)

duplicateResult = response.json()



for lexeme in duplicateResult:
    parseWord = urllib.parse.quote_plus(lexeme['word'])
    response2 = requests.get('https://lexeme-forms.toolforge.org/api/v1/duplicates/www/ig/' + parseWord, headers=headerSet)
    if response2.status_code == 200:
        duplicateResponseData = response2.json()
        print("duplicate word is = ", duplicateResponseData[0]['label'])
    elif response2.status_code == 204:
        print("this is not a duplicate word", response2)
    

