import math

# 1. rad을 degree로 degree를 rad으로 바꾸는 법
print(math.pi) # 라디안 pi : 3.14
degree = 30
# rad = 30 * (math.pi / 180) : 공식
rad = math.radians(degree) # 공식대신 메서드
print(rad)
degree = math.degrees(rad) # 공식대신 degree로 변환

# 2. sin, cos, tan
print(f'{math.sin(rad):.1f}')
print(f'{math.cos(rad):.1f}')
print(f'{math.tan(rad):.1f}')

# 2. sin, cos, tan
print(f'{math.sin(rad):.1f}')
print(f'{math.cos(rad):.1f}')
print(f'{math.tan(rad):.1f}')

# 3. 피타고라스 정리 (두 변의 길이를 알 때 나머지 한변의 길이 구하기_
# b 와 c 를 알고 a를 구하고 싶다

b = 4
c = 5
# 식 a**2 + b**2 = c**2
# a**2 = c**2 - b**2
# 양 변에 루트 씌우기 ( 루트: sqrt)
a = math.sqrt(c**2 - b**2)
print(a)

# 4. 삼각함수의 역함수 (변의 길이를 알고 각도를 알고 싶을 때)
print(math.asin(a/c))
print(math.acos(a/c))
print(math.atan(a/c))

# 이건 알고 있어야 함!!!
# 직경: 지름
# 당구대 플레이 영영 = 254 * 127
# 공 직경: 5.73
# 코딩 시 좌표의 1.0 은 1cm를 의미

# =====================================================
start = (1, 1)
end = (2, 2)

a = abs(start[0] - end[0])
b = abs(start[1] - end[1])

r = math.sqrt(a**2 + b**2)

# math.atan 결과는 radian 으로 나옴 내장함수로 degree 로 변환해야함
radian = math.atan(b/a)

print(r, math.degrees(radian))

# ========================
# start = (x1, y1)
# end = (x2, y2)
# 가로 길이
a = abs(start[0] - end[0])
# 세로 길이
b = abs(start[1] + end[1])
# 대각선 길이
r = math.sqrt(a**2 + b**2)
# 라디안 길이
radian = math.atan(a / b)
# 라디안을 각도로 변환
d = math.degrees(radian)

# ------ 함수로 적용 (쎄타 값 알아내기 공식)-----------
def calculate_theta(x1, y1, x2, y2):
    x = x2 - x1
    y = y1 + y2

    theta = math.atan(x / y)
    return theta

x1, x2 = 1.0, 2.0
y1, y2 = 5.0, 1.0

alpha = calculate_theta(x1, y1, x2, y2)

print(alpha)
print(math.degrees(alpha))

# -------------------------
# 1 은 myball 2 는 hole, 3은 target
x1, x2, x3 = 1.0, 5.0, 3.0
y1, y2, y3 = 1.0, 5.0, 2.0

# 반지름
r= 5.73 / 2

x = x2 - x1
y = y2 - y1

# my ball ~ hole 까지의 거리(대각선)
a = math.sqrt(x ** 2 + y ** 2)
# target ~ hole 까지 거리(대각ㄴ)
b = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
# myball ~ target까지의 거리(대각선
c = math.sqrt((x3- x1) ** 2 + (y3 - y1) ** 2)

# a 랑 y 사이 각도(radian 값)
ga = math.atan(x / y)

# a랑 b 사이 각도(radian 값)
da = math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))
# my ball 이 움직여야 하는 거리
d = math.sqrt(a ** 2 + (b + 2 * r) ** 2 - (2 * a * (b + 2 * r) * math.cos(da)))
# a 랑 d 사이 각도
na = math.acos((a ** 2 + d ** 2 - ((b + 2 * r) ** 2)) / (2 * a * d))
# y 랑 d 사이 각도 (최종적으로 구해야하는 cos에 들어가는 값)
theta = ga + na

# 마찰계수(주어진다고는 하는데,, 흠,,,
mu = 0  #(0.?)
# 중력가속도
g = 9.8

# 목표: target 이 hole 까지 도달 (거리가 b 이상 되야함)
# 목적구의 속도 / v = 내공의 속도
v_t = math.sqrt(2 * mu * g * b)
v = v_t / math.cos(theta)

# -------- 연습 -----------
a = math.sqrt(x ** 2 + y ** 2)
b = math.sqrt((y2 - y3) ** 2 + (x2 - x3) ** 2)
c = math.sqrt((x3-x1) ** 2 + (y3 - y1) ** 2)

ga = math.atan(x / y)

da = math.acos((a** 2 + b**2 - c **2) / (2 * a* b))

d = math.sqrt(a ** 2 + (b + 2 * r) ** 2 - (math.cos(da) * 2 * a * (b + 2 * r)))

na = math.acos((a ** 2 + d ** 2 -(b + 2 * r) ** 2) / (2 * a * d))
theta = ga + na