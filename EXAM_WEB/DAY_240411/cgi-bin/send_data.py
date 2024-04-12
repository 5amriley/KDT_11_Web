### 모듈 로딩
import cgi
import sys, codecs

# Web 인코딩 설정 (한글 깨짐 해결)
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

# 웹 페이지의 form 태그 내의 input 태그 입력값을
# 가져와서 저장하고 있는 인스턴스 (딕셔너리 형식)
form = cgi.FieldStorage()     # 출력 : 웹 (터미널X)

# form['img_file'] => 딕셔너리
# value 를 취하면 값을 빼낼 수 있다.
if 'img_file' in form and 'message' in form:
    filename = form['img_file'].value   # form.getvalue('img_file')
    msg = form['message'].value         # form.getvalue('message')


## 요청에 대한 응답 HTML
print('Content-Type: text/html; charset=utf-8')    # HTML is following
print()
print("<TITLE>CGI script ouput</TITLE>")
print("<H1>This is my first CGI concept.</H1>")
print(f"Hello, world! {form}")
print(f"<img src={filename}>")
print(f"<h3>{msg}<h3>")