# 1. 아스키코드 (유니코드)
# 대문자 A : 64 / 소문자 a :97
# 대문자 + 32 => 소문자

# 2. Parsing 문제에서 쓰는 메서드 : find 메서드
# 1) str.find() : 찾으면 발견된 인덱스 반환, 못 찾으면 -1 반환
#       .index() : 못 찾으면 에러를 발생 시켜서 잘 안쓰고 find 씀
# 2) str.find('a', n) : n번 인덱스부터 시작해서 문자 'a'를 찾아라 / 못찾으면 -1 반환
# ex) [1234]wneir[23]woe[12]-> 대괄호 안에 있는 숫자만 Parsing 해서 더하고 싶다.

text = 'banana'

n1 = text.find('a')     # 첫번째로 발견된 a 인덱스 반환
print(n1) # 1
n2 = text.find('a', n1+1)
print(n2)   # 3
n3 = text.find('a', n2+1)
print(n3)   # 5

# 3) 회문 : 거꾸로 읽어도 같은 문자열
# 거꾸로 뒤집는 방법 [::-1]
text = "level"

# 회문이냐? 회문 판별 함수
def is_p(text):
    return text == text[::-1]

print(is_p(text))
print(int(is_p(text)))  # 같으면 1, 다르면 0 반환

# -------------------------------------------------

# Parsing 배우는 이유
# 1. 코테 준비
# 2. 현업에서 반드시 필수 역량
# 3. 디버깅 훈련에 좋다 기타 등등
