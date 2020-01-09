# csv 전담 라이브러리 -> 표준 라이브러리
import csv

with open("../day7/점수.txt", mode="r", encoding="utf-8") as f:
    f_csv = csv.reader(f)   # csv.reader(파일)로 파일을 csv 형태로 읽어서 리스트의 묶음인 csv reader 오브젝트로 반환
    header = next(f_csv)  # next(csv reader 오브젝트)로 첫 줄을 없앨 수 있음
    kor_list = []
    eng_list = []
    math_list = []
    for row in f_csv:
        kor, eng, math = row
        kor_list.append(int(kor))
        eng_list.append(int(eng))
        math_list.append(int(math))
    print(sum(kor_list))
    print(sum(eng_list))
    print(sum(math_list))