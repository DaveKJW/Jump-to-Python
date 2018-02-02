# Jump-to-Python


# 문자열 자료형

  ● 문자열 인덱싱, 슬라이싱

        a = "20180122Cloudy"
        year = a[:4]
        day = a[4:8]
        weather = a[8:]
        print("Year : " + year + "\n" + "Day : " + day + "\n" + "Weather : " + weather)

  ● 문자열 포맷팅, 고급포맷팅

        "I eat %d apples." % 3      #숫자 바로 대입 - 포맷팅
        apple = "I eat %d apples." % 3
        "I eat {0} apples.".format(3) # 고급포맷팅

        number = 3
        "I eat %d apples" % number  #숫자값을 나타내는 변수 대입
        "I eat {0} apples.".format(number) # 고급포맷팅 

        number = 10
        day = "three"
        "I ate %d apples. So I was sick for %s days." % (number, day)    # 2개 이상의 값 넣기
        "I ate {0} apples. So I was sick for {1} days.".format(number, day) #고급포맷팅
        "I ate {number} apples. So I was sick for {day} days.".format(number = 5, day = "two") #이름으로 넣기 - 변수 지정하면서 넣기

        "{0:<10}".format("Hi") #왼쪽 정렬 - 총 공간 지정후 문자를 왼쪽으로 정렬한다.
        "{0:>10}".format("Hi") #오른쪽 정렬 - 총 공간 지정후 문자를 오른쪽으로 정렬한다.
        "{0:=^10}".format("Hi") #공백채우기 및 가운데 정렬

  ● 문자열 관련 함수

        a = "hobby" # count 함수는 문자의 갯수를 알려줌
        a.count('b')

        a = "Python is best choice" #find 함수는 해당 문자가 처음 등장하는 위치를 알려줌. 문자가 없다면 -1 반환
        a.find('b')

        a = "Life is too short" # index 함수는 해당 문자가 처음 등장하는 위치를 알려줌. 문자가 없다면 오류 발생
        a.index('t')

        a = ","
        a.join("abcd")

        ",".join("Life is")
        ",".join(('Life', 'is', 'long')) #join 함수는 문자열의 각각의 문자 사이에 변수를 삽입함.

        a = "Life is too short"
        a.replace("Life", "Your finger") #replace 함수는 문자열 내의 값을 다른 값으로 변경해줌.

        a = "Life is too short"
        a.split()
        a = "a : b : c :d"
        a.split(":") # 문자열을 변수에 따라 구분하여 나눠줌. 나눈 값은 리스트 형태로 저장됨. 

# 리스트 자료형

        a = [1, 2, 3, ['a', 'b', 'c']]
        a[0] # 리스트 자료형 인덱싱
        a[-1]
        a[3]
        a[-1][0] #이중 인덱싱

        a[0:2] # 리스트 자료형 슬라이싱
        a = [1, 2, 3, ['a', 'b', 'c'], 4, 5] # 중첩된 리스트에서 슬라이싱하기
        a[2:5]
        a[3][:2]

        a = [1, 2, 3]
        b = [4, 5, 6]
        a + b         # 리스트 자료형 더하기
        a * 3         # 리스트 자료형 곱하기

        a = [1, 2, 3]
        str(a[2]) + "hi" # 정수값과 문자열은 더하기 불가능

        a = [1, 2, 3]
        a[2] = 4      # 하나의 값 수정

        a[1:2] = ['a', 'b', 'c'] # 연속된 범위의 값 수정
        a[1] = ['a', 'b', 'c']   # 인덱싱과 슬라이싱의 수정시 차이
        del a[1]      # 리스트 요소 삭제

  -리스트 관련 함수

        a = [1, 2, 3]
        a.append(4)   #리스트 요소 추가 - 어떤 자료형도 추가 가능

        a = [1 ,4, 3, 2]
        a.sort()      # 순서대로 정렬
        a.reverse()   # 순서를 뒤집음
        a.index(3)    # 위치를 반환해줌.
        a.insert(0,4)  # 해당 위치에 해당 값을 삽입.
        a.remove(3)    # 해당 값을 삭제. 첫번째 것만 삭제됨.
        a.pop(1)      # x번째 변수를 돌려주고 삭제함. 빈값으로 넣으면 마지막 요소를 반환후 삭제.

        a = [1, 2, 3]
        a.extend([4, 5])  # 리스트 안에 리스트 값을 추가함. 괄호안에는 리스트만 가능.

# 튜플 자료형

        t1 = ()
        t2 = (1,)    # 요소가 1개일때는 ',' 반드시 붙여야함.
        t3 = (1, 2, 3)
        t4 = 1, 2, 3    # 튜플은 괄호 생략 가능
        t5 = 1, 2, "hello", 4          # 자료형 구분 없이 선언가능
        t6 = 1, 2, (3, 4, 5), 6, 7     # 튜플 안에 튜플 넣는 것 가능

