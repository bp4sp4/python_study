# crawling_run.py

# 동적 웹크롤링 : selenium 모듈 사용함 => 패키지 설치
# selenium 모듈은 웹브라우저와 연동해서,
# 브라우저에 입력된 웹사이트와 이 사이트의 검색영역의 검색 키워드를
# 파이썬에서 입력받아서 해당 사이트로 전송해서
# 검색 태그 영역에 값으로 적용시켜서 검색하게 함 : 원격 검색
# 검색된 결과가 브라우저에 출력 > 파이썬에서 읽어와서 분석함
# 동적 웹크롤링 동작 :
# 파이썬에서 검색 키워드 전송함 >> 브라우저 페이지에서 검색 적용
# >> 잠시 대기 >> 브라우저에 결과 출력 >> 파이썬으로 읽어옴 >> 분석

# import 방법
# import 모듈명 [as 줄임말]  => 모듈이 가진 전체 내용 임포트됨
# 모듈이 가진 일부 항목만 선택해서 임포트할 수 있음
# from 모듈명 import 선택항목명[, 선택항목, 선택항목, ....]
# 선택항목 : 함수, 클래스, 하위 모듈 등이 해당됨
from selenium import webdriver as wd
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
# 명시적 대기를 위해 (waiting 을 명시함)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Tour.TourInfo, TourModel.TourModel 임포트
from Tour import TourInfo
from TourModel import TourModel

# selenium 과 연결할 브라우저 선택 : 크롬(chrome)
# 현재 사용 중인 크롬 브라우저의 버전 확인함
# => 브라우저 우측상단 점 3개 > 도움말 > 버전정보 확인
# 웹에서 '크롬 드라이버' 검색 > 확인된 버전과 같은 드라이버 다운받음
# 압축 풀어서 압축푼 폴더 안의 exe 파일을 현재 프로젝트 폴더로 복사함

