#클래스 기본

class Calculator:
    def __init__(self):
        self.result = 0

    def adder(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result -= num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.adder(3))
print(cal1.adder(4))
print(cal1.sub(3))
print(cal2.adder(3))
print(cal2.adder(7))
print(cal2.sub(3))

#사칙연산 계산기

class FourCal:
    def __init__(self, first, second): #생성자
        self.first = first
        self.second = second        
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def sum(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = FourCal(4, 2)
print(a.first)
print(a.second)
print(a.sum(), a.mul(), a.sub(), a.div())

#상속

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(4, 2)
print(a.pow())

#오버라이딩

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            result = self.first / self.second
            return result

a = SafeFourCal(4, 0)
print(a.div())
