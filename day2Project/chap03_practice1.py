# chap03_practice1.py
# 문자자료형 실습 문제

# 키보드로 입력받아 요구대로 처리하고 출력
# 입력내용 :
#     회원이름 : 이순신 (member_name : str)
#     회원아이디 : leess88@ict.org (member_id : str)
#     패스워드 : pass1234 (member_passwd : str)
#     나이 : 45 (age : int)
#     키 : 187.5 (height : float)
#     출력내용 : format() 매소드 사용함
#     이순신 회원의 아이디는 leess88@ict.org 이고 암호는 pass**** 입니다
#     나이는 45세이고, 키는 187.5 입니다.
# - 출력시 처리조건 :
# 암호는 첫글자 부터 4글자만 슬라이싱 한 다음 나머지 글자수에 맞춰서 * 로 출력되게함
# 키는 소숫점아래 첫자리까지만 출력되게 포맷팅함


member_passwd = str(input('패스워드 :'))


# 암호 * 문자 출력갯수 계산
repeat_count = len(member_passwd)-1
print_pwd = member_passwd[0:7] + ('*' * repeat_count)
# print(print_pwd)
print(f' 암호는 {print_pwd}입니다.')
