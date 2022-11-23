import tfsl
import requests
import urllib.parse


api_key_token = "aaa1b71a-6c34-4fab-b024-059e3ed23739"
headers = { 'X-API-Key' : api_key_token}
headerSet = {'Accept': 'application/json'}

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

def handleLexemesSubmitToWikidata(newlexeme,push=False):
    my_username = 'TemTechie'
    my_password = '2580Ndutem144$$'
    current_session = tfsl.WikibaseSession(my_username, my_password)
    print("newlexeme", newlexeme)
    #submitting lexeme
    if push:
        current_session.push(newlexeme, "new lexeme")


def differentiateDuplicateAndNonDuplicateLexemes(word, usageExampleIgbo, newsense_, parseWord, lexemeWordClasses, code):
    response2 = requests.get('https://lexeme-forms.toolforge.org/api/v1/duplicates/www/ig/' + word, headers=headerSet)
    if response2.status_code == 200:
        # Duplicate Lexemes
        duplicateResponseData = response2.json()
        print("This word is a duplicate lexeme = ", duplicateResponseData[0]['label'])
        return None
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
        return newlexeme

    

def createIgboApiLexemes(ApiResponse):
    for item in ApiResponse:
        if item['wordClass'] in lexemeWordClasses.keys():
            usageExample = item['examples'][0]
            usageExampleIgbo = usageExample['igbo']
            parseWord = urllib.parse.quote_plus(item['word'])

            newlexeme = differentiateDuplicateAndNonDuplicateLexemes(item['word'], usageExampleIgbo, item['definitions'][0], parseWord, lexemeWordClasses, item['wordClass'])
            if newlexeme is not None:
                handleLexemesSubmitToWikidata(newlexeme) # if you want to push it, then run handleLexemesSubmitToWikidata(newlexeme,push=True)


if __name__=='__main__':
    base_url = "https://igboapi.com/api/v1/"
    # keywordQueryParam = input("Enter keyword querying words:")
    request_url = base_url + "/words?keyword=i&range=%5B1%2C%2020%5D&examples=true"
    response = requests.get(request_url, headers=headers)
    my_response = response.json()

    createIgboApiLexemes(my_response)


