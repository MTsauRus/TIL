## 프론트 컨트롤러 패턴 소개

- 기존의 MVC는 공통 처리가 불가
- ![alt text](image-6.png)
- ![alt text](image-7.png)
- 프론트 컨트롤러 패턴
  - 프론트 컨트롤러 서블릿 하나로 클라의 요청을 받는다.
  - 프론트 컨트롤러가 요청에 맞는 컨트롤러를 찾아 호출한다.
  - 입구가 하나, 공통 처리 가능
  - <mark>따라서, 프론트 컨트롤러를 제외한 나머지 컨트롤러는 서블릿을 상속받을 필요가 없다.</mark>
- 참고로, 스프링MVC의 DispatcherServlet이 FrontController 패턴이다.

## 유연한 컨트롤러 1 - V5

- 어댑터 패턴

  - V3, V4는 호환이 안됨. 아예 다른 버전
  - 프론트 컨트롤러가 다양한 방식의 컨트롤러를 처리할 수 있도록 변경해보자.
  - 핸들러 어댑터 목록에서 V3, V4 등과 호환되는 어댑터를 찾아오자.
  - 그 다음 핸들러 어댑터를 끼워서 핸들러(컨트롤러)를 호출하자.

- MyHandlerAdapter
  - boolean supports(object handler)
    - handler는 컨트롤러를 의미
    - 어댑터가 해당 컨트롤러를 처리할 수 있는지를 판단
  - ModelView handle(request, response, handler)
    - 어댑터가 컨트롤러를 호출. 모델뷰 리턴
