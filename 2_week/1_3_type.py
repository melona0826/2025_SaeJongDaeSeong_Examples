'''
Python의 경우 Dynamic Typing을 사용하기 때문에 추후에 코드에서 변수의 type이
무엇인지 모를 때가 존재한다.
이때는 type 함수를 이용하여 판별할 수 있으며,
type(type을알고싶은변수이름)
형식으로 사용할 수 있다.
'''

# Integer type variable initialized with positive integer
val1 = 10
print("val1 :", val1)
print("type(val1) :", type(val1))

# Integer type variable initialized with negative integer
val2 = -10
print("val2 :", val2)
print("type(val2) :", type(val2))

# Float type variable initialized with positive float
val3 = 10.5
print("val3 :",val3)
print("type(val3) :", type(val3))

# Float type variable initialized with negative float
val4 = -10.5
print("val4 :",val4)
print("type(val4) :", type(val4))

# String type variable initialized with one character
val5 = 'a'
print("val5 :",val5)
print("type(val5) :", type(val5))

# String type variable initialized with many characters
val6 = "Testing"
print("val6 :",val6)
print("type(val6) :", type(val6))
