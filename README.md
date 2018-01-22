# Jump-to-Python

#### Day 1

●문자열 자료형

  -문자열 인덱싱, 슬라이싱

        a = "20180122Cloudy"
        year = a[:4]
        day = a[4:8]
        weather = a[8:]
        print("Year : " + year + "\n" + "Day : " + day + "\n" + "Weather : " + weather)

  -문자열 포맷팅, 고급포맷팅

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

  -문자열 관련 함수

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

●튜플 자료형

        t1 = ()
        t2 = (1,)    # 요소가 1개일때는 ',' 반드시 붙여야함.
        t3 = (1, 2, 3)
        t4 = 1, 2, 3    # 튜플은 괄호 생략 가능
        t5 = 1, 2, "hello", 4          # 자료형 구분 없이 선언가능
        t6 = 1, 2, (3, 4, 5), 6, 7     # 튜플 안에 튜플 넣는 것 가능

튜플은 추가, 변경, 삭제가 안됨.

●딕셔너리 자료형

항상 쌍으로 존재한다.
Key에는 변하지 않는 값을 사용. Value에는 변하는 값, 변하지 않는 값 모두 사용.

        dic = {'name':'pey', 'phone':'0119993323', 'birth':'1128'}
        a = {1: 'a'}
        a[2] = 'b'     
        a['name'] = 'pey'   # 딕셔너리 요소 추가

        grade = {'pey': 10, 'julliet': 99}    # Key로 Value 찾기
        grade['pey']

   Key값으로 리스트는 쓸수 없으나 튜플은 사용 가능

  딕셔너리 관련 함수

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

●집합 자료형

  1. 중복을 허용하지않는다.
  2. 순서가 정해져 있지 않다.
  따라서 list와 tuble과 함께 많이 사용됨(중복 없애고 순서대로 정렬가능)
    
        s1 = set([1, 2, 3])
        l1 = list(s1)
        t1 = tuble(s1)
    
  -집합 자료형 활용 방법

    1. 교집합
  
        s1 = set([1, 2, 3, 4, 5, 6])
        s2 = set([4, 5, 6, 7, 8, 9])
        s1 & s2
    
    2. 합집합
  
        s1 | s2
    
    3. 차집합
  
        s1 - s2
        s1.difference(s2)
    
  -집합 자료형 관련 함수
 
    1. add (값 1개 추가하기)
    
        s1 = set([1, 2, 3])
        s1.add(4)
    
    2. update (여러개 추가하기)
  
        s1 = set([1, 2, 3])
        s1.update([4, 5, 6])
    
    3. remove (특정값 제거하기)
  
        s1 = set([1, 2, 3])
        s1.remove(2)
