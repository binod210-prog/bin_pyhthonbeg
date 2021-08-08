apikey = '70gHJPFfry9YUXHyJabcfZ4ar-WS8omOCMkrGmjrDJE_'

url = 'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/fe2a5d0e-4666-42ff-b207-c9cc386093bc'

# import deps
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Setup service
authenticator = IAMAuthenticator(apikey)
lt = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)
lt.set_service_url(url)


translation = lt.translate(text='Hello', model_id='en-de').get_result()
text_tr = translation['translations'][0]['translation']
print(text_tr)