def run():
    # 드라이버 등록
    # Mac 용
    # driver = wd.Chrome(executable_path='./chromedriver')
    # 윈도우용
    driver = wd.Chrome(executable_path='./chromedriver.exe')

    # 접속할 테스트 사이트 url 연결 확인하기 --------
    main_url = 'http://tour.interpark.com/'
    # main_url = 'https://www.naver.com/'
    # main_url = 'https://news.naver.com/'
    # 해당 페이지의 검색에 전달할 검색 키워드 정하기
    keyword = '로마'
    # 검색 결과 담을 리스트
    tour_list = []
    # 사이트에 접속
    driver.get(main_url)  # 실행 확인

    # 해당 페이지의 검색창 찾아서 검색 키워드 입력되게 처리 ----
    # 검색창 태그 앨리먼트는 '개발자도구' 이용해서 찾음
    # input 태그의 id 명 : SearchGNBText
    # 파이썬에서 브라우저 페이지로 검색창에 검색할 키워드 전송함
    driver.find_element(By.ID, 'SearchGNBText').send_keys(keyword)
    # 웹페이지 검색창에 전송한 키워드 '로마'가 자동 입력됨

    # 검색 버튼 클릭 작동함
    # button 태그의 class 명 : search-btn
    driver.find_element(By.CSS_SELECTOR, 'button.search-btn').click()

    # 잠시 대기 => 검색 결과 페이지가 로드되고 (브라우저에 출력)
    # 즉각적으로 데이터를 획득하는 행위는 명시적으로(코드상으로)
    # 대기시켜야 함
    # 획득할 데이터가 발견될 때까지 대기시킴

    # 대기 방법 : 명시적 대기와 암묵적 대기 2가지 처리 가능함
    # 명시적 대기 : 요구한 앨리먼트을 찾을 때까지 대기시킴
    try:
        element = WebDriverWait(driver, 10).until(\
           # 지정한 앨리먼트 위치를 확인하면 대기 종료됨
           EC.presence_of_element_located((By.CLASS_NAME, 'boxList')))
    except Exception as msg:
        print('대기 요청 오류 : ', msg)

    # 암묵적 대기 :
    # DOM(Document Object Model : 태그 사용 계층 구조)이
    # 전부 다 브라우저에 로드될 때까지(모두 읽어들일 때까지)
    # 대기하고 먼저 로드되면 바로 요소를 찾도록 진행함
    # 요소를 찾을 시간(초)을 지정하면, 지정 시간동안
    # DOM 풀링을 지시할 수 있음
    driver.implicitly_wait(10)

    # 절대적인 대기도 설정할 수 있음
    # time.sleep(10)

    # 검색 결과 페이지에서 '해외여행' 클릭해서
    # 여행상품 게시판에 진입함
    driver.find_element(By.CSS_SELECTOR,\
            'div.sortTabInner>ul.sortTabBox>li:nth-child(4)').click()

    # '해외여행' 게시판에서 데이터 가져올 때
    # 혹시 로그인을 해서 접근되는 사이트일 때는 세션 관리 필요함
    # 데이터가 많으면 자동 로그아웃될 수 있으므로.
    # 특정 단위별로 로그아웃하고 다시 로그인하는 처리가 필요함
    # 특정 게시물이 사라지는 경우의 처리도 검토할 필요가 있음
    # => 팝업 발생 : 팝업이 없는 컨텐츠로 변경 등의 검토가 필요
    # 게시판 스캔시 => 임계점 모름!!
    # => loop 문 돌려서 일괄적으로 접근 처리 필요함 : 메타 정보 획득

    # searchModule.SetCategoryList(1, '') 자바스크립트 실행
    # 페이지가 리뉴얼되서 자바스크립트 함수 undefine 상태임
    # 1부터 16까지로 테스트해 봄 : 게시물 넘어갔을 때 현상 확인
    # for page in range(1, 16):

    # 게시판 페이지 하단의 div.pageNumBox > ul > li 태그 클릭
    # 페이지 이동해서 게시 정보 가지고 오게 함
    page_elements = driver.find_elements(By.CSS_SELECTOR,\
                            'div.pageNumBox>ul>li')
    pages = len(page_elements)
    for page in range(1, pages):
        try:
            # 자바스크립트 구동하기 예 :
            # driver.execute_script('searchModule.SetCategoryList(%s, '')' % page)

            page_elements[page - 1].click()

            time.sleep(2)
            print('%s 페이지로 이동 처리 확인' % page)
            # 실행 확인 -----------------

            #######################################
            # 검색할 공통 항목 정하기
            # 상품명, 여행기간, 가격, 썸네일이미지,
            # 링크(상품상세정보), 출발가능기간
            boxitems = driver.find_elements(By.CSS_SELECTOR\
                                , 'ul#boxList>li')
            print('상품갯수 : ', len(boxitems))

            # 해외여행 상품 하나씩 접근해서, 각 항목 값 객체 저장
            for li in boxitems:
                # 해외상품 안의 상품특성 li 태그들 추출
                # contents = li.find_elements(By.CSS_SELECTOR,\
                #     'div.boxProduct>div.productInfo div.infoTravelDetail div.content>ul>li')
                # print('contents : ', len(contents))
                #
                # # 상품특성들을 하나의 문장 만들기
                # litxt_list = []
                # for cli in contents:
                #     print('2. ', cli)
                #     litxt_list.append(cli.text)
                #
                # print('상품특성 확인 : ', litxt_list)

                # print(li.find_element(By.CSS_SELECTOR, \
                #         'div.boxProduct>div.productInfo a.infoLink>h5.infoTitle').text)

                # li 태그 안의 각 앨리먼트 값 추출 > 객체 초기화
                tour_obj = TourInfo(
                    li.find_element(By.CSS_SELECTOR, 'div.boxProduct>div.productInfo a.infoLink>h5.infoTitle').text,
                    li.find_element(By.CSS_SELECTOR, 'div.boxProduct>div.productInfo div.infoPrice strong').text,
                    li.find_element(By.CSS_SELECTOR, 'div.boxProduct>div.productImage img').get_attribute('src'),
                    li.find_element(By.CSS_SELECTOR, 'div.boxProduct>div.productInfo p.infoSubTitle').text,
                    li.find_element(By.CSS_SELECTOR, 'div.boxProduct>div.productInfo>div:nth-child(3) p.info:first-child>span').text,
                    li.find_element(By.CSS_SELECTOR, 'div.boxProduct>div.productInfo>div:nth-child(3) p.info:nth-child(2)').text,
                    '')
                print('객체 값 확인 : ', tour_obj)
                # TourInfo 안의 __str__ 자동 실행됨
                tour_list.append(tour_obj)

            # boxitems li --------------------------

        except Exception as msg:
            print('데이터 가져오기 오류 : ', msg)
        # try except ------------------------------
    # page for -----------------------------------

    print(tour_list)
    print(len(tour_list))



    # time.sleep(10) # 10초 멈춤
    
    # 브라우저 종료
    driver.close()  # 크롬 브라우저 닫기
    driver.quit()   # 드라이버 종료
    
    return   # main 으로 리턴 : 프로세스 종료
# run() ---------------------------------------------