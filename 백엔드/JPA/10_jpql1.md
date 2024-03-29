## 소개

- JPA를 사용하면 엔티티 객체를 중심으로 개발
- 검색을 할 때도 테이블이 아닌 엔티티 객체를 대상으로 검색

### JPQL

- SQL을 추상화한 객체 지향 쿼리언어

### QueryDSL

- 문자가 아닌 자바코드로 JPQL을 작성할 수 있음.
- 동적 쿼리 작성이 편리함
- 단순하고 쉬움
- JPQL 빌더 역할
- 실무에 적합하다

## JPQL 기본 문법

- JPQL은 객체지향 쿼리 언어. 엔티티 객체를 대상으로 쿼리.
- 특정 DB SQL에 의존하지 않음.
- JPQL -> SQL로 변환됨

### JPQL 문법

- 대소문자 구분.
- JPQL 키워드는 대소문자 구분 X. (select, from, where)
- <mark>엔티티 이름을 사용해야 한다. 테이블 이름 X</mark>
- 별칭은 필수이다.

```sql
    select m From Member as m where m.age > 18
```

- TypeQuery: 반환 타입이 명확할 때 사용
- Query: 반환 타입이 명확하지 않을 때 사용

```java
    TypeQuery<Member> query = em.createQuery("select m from Member m", Member.class); // 타입이 Member으로 명확
    Query query = em.createQuery("select m.name, m.age from Member m"); // 타입이 String, int 혼재함.
```

- 반환은 `query.getResultList()`(반환이 여러개인 경우), `query.getSingleResult()`(반환이 한 개인 경우)로 하자.
- getResultList의 경우, 결과가 없을 때 빈 리스트를 반환한다. 즉, <mark>널포인트 익셉션 처리를 하지 않아도 된다.</mark>
- 반면에, getSingleResult()의 경우, 결과가 없어도, 둘 이상이어도 익셉션이 뜬다.

- 파라미터 바인딩

```java
    Member result = em.createQuery("select m from Member as m where m.username = :username", Member.class)
    .setParameter("username", "hgr")
    .getSingleResult();
```

- setParameter("변수이름", "값")의 방식으로 바인딩하자.

## 프로젝션

- select 절에 조회할 대상을 지정하는 것.
- 엔티티, 임베디드 타입, 스칼라 타입 모두 지정 가능

```sql
    select m from Member m -- 엔티티 프로젝션
    select m.team from Member m -- 엔티티 프로젝션
    select m.address from Member m -- 임베디드 타입 프로젝션
    select m.username, m.age from Member m -- 스칼라 타입 프로젝션
    -- DISTINCT 속성으로 중복 제거
```

- 엔티티 프로젝션 시 해당 엔티티는 <mark>영속성 컨텍스트에서 관리된다.</mark>

```java
    List<Member> result = em.createQuery("select m from Member m", Member.class)
    .getResultList();

    Member findMember = result.get(0);
    findMember.setAge(20);
```

result로 가져온 쿼리의 결과인 Member 엔티티가 영속성 컨텍스트에서 관리된다. 따라서, setAge(20)이 반영될 수 있다.

### 프로젝션 - 여러 값 조회

1. object[]

```java
    List resultList = em.createQuery("select m.username, m.age from Member m").getResultList();

    object o = resultList.get(0);
    object[] result = (object[]) o; // 오브젝트 리스트형으로 캐스팅
    svout("result[0]~~");
```

오브젝트 리스트로 캐스팅해서 가져오는 방법.

2. List<object[]> 제네릭에 선언하는 방법

```java
    List<object[]> resultList~~
```

3. <mark>new 명령어로 조회</mark>

- DTO를 만들고 select 뒤에 new를 사용하자

```java
    em.createQuery("select new jpql.MemberDTO(m.username, m.age) from Member m", MemberDTO.class)
    .getResultList();
    // MemberDTO 생성자가 존재해야 한다.
    MemberDTO memberDTO = result.get(0);
```

## 페이징

단 두 개의 API만 있다!

- setFirstResult(int startPos): 조회 시작 위치
- setMaxResults(int maxResult): 조회할 데이터 수

```java
    List<Member> result = em.createQuery("select m from Member m order by m.age desc", Member.class)
    .setFirstResult(1)
    .setMaxResults(10)
    .getResultList();
```

## 조인

- 내부 조인

```java
    String query = "select m from Member m inner join m.team t where t.name = :teamName";
    // inner는 생략 가능
```

- 외부 조인

```java
    String query = "select m from Member m left join m.team t where t.name = :teamName";
```

- 세타 조인

```java
    String query = "select m from Member m, Team t where t.name = m.username";
```

### on 절

1. 조인 대상 필터링

   회원과 팀을 조인하면서, 팀 이름이 A인 팀만 조인

   ```sql
        select m, t from Member m left join m.team t on t.name = 'A'
   ```

2. 연관관계 없는 엔티티 외부 조인

   회원의 이름과 팀의 이름이 같은 대상 외부 조인

   ```sql
       select m, t from Member m left join Team t on m.username = t.name
   ```

## 서브 쿼리

- 쿼리 안의 쿼리
- ex1. 나이가 평균보다 많은 회원

```sql
    select m from Member m
    where m.age > (select avg(m2.age) from Member m2)
```

- ex2. 한 건이라도 주문한 고객

```sql
    select m from Member m
    where (select count(o) from Order o where m = o.member) > 0
```

- JPA 서브 쿼리 한계
  - WHERE, HAVING 절에서만 서브 쿼리 사용 가능
  - SELECT 절은 하이버네이트에서만 사용 가능
  - FROM 절의 서브 쿼리는 불가능.
    - 조인으로 풀어서 해결하자

## JPQL 타입 표현

- 문자: '' 안에
- 숫자: 10L, 10D, 10F
- boolean: TRUE, FALSE
- ENUM: jpabook.MemberType.Admin(패키지명 모두 포함)
- 엔티티 타입: TYPE(m) = Member (상속 관계에서 사용)
-
