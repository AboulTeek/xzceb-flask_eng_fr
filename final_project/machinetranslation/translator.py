"""
To use IBM Watson Language translator to translate text from
English to French and vice versa.
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

#Creating an instance of the IBM Watson Language translator
#Author: Tarek Nasr

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(englishText):
    """
    Translating English text to French
    """
    translation = language_translator.translate(text=englishText,
    model_id='en-fr').get_result()
    return translation["translations"][0]['translation']

def frenchToEnglish(frenchText):
    """
    Translating French text to English
    """
    translation = language_translator.translate(text=frenchText,
    model_id='fr-en').get_result()
    return translation["translations"][0]['translation']
