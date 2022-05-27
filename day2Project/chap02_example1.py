#chap02_example.py
#복습문제 1

student_name = str(input('학생이름 :'))
student_no = int(input('학생번호 :'))
kor = int(input('국어 점수 :'))
eng = int(input('영어 점수 :'))
mat = int(input('수학 점수 :'))
tot = int(kor+eng+mat)
avg = float(tot/3)

print('{}번 {}의 과목총점은{}이고 평균은 {:0.2f}점'.format(student_no,student_name,tot,avg))