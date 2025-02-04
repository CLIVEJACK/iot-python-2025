# py03_inout.py
# 화면입출력

print('출력입니다')
# 기본입력 
number = input('만나이를 입력하세요 > ') # 입력방법
# 입력되는 값, 출력되는 값 모두 문자열이다! 
number = int(number) # str -> int 로 변환 
print(type(number))
print("현재나이는", number + 1) # 여러 값을 같이 출력하려면 ,로 구분
# print("현재나이는", int(number) + 1) 이케도 변환 가능 

# 다중입력
x, y = input('합산할 두 수를 입력하세요 > ').split() # 기본 공백으로 잘라줘
x = int(x)
y = int(y)
print(x + y) 