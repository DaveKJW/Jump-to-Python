# Jump-to-Python
●문자열 자료형

●문자열 인덱싱, 슬라이싱

    a = "20180122Cloudy"
    year = a[:4]
    day = a[4:8]
    weather = a[8:]
    print("Year : " + year + "\n" + "Day : " + day + "\n" + "Weather : " + weather)

●문자열 포맷팅, 고급포맷팅

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

●문자열 관련 함수

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

●리스트 자료형

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

●리스트 관련 함수

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

●튜플 자료형

    t1 = ()
    t2 = (1,)    # 요소가 1개일때는 ',' 반드시 붙여야함.
    t3 = (1, 2, 3)
    t4 = 1, 2, 3    # 튜플은 괄호 생략 가능
    t5 = 1, 2, "hello", 4          # 자료형 구분 없이 선언가능
    t6 = 1, 2, (3, 4, 5), 6, 7     # 튜플 안에 튜플 넣는 것 가능

# 튜플은 추가, 변경, 삭제가 안됨.
