'''
if-elif-else문에서 조건판별의 우선순위는
if > elif > else
이다.

만약 elif문이 여러 개 존재하는 경우에는 상단에 위치할 수록 우선순위가 높다.
'''

# if 우선
a = 10

if a > 5 :
  print("Yamu")

elif a > 3 :
  print("Jini")

else :
  print("YJR")


# 상단 elif 우선
a = 10

if a < 5 :
  print("Yamu")

elif a > 3 :
  print("Jini")

elif a > 6:
  print("YJR")


# 상단 elif 우선
a = 10

if a < 5 :
  print("Yamu")

elif a > 6 :
  print("YJR")

elif a > 3:
  print("Jini")
