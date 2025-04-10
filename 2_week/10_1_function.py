'''
함수란 특정한 처리 과정(코드)을 따로 묶어서 작은 프로그램으로 만드는 것이다.
자주 반복되는 처리 과정(코드)을 함수로 만들어 반복되는 코드를 줄이거나,
추후에도 다시 코드를 이용하기 위해서 함수를 만든다.

함수의 선언은 아래와 같이
def 함수이름(매개변수) :
  함수내용
  return 반환값

의 형태로 선언한다.
함수의 경우 매개변수와 반환값은 필수 사항이 아니며 둘 중 한 개만 존재하거나
둘 다 존재하지 않는 경우 모두 가능하다.

선언한 함수를 사용할 때는
함수이름(인자)
의 형태로 사용한다.

매개변수가 존재하지 않는 경우에는
함수이름()
형태로 사용한다.
'''
# 함수를 사용하지 않을 때
print("[No Function]")

val1 = 3
val2 = 6
val3 = 10

print(2 * val1 + val2)
print(2 * val2 + val3)
print(2 * val3 + val1)

# 함수를 사용할 때
print("[Function]")

def yamu_equation(x1, x2) :
  return 2 * x1 + x2

val1 = 3
val2 = 6
val3 = 10

print(yamu_equation(val1, val2))
print(yamu_equation(val2, val3))
print(yamu_equation(val3, val1))
