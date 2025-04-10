'''
if문과 함께 if-else문을 사용할 수 있으며,
if문의 조건이 거짓일 경우 if문의 Body 전체가 스킵되는 것에 반해서
if-else문에서는 if문의 조건이 거짓일 경우에는 else의 Body가 실행된다.

또한, else는 반드시 if가 위에 있어야만 사용할 수 있다.
'''

a = 100

if a < 10 :
  print("a is smaller than 10!")
  print("Yamu")

else :
  print("a is bigger or equal to 10")
  print("Jini")

print("Wow!")
