import base64

path = input("Enter image name:")

with open(f"{path}", "rb") as image_file:
    base64str = base64.b64encode(image_file.read()).decode("utf-8")

import requests, json
payload = json.dumps({
  "base64str": base64str,
  "threshold": 0.5
})
response = requests.put("http://54.217.150.250/predict",data = payload)
data_dict = response.json()

print(data_dict)