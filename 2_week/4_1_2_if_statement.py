'''
If문에서 조건이 변수일 경우 변수의 값이
0이라면 거짓(False)
0이 아니라면 참(True)

0이 아니라면 참이기에 0을 제외한 모든 수 (-1, -100, -3.2 등)는 참(True)으로
취급된다.
'''
print("a == 1")
a = 1

if a :
  print("hello")
  print("YamuJini")

print("Yaho!")

print()
print("a == 0")
a = 0

if a :
  print("hello")
  print("YamuJini")

print("Yaho!")

print()
print("a == -1")
a = -1

if a :
  print("hello")
  print("YamuJini")

print("Yaho!")
