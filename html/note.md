## HTML

##### Hyper Text Markup Language

## 웹 개발 라이프사이클

1. 정보 수집 단계

2. 기획 단계  
   기술 스택 정하기

3. 디자인 단계  
   여러 가지 디자인 시안

4. 콘텐츠 생성 단계

5. 개발 단계  
   HTML, CSS, JS, 서버, DB

6. 테스트 및 품질 보증 단계  
   QA(Quality Assurance), Test. 문제 발생 시 다시 개발.

7. 배포 및 운영 단계

## 작업 환경 (extensions)

- live server
- snippets
- HTML CSS support
- open in browser
- Prettier - Code formatter

## 02_HTML 기본 구조 및 기본 요소

[01](TIL\html\01_helloworld.html)
[02](TIL\html\02_basic.html)

- 요소(element) : 태그 사이에 들어가 있는 내용들
- html을 작성한 후, 우클릭으로 open live server
- \<p> 태그는 문장을 나눔.
- <a href="naver.com">네이버</a>
- <a href="./01_helloworld.html">01_helloworld.html</a>
- \<a> 태그는 js로 작성된 함수를 작동시킬 수 있음.
- \<img> src에는 이미지 주소, alt에는 이미지 설명
- \<br> 줄바꿈 태그
- \<label>
- \<input>

## 03\_글로벌 속성과 로컬 속성

[03](TIL\html\03_global_attribute.html)

#### 글로벌 속성

- \<h1 draggable="true"> : 잡아 끌 수 있음.
- \<p lang = "ko">대한민국</p> : 이 문장의 언어가 무엇인지. 구글 검색 시 해당 문자가 한글로 반영된다.
- hidden: 화면에 보이지 않는 속성.
- id: body 내에 유일한 키 값.
- spellcheck: 스펠링 검사. 빨간 밑줄이 그어진다.
- contenteditable: 수정 가능한 문장.
- tabindex: 탭 키 눌렀을 때 이동 순서.
- title: 마우스를 갖다 댔을 때 뜨는 설명문.
