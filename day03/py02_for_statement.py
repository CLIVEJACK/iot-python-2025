# py02_for_statement.py

# for 문: 프로그래밍의 꽃
# 반목을 처리할 떄 사용 
# for 변수 in 반목할 값:
#    구문안으로...

# 아래와 출력되는 프로그램을 작성하시
'''
*
**
***
****
'''

# range() 범위를 생성하는 함수
# 마지막수 : max - 1 
# range(8) -> range(0,8)
# range(init, max, add)
# print(range(0, 8, 2))

# for i in [0, 1, 2, 3, 4, 5, 6, 7]: # 이 조건이 참인동안 반복 ...
# # for i in range(0,8):
#     print(i)


# num =int(input('최대별수 : '))

# for i in range(1, num + 1):
#     print('*' * i)

# 구구단
# 2단부터 2x9 ~ 9x9
# 2x1 = 2, 2x2 = 4 .......
# 요구사항1 - 한줄에 각 단씩 나오도록 
# 요구사항2 - ixj값이 항상 두줄씩 표현되도록 
# 요구사항3 - 단시작을 표시 
for i in range(2, 9 + 1):
    # if i == 8 : break   # 브레이크는 여기서 멈춤
    if i == 5 : continue  # 컨티뉴는 이거제외하고 출력 

    print(f'{i}단 시작')
    for j in range(1, 9 + 1):
        print(f'{i} x {j} = {i * j:2d}', end = '    ')
    
    print() # 그냥 한줄내리기 

print('구구단종료 \n\n\n\n')

## 반복을 빠져나올때 : break
## 반목문에서 특정 조건을 지나칠떄 : continue