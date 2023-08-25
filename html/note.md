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

## 기본 구조 및 기본 요소

[01_helloworld.html](01_helloworld.html)
[02_basic.html](02_basic.html)

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

## 글로벌 속성

[03_global_attribute.html](03_global_attribute.html)

- \<h1 draggable="true"> : 잡아 끌 수 있음.
- \<p lang = "ko">대한민국\<\p> : 이 문장의 언어가 무엇인지. 구글 검색 시 해당 문자가 한글로 반영된다.
- hidden: 화면에 보이지 않는 속성.
- id: body 내에 유일한 키 값.
- spellcheck: 스펠링 검사. 빨간 밑줄이 그어진다.
- contenteditable: 수정 가능한 문장.
- tabindex: 탭 키 눌렀을 때 이동 순서.
- title: 마우스를 갖다 댔을 때 뜨는 설명문.

## 로컬 속성

[04_local_attribute.html](04_local_attribute.html)

- \<a>에서 target: 링크를 눌렀을 때의 동작  
  \_blank: 새 창을 연다.  
  \_self(default): 기존 창에서 바로 연다.
- 참고하면 좋은 링크 https://developer.mozilla.org/ko/

## 스타일 속성

[05_style.html](05_style.html)

- inline 스타일: html 요소에서 직접 style 속성을 통해 정의
- internal 스타일: \<style> 태그를 써서 작성
- external 스타일: css 문서를 작성

## 의미에 맞는 태그 사용하기

[06_meaningful.html](06_meaningful.html)

- \<p style="font-weight: bold">, \<b>, \<strong> 태그는 모두 같은 결과를 보여주지만, 태그 자체가 가지고 있는 의미가 존재한다. 문장을 강조하려는 의미에서의 볼드라면 strong 태그를 쓰는게 좋다.
- 마찬가지로, \<em> 태그는 강조하는 이탤릭 태그이다.
- \<small>: 글자를 작게 하는 태그
- \<mark>: 하이라이트
- \<del>: 취소문
- \<ins>: 밑줄
- 마찬가지로, 위의 태그는 모두 스타일 태그로 구현 가능하지만, semantic 관점에서 위의 태그를 사용하는 것이 좋다.

- \<sub>: 아래첨자
- \<sup>: 윗첨자
- \<q>: 짧은 인용
- \<blockquote cite="">: 긴 인용. 출처를 적을 수 있다.
- \<abbr title = "">: 축약어. title에는 원래 문장을 적는다.
- \<address>: 주소는 주소에 쓰자.
- \<cite>: 작품명, 상품명, 영화이름 등등

### 의미 없는 태그: div, span

1. 컨테이너의 역할
2. 컨텐츠를 배치하기 위한 레이아웃 용도

- div, h1, p: block elements. 속성을 주었을 때 한 줄을 차지한다.
- span: inline elements. 딱 차지한 만큼만.
