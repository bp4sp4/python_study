#chap05_list.py
# 파이선이 제공하는 list 관련 함수 테스트
lst = [1, 3.5, 'list', True, 20, ['a','b','c']]
print(f'before : {lst}')
print(f'lenth : {len(lst)}')
# append() : 리스트 뒤로 새 값 추가함
# 리스트 변수 : append(추가할값)

lst.append(456)
print(f'after :  {lst}')
print(f'lenth : {len(lst)}')

# remove() : 지정한 인덱스 위치의 데이터 제거함, 갯수 줄어듦
# 리스트변수 : remove(제거할값)

lst.remove(20)
print(f'after :  {lst}')
print(f'lenth : {len(lst)}')

# 같은 값이 여러 개 저장되어 있는 리스트인 경우
lst_1 = [1, 1, 2, 2, 1, 3]
print(f'before remove :  {lst_1}')
print(f'lenth : {len(lst_1)}')
lst_1.remove(1) # 앞에서부터 검색해서 첫번째로 만나는 해당값 삭제
print(f'after :  {lst_1}')
print(f'lenth : {len(lst_1)}')

# insert() : 리스트 안의 원하는 위치에 값을 추가함
# fltmxmqustn.insert(위치인덱스, 추가할 값)

print(f'before insert :  {lst}')
print(f'lenth : {len(lst)}')

lst.insert(1, '추가확인')
print(f'after insert :  {lst}')
print(f'lenth : {len(lst)}')

# pop() : 인덱스 위치의 값을 꺼냄(제거)
# 리스트변수.pop() : 마지막 인덱스 위치의 값 꺼냄(제거)
# 리스트변수.pop(index) : 해당 인덱스 위치의 값 꺼냄(제거)
lst.pop()
print(f'after pop:  {lst}')
print(f'lenth : {len(lst)}')
lst.pop(3)
print(f'after pop  2:  {lst}')
print(f'lenth : {len(lst)}')

# extend() : 기존 리스트 뒤쪽에 다른 리스트를 추가해서 리스트를 확장함
# 리스트변수1.extend(연장할 리스트)
lst.extend(lst_1)
lst.pop(3)
print(f'after extend:  {lst}')
print(f'lenth : {len(lst)}')

# reverse() : 리스트의 저장순서를 반대로 뒤집기함
# 리스트변수.reverse()
lst.reverse()
print(f'after reverse:  {lst}')

# sort() : 리스트의 저장값들을 오름차순정렬 처리함
# 한가지 종류의 값들로만 저장되어 있을 때 사용할 수 있음
# lst.sort() # 여러 종류의 값들은 크냐 작으냐에 대한 비교연산 못함, error

lst_int = [1, 2, 4, 6, 7, 21, 35, 100]
print('before sort : {}'.format(lst_int))
lst_int.sort() # 오름차순정렬 (작은값에서큰값 순으로)
print('after sort (ascending) : {}'.format(lst_int))
lst_int.sort(reverse=True) # 내림차순정렬 ( 큰값에서 작은값 순으로)
print('after sort (descending : {}'.format(lst_int))

lst_float = [5.3, 1.2, 1.6, 7.8, 5.9]
print('before sort : {}'.format(lst_float))
lst_float.sort() # 오름차순정렬 (작은값에서큰값 순으로)
print('after sort (ascending) : {}'.format(lst_float))
lst_float.sort(reverse=True) # 내림차순정렬 ( 큰값에서 작은값 순으로)
print('after sort (descending : {}'.format(lst_float))

lst_str = ['blue', 'yellow', 'white', 'green']
print('before sort : {}'.format(lst_str))
lst_str.sort() # 오름차순정렬 (작은값에서큰값 순으로)
print('after sort (ascending) : {}'.format(lst_str))
lst_str.sort(reverse=True) # 내림차순정렬 ( 큰값에서 작은값 순으로)
print('after sort (descending : {}'.format(lst_str))

lst_str_kr = ['자바', '파이선', 'C언어', '리액트']
print('before sort : {}'.format(lst_str_kr))
lst_str_kr.sort() # 오름차순정렬 (작은값에서큰값 순으로)
print('after sort (ascending) : {}'.format(lst_str_kr))
lst_str_kr.sort(reverse=True) # 내림차순정렬 ( 큰값에서 작은값 순으로)
print('after sort (descending : {}'.format(lst_str_kr))

# count() : 리스트에 저장된 동일한 값의 갯수 조회
# 리스트변수.count(찾을값)
print(f'lst:{lst}')
print(f'lst 에 저장된 정수 1의 갯수 조회 : {lst.count(1)}')