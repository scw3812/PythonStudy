# csv 전담 라이브러리 -> 표준 라이브러리
# csv 파일 값 구분은 콤마로만 중간에 공백이 있으면 안됨
import csv

with open("../day7/점수.txt", mode="r", encoding="utf-8") as f:
    f_csv = csv.DictReader(f)   # csv.DictReader(파일)로 파일을 csv 형태로 읽어서 딕트의 묶음인 오브젝트로 반환 -> 첫줄을 헤더로
    for row in f_csv:
        print(row)
