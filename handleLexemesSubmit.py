import requests
import json
import schedule
import time
import tfsl
import urllib.parse

def handleLexemesSubmitToWikidata(newlexeme):
    my_username = 'TemTechie'
    my_password = '2580Ndutem144$$'
    current_session = tfsl.WikibaseSession(my_username, my_password)
    print("newlexeme", newlexeme)
    #submitting lexeme
    current_session.push(newlexeme, "new lexeme")