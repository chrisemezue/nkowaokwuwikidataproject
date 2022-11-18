
import requests
import json
import schedule
import time
import tfsl
import urllib.parse
# referenceUrlForOfficialWebsiteP856 = "https://nkowaokwu.com/lacuna"


def filterAllNonDuplicateLexeme(word, usageExampleIgbo, newsense_, parseWord, lexemeWordClasses, code):
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

    newlexeme = tfsl.Lexeme(word @ tfsl.langs.ig_, tfsl.langs.ig_, lexemeWordClasses[code], statements = statementlist, senses = senselist)
        # print("newlexeme", newlexeme)
    #submitting lexeme
    # current_session.push(newlexeme, "new lexeme")
    