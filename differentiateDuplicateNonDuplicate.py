
import requests
import json
import schedule
import time
import tfsl
import urllib.parse

from handleLexemesSubmit import handleLexemesSubmitToWikidata

headerSet = {'Accept': 'application/json'}

def differentiateDuplicateAndNonDuplicateLexemes(word, usageExampleIgbo, newsense_, parseWord, lexemeWordClasses, code):
    response2 = requests.get('https://lexeme-forms.toolforge.org/api/v1/duplicates/www/ig/' + word, headers=headerSet)
    if response2.status_code == 200:
        # Duplicate Lexemes
        duplicateResponseData = response2.json()
        print("This word is a duplicate lexeme = ", duplicateResponseData[0]['label'])
    elif response2.status_code == 204:
        # Non Duplicate Lexemes
        fullWorkAvailable = 'https://nkowaokwu.com/word?word={}'
        referenceForReferenceURL = "https://nkowaokwu.com/lacuna"
        referenceforFullWorkAvailableAt = fullWorkAvailable.format(parseWord)
        newsense_gloss = newsense_ @ tfsl.langs.en_
        newsense = tfsl.LexemeSense([newsense_gloss])
        senselist = [newsense]
        newstatement = tfsl.Statement("P5831", usageExampleIgbo @ tfsl.langs.ig_, references=[tfsl.Reference(tfsl.Claim("P854", referenceForReferenceURL)), tfsl.Reference(tfsl.Claim("P953", referenceforFullWorkAvailableAt))])
        statementlist = [newstatement]
        newlexeme = tfsl.Lexeme(word @ tfsl.langs.ig_, tfsl.langs.ig_, lexemeWordClasses[code], statements = statementlist, senses = senselist)

        handleLexemesSubmitToWikidata(newlexeme)
    