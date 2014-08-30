import requests
import json
import urllib2
import webbrowser
from pprint import pprint

token = 'CAACEdEose0cBAPLG4DEapGSE8ZAxSALnNanAXtRTpZBM390EhRZAV3ZBnh7bZBLERNRLRXXclW53LubKLGWZB7j2CZBgh9F5ZAuBDiAWY5xFrAiKb8Sha7HrwXVKM9zbD7vkJOmHeIbbOZAuvtIaIQupU6DhntFPZC1bVTU6VvXUlBsdmHGEQfYbKX0yV1ejLL194Ae9m7ernx6TArdQBR0o5zee7quRTBvTYZD'
api_url = 'https://graph.facebook.com/v2.1/'
params = {'access_token' : token}

def extractFriends():
    call = "me/friends?fields=picture.type(large),gender,name"
    response = requests.get(api_url + call, params=params)
    r = (json.loads(response.content))
    #pprint(r)
    for f in r['data']:
        #print f['name'], f['gender']
        p_url = str(f['picture']['data']['url'])
        print p_url
        #webbrowser.open(p_url)
        #urllib.urlretrieve(p_url, 'something21.jpg')
        
        opener1 = urllib2.build_opener()
        page1 = opener1.open(p_url)
        my_picture = page1.read()

        filename = "my_image.jpg"
        print filename
        fout = open(filename, "wb")
        fout.write(my_picture)
        fout.close()
        
        break


extractFriends()
