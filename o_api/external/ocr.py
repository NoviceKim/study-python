# https://ocr.space/OCRAPI
# K86576074088957(API 키)
# https://api.ocr.space/parse/imageurl?apikey=&url=
# https://api.ocr.space/parse/imageurl?apikey=&url=&language=&isOverlayRequired=true
import requests

url = 'https://api.ocr.space/parse/imageurl?apikey=K86576074088957&url=https://i.pinimg.com/474x/34/8b/c5/348bc51a10af4a96dea207318f88cc6b.jpg&language=kor&isOverlayRequired=true'
response = requests.get(url)
response.raise_for_status()

# 위 API가 분석한 글자 데이터를 json으로 받아옴
result = response.json()

print(type(result))