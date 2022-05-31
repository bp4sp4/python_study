# list_review.py
# list 자료형 복습문제

'''
키보드로 값을 입력받고 요구대로 처리한 다음 출력 확인하시오
입력내용 :
    번호 : 12 (sno : int)
    이름 : 황지니(sname : str)
    국어 : 85 (kor:int)
    영어 : 85 (eng : int)
    수학 : 85 (mat : int)

처리 내용
    입력받은 값들을 리스트(sungjuck_list)에 저장하시오
    index 0 : sno, index 1 : sanme, index 2 :kor, index 3 : eng,
    index 4 : mat
    index 5 : 3과목의 총점(int)
    index 6 : 3과목의 평균(float)

출력내용 : format() 사용함
    12번 황지니의 총점은 255점, 평균은 85.0점
    국어 : 85점, 영어 85점, 수학: 85점 입니다.

'''
def func():
      sno = int(input('번호 :'))
      sname = str(input('이름 :'))
      kor = int(input('국어 :'))
      eng = int(input('영어 :'))
      mat = int(input('수학 :'))
      tot = int(kor+eng+mat)
      avg = float(tot/3)

      sungjuck_list= [sno, sname, kor, eng, mat, tot, avg]

      print('{}번 {}의 총점은 {}점, 평균은 {}점'.format(sungjuck_list[0],sungjuck_list[1],sungjuck_list[5],sungjuck_list[6]))
      print('국어 : {}점 , 영어 : {}, 수학 : {}점 입니다.'.format(sungjuck_list[2],sungjuck_list[3],sungjuck_list[4]))