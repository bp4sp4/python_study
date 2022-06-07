# file path : fileio\\ fileio_sample.py
# module name : fileio.fileio_sample

# 파이선에서의 파일입출력 처리
# open() --> write() or read() --> close()

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