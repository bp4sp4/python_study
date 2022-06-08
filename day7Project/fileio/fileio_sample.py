# file path : fileio\\ fileio_sample.py
# module name : fileio.fileio_sample
#
# 파이선에서의 파일입출력 처리
# open() --> write() or read() --> close()
#
# 파일변수 = open('디렉토리명\\파일명.확장자', '열기모드')
# 파일 입출력의 기본은 텍스트(문자) 파일 입출력임
# 열기모드 w,x : 새로 쓰기
# w(wt) : 대상파일이 없으면 파일을 자동으로 새로 만듦
#         대상파일이 있으면 기존 내용을 지우고 새로쓰기 상태로 엶
# x(xt) : 대상파일이 있으면 에러 발생남
# r(rt) 읽기전용
# a(at) : 추가 쓰기
#   대상파일이 없으면 w처럼 파일을 새로 만듦
#   대상파일이 있으면 기존 내요을 그래도 두고 열림
#   기본적으로 기존 내용 뒤에 추가쓰기됨
#
# 파일 새로 만들고 값 기록 저장하기
import os

def test_fwrite():
    f = open('testa.txt', 'w') # 기본경로는 프로젝트 폴더 아래에 저장됨
    f.write('test file write')
    f.write('1234')
    #f.write('문자형 저장 확인') # 텍스트 파일 인코딩이 'ms949' 문자셋임
   # f.write('★★★★★★★★★★★') # 한글과 기호문자는 깨짐
    f.close()

# os 모듈을 활용해서 현재 디렉토리 경로를 확인할 수 있음
print(os.getcwd()) # cwd( current working directory : 현재 작업 디렉토리) # 프로젝트까지의 경로만 확인됨

# 원하는 디렉토리(폴더)에 파일을 만들려면

def test_fwrite2():
    # 파일 열기할 때 유니코드 문자 인코딩으로 지정할 수 있음
    # f = open('C:\\python_workspace\\day7Project\\fileio\\testb.txt', 'w', encoding='utf-8')
    # f = open('C:\\python_workspace\\day7Project\\fileio\\testb.txt', 'x', encoding='utf-8')
    # x 모드 : 대상파일이 존재하면 FileExistsError 에러 발생
    f = open('C:\\python_workspace\\day7Project\\fileio\\testc.txt', 'x', encoding='utf-8')
    # x 모드 : 대상파일이 없으면 자동으로 새로 만들어짐
    f.write('file path open test\n') # \n(new line) : 줄바꿈 처리
    f.write('경로를 포함해서 파일 지정 확인.\n')
    f.write('2022 년 6월 7일 화요일')
    f.close()

# a 모드 : append (추가 쓰기) 모드
# 대상파일이 존재하지 않으면 , w 와 x 모드와 동일함(자동으로 파일생성)
# 대상파일이 존재하면, 기존 내용을 그대로 두고 열림 (w 와 다른점)
# 기존 내용 아래에 새로운 내용을 추가함
def test_fwrite3():
    f = open('testd.txt', 'a', encoding='utf-8')
    f.write('file content append test\n')
    f.write('파일의 기존 내용 뒤에 추가쓰기 확인.\n')
    f.close()

# 파이선에서 파일이나 디렉토리 다루기
# os 모듈이 제공하는 함수 사용함
import os
def test_osmodule():
    # 컴퓨터의 사용자계정(컴퓨터이름) 조회
    print(os.getlogin())
    #현재 작업 디렉토리 조회
    print(os.getcwd())

    system_user = os.getlogin()
    # 디렉토리 만들기 : os.mkdir('만들 디렉토리경로와 이름')
    work_dir = ('C:\\Users\\' + system_user + '\\Desktop\\python')
    # os.mkdir(work_dir) # 주의 : 같은 이름의 디렉토리 있으면 에러남
    # 작업 디렉토리 변경하기 : os.chdir(변경할 디렉토리)
    os.chdir(work_dir)
    # 현재 작업 디렉토리 확인
    print(os.getcwd())
    
    # 변경한 디렉토리에 파일 저장
    f = open('sample.txt', 'w', encoding='utf-8')
    f.write('파이선으로 디렉토리 만들고, 만든 디렉토리로 작업폴더 변경\n')
    st ='''하고 파일 만들어
    내용 기록 저장 확인 '''
    f.write(st)
    f.close()

# 리스트, 튜플, 셋 에 저장한 데이터들은 파일에 저장
def test_writelines():
    tp = ('a', 'b', 'c')
    ls = ['r', 'e', 'd']
    f = open('list.txt', 'w')
    f.writelines(tp)
    f.write('\n')
    f.writelines(ls)
    # 각 요소별로 한 줄씩 기록을 원하면, write() 르 반복 실행하면 됨
    # f.write(ls) #write() 는 str 만 사용할 수 있음 리스트 사용 못 함
    for data in ls:
        f.write(str(data)) # 문자형이 아닌 요소는 str() 사용함
        f.write("\n")
    f.close()

