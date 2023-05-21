import json
import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import pylint
load_dotenv()

apikey = os.environ['api_key']
apiurl = os.environ['api_url']

authenticator = IAMAuthenticator('api_key')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator

)

language_translator.set_service_url(apiurl)


def english_to_french(english_text):
    translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    french_text=translation
    return french_text["translations"][0]["translation"]

def french_to_english(french_text):
    translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    english_text=translation
    return english_text["translations"][0]["translation"]
