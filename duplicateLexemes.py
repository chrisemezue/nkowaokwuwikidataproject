
import requests
import json
import schedule
import time
import tfsl
import urllib.parse
# referenceUrlForOfficialWebsiteP856 = "https://nkowaokwu.com/lacuna"


def filterNonDuplicateLexeme(word, usageExampleIgbo, newsense_, parseWord):
    my_username = 'TemTechie'
    my_password = '2580Ndutem144$$'
    current_session = tfsl.WikibaseSession(my_username, my_password)
    fullWorkAvailable = 'https://nkowaokwu.com/word?word={}'
    referenceUrlForReferenceURL = "https://nkowaokwu.com/lacuna"
    referenceUrlforFullWorkAvailableAt = fullWorkAvailable.format(parseWord)
                
    referenceUrlforFullWorkAvailableAt = fullWorkAvailable.format(parseWord)
    #
    newsense_gloss = newsense_ @ tfsl.langs.en_
    newsense = tfsl.LexemeSense([newsense_gloss])
    senselist = [newsense]

    #creating statement and references
    newstatement = tfsl.Statement("P5831", usageExampleIgbo @ tfsl.langs.ig_, references=[tfsl.Reference(tfsl.Claim("P854", referenceUrlForReferenceURL)), tfsl.Reference(tfsl.Claim("P953", referenceUrlforFullWorkAvailableAt))])
      
    statementlist = [newstatement]
    #creating lexeme
    newlexeme = tfsl.Lexeme(word @ tfsl.langs.ig_, tfsl.langs.ig_, 'Q54557461', statements = statementlist, senses = senselist)
    print("newlexeme", newlexeme)
    #submitting lexeme
    # current_session.push(newlexeme, "new lexeme")
    




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

for code in lexemeWordClasses.values():
    print("code", code)
