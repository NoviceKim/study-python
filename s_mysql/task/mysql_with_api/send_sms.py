import json
import message

# 한번 요청으로 1만건의 메시지 발송이 가능합니다.
def send_message(phone, certification_number):
    data = {
        'messages': [
            {
                'to': 'phone',
                'from': '01086709568',
                'text': f'[인증번호]\n{certification_number}'
            }
        ]
    }
    res = message.send_many(data)
    print(json.dumps(res.json(), indent=2, ensure_ascii=False))
