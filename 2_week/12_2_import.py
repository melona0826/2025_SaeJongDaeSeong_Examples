'''
import를 이용하여 다른 파일을 참조해 다른 파일의 함수를 사용할 수 있다.
import 파일명 (.py 생략)
의 형태로 사용한다.

import 이후에
파일명.함수이름
형태로 참조한 파일의 함수를 사용할 수 있다.

다만, import를 이용해 참조할 경우 참조하는 파일의 이름이 변수처럼 취급되기 때문에
반드시 변수이름 규칙을 따라야만 import가 가능하다.
(숫자로 시작하지 않아야하며, _ (under-bar)를 제외한 특수문자 및 공백이 없어야함)
'''

import module

print(module.yamu_equation_both(3, 3))
