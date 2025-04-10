'''
아래와 같이
int(input(원하는메세지))
의 형식으로 사용자로부터 입력을 받을 수 있다.
input(원하는메세지) 함수를 이용하여서 사용자로부터 입력을 받아올 수 있으며,
받아진 입력값은 모두 str type으로 받아지게된다.

본 예제에서는 짝수 판별을 위해 정수 type으로 변환이 필요하기에 int()를 이용하여
str type을 int type으로 변환하였다.

또한, 아래처럼 print를 위해 str()을 이용해 str type으로 변환해서 사용하기도
한다.
'''
val = int(input("Type the number!\n"))

if(val % 2) :
  print(str(val) + " is Odd Number!")

else :
  print(str(val) + " is Even Number!")
