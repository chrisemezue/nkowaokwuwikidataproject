import requests
import json
import schedule
import time

headers = {'Accept': 'application/json'}

response = requests.get('https://lexeme-forms.toolforge.org/api/v1/duplicates/www/ig/zu', headers=headers)

duplicateResult = response.json()
# print(f"Response: {r.json()}")

print("duplicate result now", duplicateResult)
