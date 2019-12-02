import requests
import json

url = 'http://testphp.vulnweb.com/login.php'

payload = {
    'uname': 'test',
    'pass': 'test',
    'sub':'submit'
}

resposta = requests.post(url, data=json.dumps(payload))

print(resposta.text)
print(resposta.status_code)

if(resposta.url != url):    
    print(resposta.status_code)
    print(resposta.url)
    print(url)
