# misson\dict_review2.py
# dict 자료형 복습문제 2

'''
키보드로 값들을 입력받아, 요구대로 처리하고 확인 출력 코드를 작성하시오
입력 내용 :
    번호 : 12 (sno :int)
    이름 : 황지니 (sname : str)
    국어 : 85 (kor :int)
    영어 : 85 (eng :int)
    수학 : 85 (mat : int)

처리 내용 :
    입력받은 값들은 사전(sungjuk_dict)에 저장 처리함
    키는 위의 변수이름을 문자형으로 사용하시오.
    3과목의 총점 (tot : int) 과 3과목의 평균 (avg : float) 사전에 추가하시오.

출력 내용 :
    12번 황지니의 총점은 255점, 평균은 85.0점
    국어 : 85점, 영어 : 85점, 수학 : 85점
    -> 점수는 소수점아래 둘째자리까지 표시
    -> format() 사용함
'''

# def dictfunc():
#     s_no = int(input('번호 :'))
#     s_name = str(input('이름 :'))
#     kor = int(input('국어 :'))
#     eng = int(input('영어 :'))
#     mat = int(input('수학 :'))
#
#     tot = int(kor+eng+mat)
#     avg = float(tot/3)
#
#     sungjuck_dict = {
#         's_no' : s_no,
#         's_name' : s_name,
#         'kor' : kor,
#         'eng' : eng,
#         'mat' : mat,
#         'tot' : tot,
#         'avg' : avg
#     }
#     print('{}번 {}의 총점은 {}점, 평균은 {}점'.format(sungjuck_dict['s_no'],sungjuck_dict['s_name'],sungjuck_dict['tot'],sungjuck_dict['avg']))
#     print('국어 : {}점, 영어 : {}점, 수학 : {}점입니다.'.format(sungjuck_dict['kor'],sungjuck_dict['eng'],sungjuck_dict['mat']))
# dict 저장 방식을 변경해 보시오.
# 학생번호를 키로 사용하고, 나머지 학생정보를 리스트로 만들어서
# 번호 : [이름, 국어 , 영어, 수학, 총점, 평균]
# sungjuck_dict 에 저장한 다음 출력하시오.
def dictfunc2():
    s_no = int(input('번호 :'))
    s_name = str(input('이름 :'))
    kor = int(input('국어 :'))
    eng = int(input('영어 :'))
    mat = int(input('수학 :'))

    tot = int(kor+eng+mat)
    avg = float(tot/3)

    sungjuk_dict = {s_no : [s_name,kor,eng,mat,tot,avg]}
    print('{}번 {}의 총점은 {}점, 평균은 {}점'.format(s_no, sungjuk_dict[s_no][0], sungjuk_dict[s_no][4],sungjuk_dict[s_no][5]))
    print('국어 : {}점, 영어 : {}점, 수학 : {}점입니다.'.format(sungjuk_dict[s_no][1],sungjuk_dict[s_no][2],sungjuk_dict[s_no][3]))