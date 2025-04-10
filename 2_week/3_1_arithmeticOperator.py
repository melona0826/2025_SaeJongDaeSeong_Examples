print("[Arithemtic Operator with Number]")
val1 = 3
val2 = 6

print("val1 : " , val1 , " val2 : ", val2)

# Plus Operator
print("val1 + val2 : ", val1 + val2)

# Subtract Operator
print("val1 - val2 : ", val1 - val2)

# Multiplication Operator
print("val1 * val2 : ", val1 * val2)

# Power Operator
print("val1 ** 3 : ", val1 ** 3)

# Divide Operator
print("val1 / val2 : ", val1 / val2)

# Modulo Operator
print("val1 % val2 : ", val1 % val2)

# 아래처럼 Python에서도 괄호를 우선적으로 계산한다.
print("(10 + 3) * 3 : ", (10 + 3) * 3)

'''
숫자가 아닌 다른 자료형에서 산술연산을 진행할 경우 자료형과 산술연산의 종류에 따라서
결과가 달라진다.
아래의 문자열 (str)의 경우 덧셈은 문자열간의 결합을 결과값으로 반환한다.
(String Concatenation)
또한, 문자열 (str) * 정수 (int)의 경우 문자열을 정수만큼 결합한 문자열을 결과값으로
반환한다.
'''
print()
print("[Arithmetic Operator with str]")

# Str Concatenation
val1 = "Hello"
val2 = "World"
print("val1 : " , val1 , " val2 : ", val2)
print("val1 + val2 : ", val1 + val2)

# Str Concatenation
val1 = "Hello"
val2 = "   World"
print("val1 : " , val1 , " val2 : ", val2)
print("val1 + val2 : ", val1 + val2)

# Str Multiply
val1 = "Hello"
print("val1 : " , val1 )
print("val1 * 3 : ", val1 * 3)


'''
Boolean Type에서는 True는 1, False는 0으로 계산되어 산술연산이 진행된다.
'''
print()
print("[Arithmetic Operator with bool]")

val1 = True
val2 = False

print("val1 : " , val1 , " val2 : ", val2)

print("val1 + val2 : ", val1 + val2)

print("val1 - val2 : ", val1 - val2)

print("val1 * val2 : ", val1 * val2)

print("val1 ** val2 : ", val1 ** val2)
