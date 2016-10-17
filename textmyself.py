#Preset values:
accountSID='ACf840de09b4e55891566ef91943109839'
authTOKEN='787c3fca87aff4d341fc114ac7c3b8c4'
mytwilionumber='+16179817784'
mycellphone='+8615121015769'
from twilio.rest import TwilioRestClient
def textmyself(message):
    twilioCli = TwilioRestClient(accountSID, authTOKEN)
    twilioCli.messages.create(body=message,from_=mytwilionumber,to=mycellphone)

