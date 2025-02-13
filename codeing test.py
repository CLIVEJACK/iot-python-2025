def main():
    set_SmartPhone
    
class SmartPhone :
    def __init__(self,phoneOwner,phoneNumber,company):
        self.__phoneOwner = phoneOwner
        self.__phoneNumber = phoneNumber
        self.__company = company

    def __str__(self):
        str = (f'휴대폰 주인: {self.__phoneOwner}\n 휴대폰 번호: {self.__phoneNumber} \n 회사:{self.__company}')
        return str
    
    def getphoneOwner(self):
        return self.__phoneOwner
    def getphoneNumber(self):
        return self.__phoneNumber
    def getcompany(self):
        return self.__company
    
def set_SmartPhone():
    phoneOwner,phoneNumber,company = input('휴대폰 주인, 휴대폰 번호, 회사를 입력하세요 > ').split()
    smartphone = SmartPhone(phoneOwner=phoneOwner, phoneNumber=phoneNumber, company=company)
    return smartphone

if __name__== '__main__':
    print('입력')
    main()