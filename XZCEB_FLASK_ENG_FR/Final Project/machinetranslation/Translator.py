import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Set some variables
api_key = '<Wzsv7x2X-EWRfAmqgOcIcv0STPNovX05tE4l_Ri896gw>'
api_url = '<https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/7434ebdd-03d7-4179-9cff-59fe138450b0>'
model_id = 'en-it'
text_to_translate = 'Hey how are you '

# Prepare the Authenticator
authenticator = IAMAuthenticator(api_key)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(api_url )

# Translate
translation = language_translator.translate(
    text=text_to_translate,
    model_id=model_id).get_result()

# Print results
print(json.dumps(translation, indent=2, ensure_ascii=False))

