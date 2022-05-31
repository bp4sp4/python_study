# misson1.py
# 리스트 실습문제

'''
키보드로 값들을 입력받아, 요구대로 처리하고 확인 출력 코드를 작성
입력내용 학생이름 : 홍길동(name :str)
        학년 : 2 (grade : int)
        반 : 3 (s_class : int)
        번호 : 12 (s_no : int)
        점수 87.5 (score : float)
처리내용 :
입력받은 값들을 리스트 (student_list)에 순서대로 저장 처리함
출력내용 :
     리스트에 저장된 값들을 출력함
    2학년 3반 12번 홍길동의 점수는 87.50 점입니다
    -> 점수는 소수점아래 둘째자리 까지 표시
    -> format()사용함
'''
# 방법 1
# name = str(input('학생이름 :'))
# grade = int(input('학년 :'))
# s_class = int(input('반 :'))
# s_no = int(input('번호 :'))
# score = float(input('점수 :'))
#
# student_list = [name, grade, s_class, s_no, score]
#
# print('{}학년 {}반 {}번 {}의 점수는{:0.2f}점입니다.'.format(student_list[1],student_list[2],student_list[3],student_list[0], student_list[4]))
# 방법 2
# name = str(input('학생이름 :'))
# grade = int(input('학년 :'))
# s_class = int(input('반 :'))
# s_no = int(input('번호 :'))
# score = float(input('점수 :'))
#
# student_list = []
# student_list.append(name)
# student_list.append(grade)
# student_list.append(s_class)
# student_list.append(s_no)
# student_list.append(score)
#
# print('{}학년{}반{}번{}의 점수는{:0.2f}점입니다.'.format(student_list[1],student_list[2],student_list[3],student_list[0], student_list[4]))
#방법 2의 코드 줄이기


student_list = []
student_list.append(input('학생이름:'))
student_list.append(int(input('학년 :')))
student_list.append(int(input('반 :')))
student_list.append(int(input('번호 :')))
student_list.append(float(input('점수 :')))

print('{}학년 {}반 {}번 {}의 점수는{:0.2f}점입니다.'.format(student_list[1],student_list[2],student_list[3],student_list[0], student_list[4]))




