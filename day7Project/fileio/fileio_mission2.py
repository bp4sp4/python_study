# fileio_mission.py
# 파일 입출력 실습문제2


def memojang():
    prompt = '''
        파이썬 메모장이 실행되었습니다.\n
        1. 새로 만들기
        2. 저장하기
        3. 불러오기
        4. 끝내기
        '''
    while True:
        print(prompt)
        no = int(input('번호 입력 : '))

        if no == '1':
            print('내용을 입력하세요 \'--end--\' 입력시 내용 입력이 끝납니다.')
            contents = ''
            while True:
                in_str = input()
                if in_str == '--end--':
                    break
                contents += in_str + '\n'

        elif no == '2':
            fname = input('저장할 파일명 :')
            f = open(fname,'w', encoding='utf-8')
            f.write(contents)
            f.close()
            print(' {} 파일에 성공적으로 저장되었씁니다'.format(fname))

        elif no == '3':
            fname = input('열기할 파일명 :')
            f = open(fname, 'r', encoding='utf-8')
            contents = f.read()
            f.close()
            print(contents, end='')

        elif no == '4':
            break

    print('==== 메모장을 종료합니다. =====')