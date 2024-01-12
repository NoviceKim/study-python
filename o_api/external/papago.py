# clientID: uxrSmI_uYTAYICL5YP8J
# clientSecret: r0Olb4srIA
# https://openapi.naver.com/v1/papago/n2mt
import urllib.request
import json

client_id = 'uxrSmI_uYTAYICL5YP8J'
client_secret = 'r0Olb4srIA'

encoding_text = urllib.parse.quote("다람쥐는 헌 쳇바퀴에 돌고파")
data = f'source=ko&target=en&text={encoding_text}'
url = 'https://openapi.naver.com/v1/papago/n2mt'

request = urllib.request.Request(url)

# -H (Header)
request.add_header('X-Naver-Client-Id', client_id)
request.add_header('X-Naver-Client-Secret', client_secret)
response = urllib.request.urlopen(request, data=data.encode('utf-8'))
rescode = response.getcode()

if rescode == 200:
    response = json.loads(response.read().decode('utf-8'))
    print(response['message']['result']['translatedText'])