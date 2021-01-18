import hashlib
import urllib
import random
import time
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = ""
# Your Auth Token from twilio.com/console
auth_token  = ""

client = Client(account_sid, auth_token)


url = ""

sleeptime = 300 

def getHash(): 
    randomint = random.randint(0,6)
    user_agents = [
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
        'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.142 Safari/535.19',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:8.0.1) Gecko/20100101 Firefox/8.0.1',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.151 Safari/535.19'
    ]
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', user_agents[randomint])]
    response = opener.open(url)
    the_page = response.read()
    return hashlib.sha224(the_page).hexdigest()

current_hash = getHash()
while 1: 
    x = getHash()
    if x != current_hash: 
        
        print('Hey, something changed on the site')
        message = client.messages.create(
            to="", #your number 
            from_="", #twilio number
            body="Something changed on https://www.fetchwi.org/adopt")
        print(message.sid)
    else:
        print('no change')
   
    current_hash = x
    time.sleep(sleeptime)
    