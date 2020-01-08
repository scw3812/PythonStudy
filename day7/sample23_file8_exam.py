# 점수.txt 파일을 읽어 국영수 총점, 평균 출력, 각 과목 최대, 최소
try:
    with open("./점수.txt", "r", encoding="utf-8") as f:
        scores = f.readlines()[1:]
        kor = []
        eng = []
        mat = []
        for score in scores:
            s = score.split(",")
            kor.append(int(s[0].strip()))  # 문자를 형변환할 때 공백들은 무시하는듯
            eng.append(int(s[1].strip()))  # strip()을 쓰면 \n도 없애줌
            mat.append(int(s[2].strip()))
        print("국어 총점:", sum(kor), "평균:", sum(kor)/len(kor))
        print("영어 총점:", sum(eng), "평균:", sum(eng)/len(eng))
        print("수학 총점:", sum(mat), "평균:", sum(mat)/len(mat))
        print("국어 최댓값:", max(kor), "최솟값:", min(kor))
        print("영어 최댓값:", max(eng), "최솟값:", min(eng))
        print("수학 최댓값:", max(mat), "최솟값:", min(mat))
except Exception as e:
    print("에러", e)
