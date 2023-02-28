import base64
with open("img/captcha_1.png", "rb") as image_file:
    base64str = base64.b64encode(image_file.read()).decode("utf-8")

import requests, json
payload = json.dumps({
  "base64str": base64str,
  "threshold": 0.5
})
response = requests.put("http://52.30.21.139/predict",data = payload)
data_dict = response.json()

print(data_dict)