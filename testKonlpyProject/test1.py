#test1.py
# 한글 형태소 분석 테스트1 스크립트

# Hannanum KAIST 말뭉치를 이용해 생성된 사전
from konlpy.tag import Hannanum # 클래스만 임포트함

hannanum = Hannanum() # 레퍼런스 변수 = 객체 생성 ()

# 제공되는 메소드 정리
# 레퍼런스.메소드(전달인자)
# hannanum.analyze() # 구(Phrse) 분석
# hannanum.morphs() # 형태소 분석
# hannanum.nonus() # 명사 분석
# hannanum.pos() # 형태소 분석 태킹

# 사용예시
print('Hannanum -------------------------------')
text1 = u'롯데마트의 흑마늘 양념 치킨이 논란이 되고 있다.'
print(hannanum.analyze(text1))
#jpype1 설치관련 에러가 발생한다면, 윈도우 os 관련 팩 다운 설치
# 필요함 down url : https://www.microsoft.com/ko-kr/download/details.aspx?id=48145