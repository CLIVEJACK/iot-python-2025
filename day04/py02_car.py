# py02_car.py

# 객체지향 다시 
class Car:
    ## __new__사용빈도가 낮음, __init__ 많이 사용    __init__ 은 초기화 한다 
    ## Car()를 호출하면 아래의 메서드가 실행     __init__이 하는일
    ## company, name, plateNumber 모를때는 None을 넣는다 몰은 먼지몰라.
    def __init__(self, company = None, name = None, plateNumber = None):  # self는 자기자신(Car)를 말한다 나머지는 자기자신의 구성요소
        self.__company = company  # 멤버변수이름 앞에 __쓰면 외부접근 불가능 
        self.__name = name
        self.__plateNumber = plateNumber
        print('Car 클래스를 새로 생성!')

    # 클래스 자체가 출력되는데,__str__문자열로 출력되도록 바꿔줌
    # def __str__(self):
    #     return f'제차는 {self.__name}이고, 차번호는 {self.__plateNumber}입니다.'
    
    # 외부에서 잘목된 차번호를 넣으면 안들어감
    def setPlateNumber(self, newPlateNumber):
        if type(newPlateNumber) is str:  # 문자열str로 설정해서 문자열만 들어가고 나머지는 안들어감
            self.__plateNumber = newPlateNumber

    def setName(self, newName = '글쎄요'): # 이름을 모를때 글쎼요로 대처처
        self.__name = newName

    def getName(self):
        return self.__name

# 모듈화 하려면 예제소스를 없어야 함
# myCar = Car('현대차','아이오닉','54라9537')
# 파라미터명 = 값 으로 먀갸변수 순서를 변경가능
# myCar = Car(name = '아이오닉',plateNumber= '54라9537',company='현대자동차')

# print(myCar) # 차의 번호를 출력하고 싶음

# myCar.__plateNumber = 2018 # 클래스 외부에서 잘못된 데이터를 넣어도 문제가 발생하지 않는다.
# print(myCar)

# myCar.setPlateNumber('54라9999')
# print(myCar)

# yourCar = Car()
# print(yourCar)
# yourCar.setPlateNumber('285구8899')
# print(yourCar)
# yourCar.setName('제네시스')
# print(yourCar)