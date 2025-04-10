'''
List 선언
List의 선언은 아래와 같이 리스트이름 = [값, 값, 값] 의 형식으로 선언한다.
List를 선언할 때는 이처럼 값들을 콤마(,)로 구분하며 대괄호 안에 넣어야한다.
'''
val = [1, 2, 3, 5, 6]
print("val :", val)

'''
List에서 특정한 Index의 값을 사용하려면 아래처럼
리스트이름[특정한Index] 형식으로 사용한다.
Index의 경우 0부터 시작한다.
'''
# 0번째 Index (1) 출력
print("val[0] :", val[0])

# -1번째 Index는 마지막 Index (6)를 의미하며 -2, -3 등도 가능하다.
print("val[-1] :", val[-1])

# 0번째부터 2번째 Index까지의 값들을 출력
# Slicing 이라고 불리며 다양한 기법들은 GPT나 구글을 참고
print("val[:3] :", val[:3])


'''
아래와 같은 문자열은 한 글자씩이 배열된 리스트로 취급되며,
아래처럼 문자열을 변수에 담을 경우 리스트처럼 사용할 수 있다.
'''
stringVal = "yamujini"
print("stringVal :", stringVal)

print("stringVal[3] :", stringVal[3])

print("stringVal[:3] :",stringVal[:3])
