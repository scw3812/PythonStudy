import requests
import json

url = "http://openapi.seoul.go.kr:8088/sample/json/SeoulLibraryTime/1/5"
response_data = requests.get(url)  # 200 : success, 404 : file not found
str_data = response_data.text
json_data = json.loads(str_data)
print(json_data)

for i in range(len(json_data["SeoulLibraryTime"]["row"])):
    print(json_data["SeoulLibraryTime"]["row"][i]["LBRRY_NAME"])