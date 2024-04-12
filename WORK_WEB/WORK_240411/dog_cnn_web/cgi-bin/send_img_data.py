### 모듈 로딩
import cgi
import sys, codecs
import os, cgitb
import datetime

# Web 인코딩 설정 (한글 깨짐 해결)
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

# 웹 페이지의 form 태그 내의 input 태그 입력값을
# 가져와서 저장하고 있는 인스턴스 (딕셔너리 형식)
form = cgi.FieldStorage()     # 출력 : 웹 (터미널X)

# 클라이언트의 요청 데이터 추출
if 'img_file' in form and 'message' in form:
    fileitem = form['img_file']     # form.getvalue('img_file')
    
    # 서버에 이미지 파일 저장
    img_file = fileitem.filename

    prefix = datetime.datetime.now().strftime('%y%m%d_%H%M%S')

    save_path = f'./image/{prefix}_{img_file}'
    with open(save_path, 'wb') as f:
        f.write(fileitem.file.read())
    
    img_path = f'../image/{prefix}_{img_file}'
    msg = form.getvalue('message')
else:
    img_path = 'None'
    msg = 'None'


# form['img_file'] => 딕셔너리
# value 를 취하면 값을 빼낼 수 있다.
if 'img_file' in form and 'message' in form:
    fileitem = form['img_file'].value   # form.getvalue('img_file')
    msg = form['message'].value         # form.getvalue('message')


## 요청에 대한 응답 HTML
print('Content-Type: text/html; charset=utf-8')    # HTML is following
print()
print("<TITLE>CGI script ouput</TITLE>")
print("<H1>This is my first CGI concept.</H1>")
print(f"Hello, world! <br>")

print(f"<img src={img_path}>")
print(f"<h3>{msg}<h3>")