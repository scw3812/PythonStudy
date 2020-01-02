# 실습문제
# 1. 영화 닥터 스트레인지, 스플릿, 럭키를 리스트에 저장
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
print(movie_rank)

# 2. 리스트에 배트맨 추가
movie_rank.append("배트맨")
print(movie_rank)

# 3. 닥터 스트레인지와 스플릿 사이에 배트맨 추가
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)

# 4. 럭키 삭제
movie_rank.remove("럭키")
# movie_rank.pop(3)
print(movie_rank)

# 5. 스플릿 배트맨 삭제
# movie_rank.remove("스플릿")
# movie_rank.remove("배트맨")
# del movie_rank[2:4]
movie_rank = movie_rank[:2]
print(movie_rank)

# 6. lang1과 lang2 합치기
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
# langs = list(set(lang1).union(set(lang2)))
# lang1.extend(lang2)
# langs = lang1.copy()
langs = lang1 + lang2
print(langs)

# 7. 최대, 최소, 총합 출력
nums = [1, 2, 3, 4, 5, 6, 7]
print("최댓값 :", max(nums))
print("최솟값 :", min(nums))
print("총합 :", sum(nums))

# 8. 왼쪽 8개만 변수에 저장
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, _, _ = scores  # start expression을 사용할 때 필요없는 변수는 언더바로 대체
print(valid_score)
