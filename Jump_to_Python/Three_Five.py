"""1. 3과 5의 배수 합하기"""
#1000미만의 자연수

result = 0
for i in range(1000):
    if i % 3 == 0:
        result += i
    elif i % 5 == 0:
        result += i
print(result)

#다른 풀이

result = 0
for n in range(1, 1000):
    if n % 3 == 0 or n % 5 == 0:
        result += n
print(result)
