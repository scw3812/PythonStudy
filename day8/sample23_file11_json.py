# JSON 포맷 -> javascript 프로그램언어에서 객체 표현시 사용하는 방법
# 1. 배열 객체 : [값1, 값2]
# 2. 일반 객체 : {키 : 값}
# 용도 : 포털사이트 및 공공기관에서 제공하는 무료 데이터(open API)는 거의 JSON 형식

response_data = '{"username": "홍길동","age": 20}'  # JSON str -> '{"key":value,...}' 밖은 홑따옴표, 안은 쌍따옴표
response_data2 = {"username": "홍길동", "age": 20}  # dict

# str -> dict
import json

json_data = json.loads(response_data)  # json.loads(JSON string)으로 string을 dict(JSON)로 바꿔줄 수 있다.
print(json_data)

str_data = json.dumps(response_data2)
print(str_data, type(str_data))  # \uXXXX -> 유니코드(전 세계 모든 언어를 표현하기 위해 만든 코드)
str_data2 = json.dumps(response_data2, ensure_ascii=False)  # ensure_ascii=False -> 유니코드를 한글로
print(str_data2)
