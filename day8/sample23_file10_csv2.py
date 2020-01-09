# csv 전담 라이브러리 -> 표준 라이브러리
# csv 파일 값 구분은 콤마로만 중간에 공백이 있으면 안됨
import csv
from collections import namedtuple

with open("../day7/점수.txt", mode="r", encoding="utf-8") as f:
    f_csv = csv.reader(f)   # csv.reader(파일)로 파일을 csv 형태로 읽어서 리스트의 묶음인 csv reader 오브젝트로 반환
    header = next(f_csv)  # next(csv reader 오브젝트)로 첫 줄을 읽어 없앨 수 있음
    named_tuple = namedtuple("named_tuple", header)  # 변수명 = namedtuple("변수명", 헤더) -> 라벨값과 변수명이 같아야 함
    for r in f_csv:
        row = named_tuple(*r)  # namedtuple 변수명(*리스트) -> 변수명(key=value, key=value...)로 바꿈
        print(row)
