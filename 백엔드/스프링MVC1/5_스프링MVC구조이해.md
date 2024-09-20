## 스프링MVC - 시작하기

- @Controller
  - 내부에 @Component 어노테이션이 있음
  - 스프링 빈으로 등록
  - 컴포넌트 스캔의 대상이 됨
  - 스프링MVC에서 어노테이션 기반 컨트롤러로 인식
    - RequestMappingHandlerMapping에서 인식
- @RequestMapping
  - 요청 정보를 매핑
  - 애노테이션 기반으로 동작하므로, 메소드 이름은 마음대로 해도 됨
  - <mark>RequestMappingHandlerMapping이 이 어노테이션을 갖고 있는 클래스를 찾아냄</mark>
- ModelAndView
  - 모델, 뷰 정보를 담아 반환