튜플은 추가, 변경, 삭제가 안됨.

# 딕셔너리 자료형

항상 쌍으로 존재한다.

Key에는 변하지 않는 값을 사용. Value에는 변하는 값, 변하지 않는 값 모두 사용.

        dic = {'name':'pey', 'phone':'0119993323', 'birth':'1128'}
        a = {1: 'a'}
        a[2] = 'b'     
        a['name'] = 'pey'   # 딕셔너리 요소 추가

        grade = {'pey': 10, 'julliet': 99}    # Key로 Value 찾기
        grade['pey']

   Key값으로 리스트는 쓸수 없으나 튜플은 사용 가능

  ● 딕셔너리 관련 함수

        a = {'name':'pey', 'phone':'0119993323', 'birth':'1128'}
        a.keys()     # Key값들 반환
        a.values()   # Value값 반환
        a.items()    # Key, Value 모두 반환 - 튜플형태로
        a.clear()    # 딕셔너리 내 모든 요소 삭제

        a = {'name':'pey', 'phone':'0119993323', 'birth':'1128'}
        a.get('name')     # Key로 Value찾기 - a['name']과 다른 점은 get은 없는 Key를 넣을 경우 오류가 아닌 None 반환
        a.get('foo', 'bar')     # 없는 값의 경우 설정한 디폴트값(뒤에 있는 요소)이 반환됨

        'name' in a      # 딕셔너리 안에 해당 Key가 있는지 확인
        
  순서가 정해져있지 않아 인덱스를 활용할 수 없다.

# 집합 자료형

  1. 중복을 허용하지않는다.
  
  2. 순서가 정해져 있지 않다.
  
  따라서 list와 tuble과 함께 많이 사용됨(중복 없애고 순서대로 정렬가능)
    
        s1 = set([1, 2, 3])
        l1 = list(s1)
        t1 = tuble(s1)
    
  ● 집합 자료형 활용 방법

    1. 교집합
  
        s1 = set([1, 2, 3, 4, 5, 6])
        s2 = set([4, 5, 6, 7, 8, 9])
        s1 & s2
    
    2. 합집합
  
        s1 | s2
    
    3. 차집합
  
        s1 - s2
        s1.difference(s2)
    
  ● 집합 자료형 관련 함수
 
        1. add (값 1개 추가하기)
    
            s1 = set([1, 2, 3])
            s1.add(4)
    
        2. update (여러개 추가하기)
  
            s1 = set([1, 2, 3])
            s1.update([4, 5, 6])
    
        3. remove (특정값 제거하기)

            s1 = set([1, 2, 3])
            s1.remove(2)

# 자료형의 값을 저장하는 공간, 변수

C나 JAVA처럼 변수의 자료형 작성 필요 없음.

변수란 객체를 가르키는 것으로 파이썬에서는 모든 것이 객체로 이루어져 있다. 일반적인 숫자조차 정수형 객체임.

객체를 가르키는 변수의 개수를 참조 개수라고 한다.

  ● 변수 생성
  
        a, b = ('Python', 'Life')
        (a, b) = ('Python', 'Life') # 괄호 생략 가능
        [a, b] = ['Python', 'Life']

        a=3
        b=5
        a,b = b,a # 쉽게 변수끼리 변경 가능

  ● 변수 제거
  
        del.(a) #Reference count가 0이되면 객체도 없어짐.
        del.(b)

  ● 리스트를 변수에 복사하고자 할때
  
        a = [1, 2, 3]
        b = a
        a[1] = 4     # 같은 객체를 가르키기 때문에 a의 요소를 변경하면 b도 영향을 받음.
        
        1. [:] 이용 
            
            a = [1, 2, 3]
            b = a[:]
            a[1] = 4     #이러면 같은 객체를 가르키는 게 아니라 복사가 되었기 때문에 다른 값을 가짐. 

        2. copy 이용
            
            from copy import copy
            b = copy(a)    # 이경우도 서로 다른 객체를 가르키게 됨.
            
# if문

  ● 기본 구조
  
        if 조건문:
            수행할 문장1
            수행할 문장2
    
        else:
            수행할 문장A
            수행할 문장B
            
        money = 1
        if money:
            print("택시를 타고 가라")
        else:
            print("걸어 가라")
            
들여쓰기에 주의해야함. Tab과 Space 혼용해서 사용하지 말자. 콜론(:) 잊지 말자.

아무것도 사용하고 싶지 않을때는 수행 문장에 pass 사용

연산자 생략

  ● elif 구조
  
        if 조건문:
            수행할 문장1
            수행할 문장2
    
        elif:
            수행할 문장A
            수행할 문장B
            
        else:
            수행할 문장3
            수행할 문장4
            
