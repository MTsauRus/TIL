## 1장. JPA 소개

### SQL을 직접 다룰 때 발생하는 문제점

1. 반복 코드
   - 자바 객체 만들기
   - DAO 만들기
   - SQL 작성하기
   - JDBC API를 활용하여 SQL문 실행하기
   - 조회 결과를 매핑하기  
     위의 작업을 각 테이블마다 반복해야 한다.
2. SQL에 의존적인 개발
   만약, MemberDAO에 회원의 연락처까지 저장해달라는 요구 사항이 추가되었다고 하자.
   - 회원 클래스에 tel 필드 추가
   - 연락처를 저장하기 위한 INSERT SQL 수정
   - 회원 객체의 연락처 값을 꺼내서 등록 SQL에 전달
   - 회원 조회용 SQL 수정
   - 연락처 조회 결과를 Member 객체에 매핑
     `String tel = rs.getString("TEL");` `member.setTel(tel);`
   - 연관된 객체의 코드 모두 수정... 등
     <br>

### JPA와 문제 해결

**JPA를 사용하면 SQL을 직접 작성하는 것이 아니라, JPA가 제공하는 API를 사용하면 된다. 그러면 JPA가 적절한 SQL을 생성하여 데이터베이스에 전달한다.**  
대표적인 CRUD API는 다음과 같다.

- 저장  
   `jpa.persist(member);`
  persist() 메소드는 JPA가 객체와 매핑정보를 보고 적절한 INSERT SQL을 생성하여 데이터베이스에 전달한다.
- 조회  
   `String memberId = "helloId";`  
   `Member member = jpa.find(Member.class, memberId);`  
   find() 메소드는 객체 하나를 데이터베이스에서 조회한다. 적절한 SELECT SQL을 생성하여 데이터베이스에 전달하고, 그 결과를 Member 객체를 생성하여 반환한다.
- 수정  
   `Member member = jpa.find(Member.class, memberId);`  
   `member.setName("이름변경");`  
   JPA는 별도 수정 메소드를 제공하지 않는다. 대신, 객체를 조회한 후 값을 변경하면 트랜잭션을 커밋할 때 데이터베이스에 적절한 UPDATE SQL이 전달된다.
- 연관된 객체 조회  
   `Member member = jpa.find(Member.class, memberId);`  
   `Team team = member.getTeam();`  
   JPA는 연관된 객체를 사용하는 시점에 적절한 SELECT SQL을 실행한다. 따라서, JPA를 사용하면 연관된 객체를 마음껏 조회할 수 있다.

### 패러다임의 불일치

- 자바의 객체 패러다임과 관계형 DB의 패러다임은 다르다.
  - 상속  
     객체는 상속 기능이 있지만, 테이블은 그렇지 않다.  
     item이란 객체를 상속받은 album, movie, book 객체가 있다 하자. 이를 테이블로 옮기려면 item에 DTYPE 컬럼을 추가하여 이 값에 따라 어떤 자식 테이블과 연관있는지 정의할 수 있다. 하지만 이를 상속이라고는 하기 힘들다.
  - 연관관계  
     객체는 참조를 사용하여 다른 객체를 조회한다. 테이블은 외래 키를 이용한 조인으로 연관된 테이블을 조회한다.

### 정리

- 데이터 접근 추상화와 벤더 독립성  
   같은 기능일지라도 데이터베이스 벤더마다 사용법이 다른 경우가 많다. JPA는 애플리케이션과 데이터베이스 사이의 추상화된 데이터 접근 계층을 제공한다. 이를 활용하여, 특정 데이터베이스 기술에 종속되지 않게 한다. 사용하는 DB가 바뀐 경우, JPA에게 그 DB를 알려주기만 하면 된다.
