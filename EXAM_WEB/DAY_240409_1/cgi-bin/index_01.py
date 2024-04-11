### 모듈 로딩
import cgi
import sys, codecs

# Web 인코딩 설정 (한글 깨짐 해결)
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

### 사용자 정의 함수
### Web 브라우저 화면 출력 모드
def print_browser(result=""):
    # HTML 파일 읽기 -> body 문자열
    filename = './html/test.html'   # 서버관점 : DAY_240409_1(터미널 pwd) 기준 경로
    with open(filename, mode='r', encoding='utf-8') as f:
        # HTML Header
        print('Content-Type: text/html')
        print()
        # HTML Body
        print(f.read().format(result))


## -----------------------------------------------
## 요청 처리 및 브라우징
## -----------------------------------------------

### Client 요청 데이터, 즉, Form 입력 데이터 저장 인스턴스 생성
form = cgi.FieldStorage()

### 데이터 추출
if 'data' in form and 'no' in form: # name 속성이 data 이거나 no
    result = form.getvalue(key='data') +'-' + form.getvalue(key='no')
else:
    result = 'NO data'

# if 'data' in form:
#     result = form.getvalue(key='data')  # form['data']

### 브라우징
print_browser(result)


# print('Content-Type: text/html')
# print()

# # HTML Body
# print('<form><input type="text" name="data" placeholder="data"><br>')
# print('<input type="number" name="no" placeholder="no"><br>')
# print('<input type="submit"></form>')

# print(f'Hello from the other side : {result}')