# while문

  ● 기본 구조
  
        while 조건문:
            수행할 문장1
            수행할 문장2
            수행할 문장3
            
        while treeHit < 10:
            treeHit = treeHit +1
            print("나무를 %d번 찍었습니다." % treeHit)
            if treeHit == 10:
                print("나무 넘어갑니다.")
            
  ● 강제로 빠져나가고 싶을때는 break 사용

        coffee = 10
        money = 300
        while money:
            print("돈을 받았으니 커피를 줍니다.")
            coffee = coffee -1
            print("남은 커피의 양은 %d개입니다." % coffee)
            if not coffee:
                print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
                break

continue를 활용해서 while문 시작으로 다시 돌아갈수 있음.
                
  ● 무한루프

        while True:
            수행할 문장
            
# for문

  ● 기본 구조
  
        for 변수 in 리스트(또는 튜플, 문자열):
            수행할 문장1
            수행할 문장2
        
        test_list = ['one', 'two', 'three']
        for i in test_list:
            print(i)
            
  ● 응용
  
        marks = [90, 25, 67, 45, 80]
        number = 0
        for mark in marks:
            number += 1
            if mark >= 60:
                print("%d번 학생은 합격입니다." % number)
            else:
                print("%d번 학생은 불합격입니다." % number)
                
continue를 활용해서 for문 시작으로 다시 돌아갈수 있음.

  ● range 함수

        a = range(10)
        a = range(1,11)   #끝 숫자는 포함하지 않음
        
  ● range 함수를 활용한 구구단

        for i in range(2,10):
            print("=====%d단======" % i)
            for j in range(1,10):
                print("{0}단 : {1} * {2} = {3}".format(i, i, j, i*j))
            print('\n')
            
  ● for문에 list 활용

        [표현식 for 항목 in 반복가능객체 if 조건]
    
        짝수에 3 곱하기
            a = [1, 2, 3, 4]
            result = [num * 3 for num in a if num % 2 == 0]            

# 함수

        def 함수명(입력 인수):
            수행할 문장1
            수행할 문장2

# 사용자 입력과 출력

  ● input
    
        text = input("명언을 입력하세요 >>>>>")
    
  ● print

        1. 큰따옴표(")로 둘러싸인 문자열은 + 연산과 동일하다
        2. 문자열 띄어쓰기는 콤마로 한다        
        3. 한 줄에 결과값 출력하기 - print(x, end=' ')
        
# 파일 읽고 쓰기

  ● 파일 생성하고 출력값 적기
    
        f = open("D:/python/새파일.txt", 'w')
        for i in range(1, 11)
            data = "%d번째 줄입니다.\n" % i
            f.write(data)
        f.close()
    
    
  ● 저장된 파일 읽기
        
      1. readline() - 한줄 출력
        
        f = open("C:/Python/새파일.txt", 'r')
        while True:
            line = f.readline()
            if not line: break
            print(line)
        f.close()
        
      2. readlines() # list 라인으로 출력
        
        f = open("C:/Python/새파일.txt", 'r')
        while True:
        line = f.readlines()
        for line in lines:
            print(line)
        f.close()
        
      3. read 함수 이용하기
        
        f = open("C:/Python/새파일.txt", 'r')
        data = f.read()
        print(data)
        f.close()
        
  ● 파일에 새로운 내용 추가하기

        f = open("C:/Python/새파일.txt",'a')
        for i in range(11, 20):
            data = "%d번째 줄입니다.\n" % i
            f.write(data)
        f.close()
  
  ● with문과 사용
    
        with open("foo.txt", "w") as f:
        f.write("Life is too short, you need python")

# 클래스

  ● 클래스 기본

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

  ● 사칙연산 계산기

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

  ● 상속

        class MoreFourCal(FourCal):
            def pow(self):
                result = self.first ** self.second
                return result

        a = MoreFourCal(4, 2)
        print(a.pow())
  상속은 MoreFourCal 클래스처럼 기존 클래스(FourCal)는 그대로 놔둔채로 클래스의 기능을 확장시키고자 할 때 주로 사용

  ● 오버라이딩

        class SafeFourCal(FourCal):
            def div(self):
                if self.second == 0:
                    return 0
                else:
                    result = self.first / self.second
                    return result

        a = SafeFourCal(4, 0)
        print(a.div())
  부모 클래스(상속한 클래스)에 있는 메서드를 동일한 이름으로 다시 만드는 것을 메서드 오버라이딩(Overriding, 덮어쓰기)이라고 한다. 이렇게 메서드를     오버라이딩하면 부모 클래스의 메서드 대신 오버라이딩한 메서드가 호출된다.
