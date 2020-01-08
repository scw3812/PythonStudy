# 점수.txt 파일을 읽어 국영수 총점, 평균 출력, 각 과목 최대, 최소

print("프로그램 시작")

kor_list = []
eng_list = []
math_list = []

try:
    with open("./점수.txt", "r", encoding="utf-8") as f:
        header = f.readline()  # 첫 줄을 없애고 싶으면 한 줄만 읽고 다시 읽어라
        while True:
            row = f.readline()
            if not row:
                break
            kor, eng, math = row.split(",")
            kor_list.append(int(kor.strip()))
            eng_list.append(int(eng.strip()))
            math_list.append(int(math.strip()))
except Exception as e:
    print("에러", e)

print("국어 총점:", sum(kor_list), "평균:", sum(kor_list)/len(kor_list))
print("영어 총점:", sum(eng_list), "평균:", sum(eng_list)/len(eng_list))
print("수학 총점:", sum(math_list), "평균:", sum(math_list)/len(math_list))
print("국어 최댓값:", max(kor_list), "최솟값:", min(kor_list))
print("영어 최댓값:", max(eng_list), "최솟값:", min(eng_list))
print("수학 최댓값:", max(math_list), "최솟값:", min(math_list))

print("프로그램 종료")
