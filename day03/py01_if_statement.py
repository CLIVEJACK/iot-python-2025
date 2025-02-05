# py01_if_statement.py

# if문 : 흐름제어 가장 기본
# 흐름제어문 마지막엔 항상 콜론(:)을 사용해야 함! 
# if (참이되는 조건):   :(colon), ;(semi-colon)
# if문 안으로 들어간다! 

age = int(input('나이를 입력하세요. > '))

# 만약에 나이가 19세가 아니면 담배를 살 수없음
# 조건이 여래개 일때 and나 or로 계속 작성성
if age > 19 or age == 19 : # 참인 조건 
# if age >= 19 :  위랑 같은 조건 
    print('4,500원입니다')
else :
    print('민자야 집에가라')

grade = input('학점을 입력하십시오 (A | B | C | D | F)').upper() # 소문자도 대문자로 변경 

if grade == 'A' or grade == 'B' : # 학점이 A이거나 B면 ,이 구문에 걸리면 구문안으로 들어간다 
    print('공부 열심히 하셨네요.')
    print('축하합니다')

    if grade == 'A':
        print('장학금을 드립니다.')
    else:
        print('잘했습니다 개추를 드리죠')

elif grade == 'C': # 학점이 C이면 
    print('그럭저럭 하셨네요')
else: 
    print('공부 좀 해라!')
