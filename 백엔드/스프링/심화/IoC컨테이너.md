## 251003 - IoC

### IoC 원칙

- Inversion of Control
- 전통적으로, 객체는 자신이 필요로 하는 다른 객체를 직접 생성하고 관리할 책임이 있었음
  - OrderService는 클래스 내부에서 new OrderRepository()와 같이 직접 OrderRepository를 생성해야 했음
  - OrderService가 제어의 주체
  - 프로그램의 흐름과 객체 생명주기를 능동적으로 관리함
- IoC는 이 제어 흐름을 뒤집는 것을 의미함
- 이 책임을 프레임워크나 컨테이너와 같은 외부 독립적 주체에게 위임
- 개발작 코드는 프레임워크의 호출에 반응하는 수동적 존재가 됨
- 객체 생성, 구성, 생명주기 관리의 제어권이 프레임워크로 역전

### IoC - 디커플링과 확장성

- IoC의 핵심: 결합도(Coupling)을 낮추는 것 -> Decoupling
- 전통적인 방식에서 OrderService는 OrderRepositoryImpl이라는 구체적 구현 클래스에 직접 의존
  - OrderRepositoryImpl의 구현이 변경될 경우 OrderService 코드 수정이 불가피
  - IoC는 이런 강한 결합 문제를 해결
- IoC를 활용하면 OrderService는 OrderRepository라는 추상적 인터페이스에만 의존하게 됨
  - 실제 구현 객체는 외부의 컨테이너가 전달함
  - 작업의 실행과 구현이 분리됨
  - 다른 구현체로의 전환 용이
  - 애플리케이션 모듈성 향상
  - 테스트 시 Mock 주입 용이
  - 확장가능성 향상

### IoC의 핵심 구현체로서의 의존성 주입(DI)

- IoC 설계 원칙을 구현하는 가장 보편적인 방법: 의존성 주입(Dependency Injection)
- [DI 정리 문서로 이동](./DI.md)

### IoC 컨테이너 - 프레임워크의 엔진

- IoC 원칙을 구현하는 실체를 컨테이너라고 함
- 앱의 구성요소를 조립하고 생명주기를 관리하는 엔진
- BeanFactory - 기초적인 컨테이너
  - 스프링 IoC 컨테이너의 최상위 루트 인터페이스
  - DI, 빈 생명주기 관리에 대한 가장 기본적인 기능 제공
  - 메타데이터 기반으로 객체 생성
  - 의존성 주입
  - 지연 로딩을 기본 전략으로 사용
    - 빈을 호출받는 시점(`getBean()`)에 객체를 생성
    - 앱 시작 시점의 부하를 줄일 수 있지만, 설정 오류가 발생했을 경우 이를 런타임 시점이 되어서야 발견
- ApplicationContext - 진보된 엔터프라이즈 컨테이너
  - BeanFactory 인터페이스를 상속받는 하위 인터페이스
  - 사실상 모든 스프링 앱에서 표준으로 사용되는 컨테이너
  - BeanFactory의 기능을 모두 포함하는 완전한 상위 집합
  - 메시지 소스 처리
  - 이벤트 발행
  - AOP 통합
  - 웹 환경 지원 - WebApplicationContext
  - 컨테이너가 시작되는 시점에 설정 파일에 정의된 모든 싱글톤 빈을 미리 인스턴스화 (즉시 로딩 - Eager loading)
    - 앱 실행 시 추가 부하
    - 주입 오류나 설정 문제를 시작 단계에서 즉시 발견할 수 있음 (fail-fast)

### 구현체와 부트스트래핑

- ApplicationContext 인터페이스는 다양한 구현체를 통해 구체화됨
- 현대 자바 기반 설정에서는 `AnnotationConfigApplicationContext`가 주로 사용됨
  - 굳이 개발자가 안써도 됨. @SpringBootApplication 어노테이션이 붙은 메인 클래스가 실행되면 스프링부트가 자동으로 적합한 구현체를 생성하기 때문.
