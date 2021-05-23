# kediTalk
창업동아리

# project introduction
Reactjs와 Django를 연동해서 
외국인들이 국내의 의료기관을 방문할 때 발생하는 어려움을 해결하기 위해 
서울열린데이터광장과 한국보건산업진흥원에서 제공하는 외국어 지원 의료기관 데이터를 기반으로 
외국어 소통이 가능한 의료기관을 추천해주는 웹앱을 제작.

#Demo vedio
https://youtu.be/pibzv00ZR5Y
// 로그인및회원가입 + 댓글작성 + 회원정보수정 + DB에서 회원정보 확인

https://youtu.be/olowtquG6z4
// 소셜로그인 구현

#Functions
1. 로그인 및 회원가입 기능
2. Google소셜로그인 기능
3. 게시글 작성 기능
4. 좋아요 기능
5. 댓글/대댓글 기능
6. 분류별 검색기능

#How to run?
<backend>
python이 깔려 있다는 전제
python3 -m venv env(가상환경이름)
(가상환경이름)env\Scripts\activate

(가상환경이름) > python -m pip install --upgrade pip
(가상환경이름) > pip install django
(가상환경이름) > pip install djangorestframework
(가상환경이름) > pip install djangorestframework-jwt
(가상환경이름) > pip install django-cors-headers
(가상환경이름) > pip install Pillow

(가상환경이름) > python manage.py createsuperuser


<frontend>
npm update
npm start
