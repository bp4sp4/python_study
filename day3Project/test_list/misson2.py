# mission2.py
# 리스트 실습문제 2

"""
키보드로 값들을 입력받아, 요구대로 처리하고 확인 출력 코드를 작성하시오.

입력 내용 :
    국어 점수 : 78.5 (kor : float)
    영어 점수 : 88.7 (eng: float)
    수학 점수 : 93.5 (mat : float)

처리 내용 :
    3명의 학생 점수를 입력 받음, 각 학생의 총점과 평균은 각각 계산함
    학생별 점수는 각 리스트에 저장한 다음, [국어, 영어, 수학, 총점, 평균]
    각 학생 점수를 리스트(sungjuk_list)에 순서대로 저장 처리함
    [[국, 영, 수, 총, 평], [국, 영, 수, 총, 평], [국, 영, 수, 총, 평]]
    3명의 점수의 총합(total_score : int)과 전체평균(average_score : float)를
    계산하시오.

출력 내용 :
    리스트에 저장된 값들을 출력함
    국, 영, 수, 총, 평균 순서로 출력
    -> 점수는 소수점아래 둘째자리까지 표시
    -> format() 사용함
    전체 총점과 전체 평균을 출력하시오.
"""
sungjuk_list = []
total_score = 0
average_score = 0.0

# 첫번째
scores1 = []
scores1.append(float(input('국어 점수 : ')))
scores1.append(float(input('영어 점수 : ')))
scores1.append(float(input('수학 점수 : ')))
scores1.append(scores1[0] + scores1[1] + scores1[2])
scores1.append(scores1[3] / 3.0)

sungjuk_list.append(scores1)
total_score += int(scores1[3])

# 두번째
scores2 = []
scores2.append(float(input('국어 점수 : ')))
scores2.append(float(input('영어 점수 : ')))
scores2.append(float(input('수학 점수 : ')))
scores2.append(scores2[0] + scores2[1] + scores2[2])
scores2.append(scores2[3] / 3.0)

sungjuk_list.append(scores2)
total_score += int(scores2[3])

# 세번째
scores3 = []
scores3.append(float(input('국어 점수 : ')))
scores3.append(float(input('영어 점수 : ')))
scores3.append(float(input('수학 점수 : ')))
scores3.append(scores3[0] + scores3[1] + scores3[2])
scores3.append(scores3[3] / 3.0)

sungjuk_list.append(scores3)
total_score += int(scores3[3])

# 전체 평균 계산
average_score = total_score / 9.0  # 3과목 * 3명

print('|%7.2f|%7.2f|%7.2f|%7.2f|%7.2f|' %(sungjuk_list[0][0], sungjuk_list[0][1], \
            sungjuk_list[0][2], sungjuk_list[0][3], sungjuk_list[0][4]))
print('|%7.2f|%7.2f|%7.2f|%7.2f|%7.2f|' %(sungjuk_list[1][0], sungjuk_list[1][1], \
            sungjuk_list[1][2], sungjuk_list[1][3], sungjuk_list[1][4]))
print('|%7.2f|%7.2f|%7.2f|%7.2f|%7.2f|' %(sungjuk_list[2][0], sungjuk_list[2][1], \
            sungjuk_list[2][2], sungjuk_list[2][3], sungjuk_list[2][4]))
print('전체 총점 : {:10}, 전체 평균 : {:10.2f}'.format(total_score, average_score))
