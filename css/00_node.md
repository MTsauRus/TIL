## css

##### Cascading Style Sheets

- 여러 웹 페이지의 레이아웃을 한 번에 컨트롤할 수 있다.

- css 파일로 스타일을 전체 웹 페이지에 한 번에 적용할 수 있기 때문에 많은 작업을 줄일 수 있다.

##### W3C 표준화 제정 단계 - https://caniuse.com/

- WD: 초안, 여러 커뮤니티로부터 검토를 받기 위해 공개한 문서. 실무에 적용하기 부담스럽다.

- CR: 후보권고안, 충분한 검토를 받아 기술적인 요구사항이 충족된 단계. 실무에 적용할 수 있음.
- PR: 제안권고안, 최종 승인을 얻기 위해 검토하는 단계
- REC: 권고안, 승인이 완료되어 표준화됨

## CSS selector

[01_universal_selector.html](01_universal_selector.html)
[02_class_selector.html](02_class_selector.html)

- CSS selector 사용법을 기억하자. JS때와도 동일하기 때문이다.
- <mark>전체 선택자: \*{ }</mark> head의 style 태그 내부에 쓰자.  
  ![Alt text](./image/universal_selector.png)
- <mark>클래스 선택자: .{ } 점으로 시작. 가장 많이 사용된다. </mark> 동일한 클래스 값을 가진 태그의 스타일을 변경한다.
- main, secondary, info, danger 등의 color 선택자를 따로 만들어놓자.
- \<p class="selector1 selector2 .. ">와 같이, 한 태그 내에 여러 개의 선택자를 적용시킬 수 있다.
- <mark>태그 선택자: 태그명을 선택자로 사용한다.</mark> 특정 태그에만 적용시킬 스타일을 작성하자.
- <mark>아이디 선택자: #id_name{ } #으로 시작.</mark> 태그 내부의 유일한 속성값인 id, 그 id를 찾아 스타일을 적용시킨다.  
  실무에서 많이 사용되지는 않는다. inline으로 하면 되지, 굳이 selector를 쓸 이유가 없기 때문이다.
- <mark>복합 선택자(combination selector): 4가지 방식이 존재한다.</mark>

  1. <mark>하위 선택자 방식: parentTag childTag { } 식으로 쓴다.</mark> parentTag 내부의 모든 childTag에 적용시킨다.
  2. <mark>자식 선택자 방식: parentTag > childTag { } 식으로 쓴다.</mark> 하위 선택자와의 차이점은 childTag 하나만 찾는다는 점. (깊이가 1)  
     ![Alt text](./image/combination_selector1.png)
  3. <mark>인접 형제 선택자 방식: tag1 + tag2 { }</mark> 형식. tag1 뒤에 나오는 tag2 한 개에 적용.
  4. <mark>일반 형제 선택자 방식: tag1 ~ tag2 { }</mark> 형식. tag1 뒤에 나오는 모든 tag2에 적용.

  ![Alt text](./image/combination_selector2.png)

47:50~
