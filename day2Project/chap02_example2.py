#chap02_example2.py
# 복습문제 2
'''
키보드로 값을 입력받아 요구조건대로 처리하고 출력되게 코드를 작성
기본값을 가진 변수 생성 할당해 둠
    total_point = 12500
입력내용 :
고객이름 : 황지니 (custom_name : str)
결제 금액 : 3000000 (price : int)
처리내용 :
    결제금액의 5 %를 포인트(poing : float)로 처리
    계산된 포인트를 누적포인트(total_point)에 증가 연산 처리함
출력내용 :
    황지니 고객님의 사용금액은 3000000 원, 발생 포인트는 15000
    현재 이용하실 수 있는 누적포인트는 27500 점입니다.
'''
total_point =12500
custom_name = str(input('고객이름 :'))
price = int(input('결제 금액 :'))
point = price * 0.05
total_point += point
# f-string 포매팅 사용
print(f'{custom_name}고객님의 사용금액은 {price}원, 발생 포인트는 {int(point)}')
# format()사용
print('현재 이용 하실수 있는 누적포인트는 {} 점입니다.'.format(total_point))