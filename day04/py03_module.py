# py03_module.py

# 모듈 - 레고 
# 모듈사용 하려면 
# import 모듈명
# form 모듈명 import 상세...
import py02_car

hisCar = py02_car.Car('기아차','스팅거','몰라')
print(hisCar)

import py02_car as c  # as는 짧게 정리한거

herCar = c.Car('페라리','GT911','290sj2468')
print(herCar)

from py02_car import Car   # ㅈㄴ귀찮으면 이케쓰기 

thatCar = Car('람보르기니','이름몰라','58로1004')

