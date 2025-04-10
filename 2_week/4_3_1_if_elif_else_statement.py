'''
if-else 외에 if-elif-else문을 사용할 수 있다.
if의 조건이 거짓일 경우 else의 Body를 실행하는 if-else문과 다르게
if-elif-else문의 경우 if문의 조건이 거짓일 경우 상단의 elif 조건부터 판별하여
elif의 조건이 참일 경우 elif의 Body를 실행하고,
elif의 조건이 거짓일 경우에는 바로 밑의 elif의 조건을 판별한다.
만약 모든 elif의 조건이 거짓이라면 else의 Body를 실행한다.
'''

a = 100

if a < 10 :
  print("a is smaller than 10!")
  print("Yamu")

elif a < 300 :
  print("a is smaller than 300!")
  print("Yamu")

else :
  print("a is bigger or equal to 10")
  print("Jini")

print("wow!")
