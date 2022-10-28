import tfsl
import requests
import json
import urllib.parse


#fetching data from igbo api
#request_url = "https://igboapi.com/api/v1/words?keyword=a&range=%5B1%2C%2025%5D" //for 1-25 pages
#request_url = "https://igboapi.com/api/v1/words?keyword=z&range=%5B1%2C%2025%5D&examples=true" //for 1-25 pages and examples

#testingstate https://igboapi.com/api/v1/words?keyword=a&range=%5B1%2C%203%5D&examples=true

api_key_token = "aaa1b71a-6c34-4fab-b024-059e3ed23739"
headers = { 'X-API-Key' : api_key_token}
base_url = "https://igboapi.com/api/v1/"
request_url = base_url + "/words?keyword=a&range=%5B1%2C%203%5D&examples=true"
# nkowaOkwuUrl = "https://nkowaokwu.com/word?word={}"
# fullWorkAvailable = 'https://nkowaokwu.com/word?word={}'

lexemeWordClasses = {
    "ADJ": "Q34698",
    "ADV": "Q380057",
    "AV": "Q24905",
    "MV": "",
    "PV": "",
    "CJN": "Q36484",
    "DEM": "",
    "NM": "",
    "NNC": "Q1084",
    "NNP": "",
    "CD": "",
    "PREP": "Q4833830",
    "PRN": "Q36224",
    "FW": "",
    "QTF": "",
    "WH": "",
    "INTJ": "Q83034",

}

response = requests.get(request_url, headers=headers)
my_response = response.json()
# my_response = ""
# print("my_response", len( my_response))

def AddBulkIgboNounWordsToWikidata(ApiResponse):
    my_username = 'TemTechie'
    my_password = '2580Ndutem144$$'
    current_session = tfsl.WikibaseSession(my_username, my_password)
    fullWorkAvailable = 'https://nkowaokwu.com/word?word={}'
    referenceUrlForOfficialWebsite = "https://nkowaokwu.com/lacuna"
    for item in ApiResponse:
        if 'NNC' in item['wordClass']:
            # print('this is a noun item', item['wordClass'], item['word'], item['definitions'][0])
            usageExample = item['examples'][0]
            usageExampleIgbo = usageExample['igbo']
            usageExampleEnglish = usageExample['english']
            #creating senses
            #passedword
            parseWord = urllib.parse.quote_plus(item['word'])
            referenceUrlforFullWorkAvailableAt = fullWorkAvailable.format(parseWord)
            #
            newsense_gloss = item['definitions'][0] @ tfsl.langs.en_
            newsense = tfsl.LexemeSense([newsense_gloss])
            senselist = [newsense]
            #creating statement and references
       
            newstatement = tfsl.Statement("P5831", usageExampleEnglish @ tfsl.langs.en_, references=[tfsl.Reference(tfsl.Claim("P856", referenceUrlForOfficialWebsite)), tfsl.Reference(tfsl.Claim("P953", referenceUrlforFullWorkAvailableAt))])
            newstatement2 = tfsl.Statement("P5831", usageExampleIgbo @ tfsl.langs.ig_, references=[tfsl.Reference(tfsl.Claim("P856", referenceUrlForOfficialWebsite)), tfsl.Reference(tfsl.Claim("P953", referenceUrlforFullWorkAvailableAt))])
            
            statementlist = [newstatement, newstatement2]
            #creating lexeme
            newlexeme = tfsl.Lexeme(item['word'] @ tfsl.langs.ig_, tfsl.langs.ig_, "Q1084", statements = statementlist, senses = senselist)

            #submitting lexeme
            # current_session.push(newlexeme, "new lexeme")
        # else: 
        #     print('no match')

AddBulkIgboNounWordsToWikidata(my_response)



# ADJ - Adjective
# ADV - Adverb
# AV - Active verb
# MV - Medial verb
# PV - Passive verb
# CJN - Conjunction
# DEM - Demonstrative
# NM - Name
# NNC - Noun
# NNP - Proper noun
# CD - Number
# PREP - Preposition
# PRN - Pronoun
# FW - Foreign word
# QTF - Quantifier
# WH - Interrogative
# INTJ - Interjection
# ISUF - Inflectional suffix
# ESUF - Extensional suffix
# SYM - Punctuations

##Function to create and submit lexeme##
#igbo languge categories 
#Igbo (Q33578)
# 1. noun (Q1084) Aha n'Igbo
# 2. verb (Q24905) Ngwaa n'Igbo
# 3. pronoun (Q36224) Nnọchiaha n'Igbo
# 4. adjective (Q34698) Nkọwaaha n'Igbo
# 5. adverb (Q380057) Nkwuwa n'Igbo
# 6. preposition (Q4833830) Mbuụzọ n'Igbo
# 7. conjunction (Q36484)  njikọ n'Igbo
# 8. interjection (Q83034) ntinye aka n'Igbo