# r (read) 모드 : 읽기 모드
# 주의사항 : 대상파일이 존재하지 않으면 에러 발생함
# read() : 파일 전체를 한번에 읽음
# readlines() : 파일 안에 내용을 한 줄씩 읽음
#       마지막 라인 읽고나서 더이상 읽을 라인이 없으면 None 리턴
# readlines() : 파일의 내용을 읽어와서 리스트로 반환

def test_fread():
    print(os.getcwd())
    f = open('sample.txt', 'r', encoding='utf-8')
    # print(f.read())
    # print(f.read()) # 파일은 내용을 한번에 다 읽음

    # 파일의 내용을 한 줄씩 읽도록 처리한다면
    # 파일 안의 읽어야할 줄 수를 정하지 못하므로
    # while 문 사용함. 읽기를 종료하기 위한 if 문이 필요함
    # print(f.readline())
    while True:
        line = f.readline()
        if not line: # line 변수의 값이 False가 아니면, None 이면)
            break
        print(line, end='')

def test_fread2():
    print(os.getcwd())
    f = open('sample.txt', 'r', encoding='utf-8')

    flist = f.readlines()
    print(flist)
    f.close()


# ------------------------------------
# 파이선 파일 입출력은 기본 텍스트 파일 입출력임
# 텍스트가 아닌 다른 종류의 데이터를 저장하려면 pickle 모듈 활용함
# 바이너리(이진 : binary) 형식의 파일로 저장해야 함
# 바이너리 모드 : wb, rb , ab 사용함
import pickle

def test_binary_fio():
    data = {1: 'python', 2: 'you need'}
    f = open('bintest.dat', 'wb')
    pickle.dump(data, f) # 파일에 딕셔너리 객체가 이진테이터로 기록됨
    f.close()

def test_binary_fio2():
    f = open('bintest.dat', 'rb')
    read_data = pickle.load(f)
    f.close()
    print(read_data)
    print(type(read_data)) # wb는 기록매체 타입 그래도 기록함

# 표준 입출력을 파일 대상으로 변경할 수 있음
# 표준 입력 : 키보드 입력(컴퓨터 기본 입력장치임), sys.stdin 표현
# 표준 출력 : 모니터 출력 (컴퓨터 기본 출력장치임) sys.stdout 표현

import sys
def change_stdinot():
    # 시스템 표준출력을 따로 변수에 저장 (원래 상태로 되돌리기 위함)
    stdout = sys.stdout

    f = open('test.txt', 'w', encoding='utf-8')
    sys.stdout = f
    print('표준출력이 사용하는 print 함수로 파일에 저장함')
    f.close()

    sys.stdout = stdout
    print('모니터 출력 확인')
# os 모듈의 함수 사용
# 디렉토리 만들기 : mkdir(), 디렉토리 변경하기 : chdir()
# 사용자계정 조회 : getlogin(), 현재 작업 디렉토리 조회 : getcwd()
# 시스템의 환경변수, 디렉토리, 파일 다를 때 주로 이용
def test_os():
    # listdir() : 해당 디렉토리 안의 파일과 하위 디렉토리 목록 조회
    print(os.listdir('.')) # '.' : 현재 디렉토리를 의미함
    print(os.listdir('../')) # ',.' : 상위 디렉토리를 의미함
    
    # rename() : 디렉토리나 파일의 이름바꾸기함
    # os.rename('sample.txt', 'sampdata.txt')
    # print(os.listdir('.'))

    # path.exists() : 파일이나 디렉토리의 존재 여부 확인
    print(os.path.exists('sample.txt')) # 파일이 없으면 False
    print(os.path.exists('sampdata.txt')) # 파일이 있으면 True
# # path.abspath() : 파일이나 디렉토리의 절대경로 조회
#     print(os.path.abspath('sampdata.txt'))
#
#     f = open(os.path.abspath('sampdata.txt'), 'a', encoding='utf-8')
#     f.write(os.path.abspath('sampdata.txt'))
#     f.close()
    # path.basename(), dirname(), split() : 파일명과 경로명을 분리
    current_path = os.path.abspath('sampdata.txt')
    print('current_path : ', current_path)
    print('basename :', os.path.basename(current_path)) # 파일명, 확장자 분리
    print('dirname :', os.path.dirname(current_path)) # 디렉토리명 분리
    print('split :', os.path.split(current_path)) #('디렉토리명', '파일명') 분리
    
    # path.splitdrive(), splittext() : 경로의 드라이브명, 파일의 확장자 분리
    print(os.path.splitdrive(current_path))
    print(os.path.splitext(current_path))
