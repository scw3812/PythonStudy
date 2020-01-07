# 모듈
# : .py 파일 하나
# -> 특징 : 서로 접근이 안됨 -> import 써서 가져와야 됨 -> import 모듈명, from 모듈명 import 요소 as 별칭
# import 기능은 사용하고자 하는 요소의 경로를 알려주는 역할
# 패키지
# : 관련있는 모듈의 그룹 -> like 폴더

# import day6.other as o6
# import day1.other as o1
# from day1 import other as o1
from day6 import other as o6
from day1.other import Test

print(o6.num)
o6.xxx()
# print(o1.Test)
print(Test)
