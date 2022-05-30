# chap06_format.py
# 문자열에 포맷(format) 적용해서 코드 작성 방법

#문장(문자열)에 여러 종류의 값을 섞어서 적용하고자 할 떄 사용 함
# 포맷문자 이용 : %서식문자 (서식문자는 값타입에 따라 정해져 있음)
# 정수 : %d (decimal : 10진수), %o (octal : 8진수), %x(hex: 16진수
# 실수 : %f
# 문자열 : %s
# 기호 % 출력시에는 %%

pname = input('상품명 :')
pamount = int(input('갯수 : '))

print(pname, '제품을', pamount, '개 주문하였습니다', sep=' ')
print(f'{pname} 제품을 {pamount}개 주문 하였습니다.')
print('%s 제품을 %d 개 주문하였습니다.' %(pname, pamount))
print('{} 제품을 {} 개 주문하였습니다.'.format(pname,pamount))

# format() 사용시 값 적용 순서를 조정할 수도 있음
st1 = '이름은 {1}이고, 나이는 {2}세이고 혈액형은 {0}형입니다.'.format('B', '홍길동', 27)
print(st1)

# format() 안에서 값에 이름을 지정할 수 있음
# 문장 안에 순번이 아닌 {이름}을 적용할 수도 있음
st2 = 'Today is {today}. Tomorrow is {tomorrow}.'.format(today='Monday', tomorrow='Tuseday')
print(st2)

# 출력시 출력칸수 지정이나, 소숫점 아래 자릿수 지정도 가능함
print('나누기 결과 : {}, {}'.format((1/3), (1//3)))
print('나누기 결과 : {:0.3f}'.format((1/3)))
print('나누기 결과 : {:f}'.format((1/3)))

print(('|{:10}|{:5.2f}|'.format(7, 12.345)))
print(('|%10d|%5.2f|' %(7, 12.345)))
print(('|%-10d|%5.2f|' %(7, 12.345)))