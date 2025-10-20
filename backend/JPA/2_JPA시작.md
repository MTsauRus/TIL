## 멤버 클래스

```java
@Entity
//@Table(name = "USER") // 만약, 이름이 다른 테이블에 저장해야 할 때 이렇게 지정. USER이란 테이블에 저장된다.
public class Member {

    @Id // PK를 알려줘야 함.
    private Long id;

    //@Column(name = "username") // @Table처럼 컬럼도 매핑해줄 수 있다.
    private String name;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
```

## JpaMain 클래스

```java
package hellojpa;

import jakarta.persistence.*;

public class JpaMain {

    public static void main(String[] args) {

        // emf는 실행 시점에서 하나만 만들어야 함.
        EntityManagerFactory emf = Persistence.createEntityManagerFactory("hello");

        // 일관적인 일을 할 때마다 em을 만들어줘야 함.
        // em을 자바 컬렉션과 같다고 이해하면 된다. 내 객체를 대신 디비에 저장해줌
        // em은 스레드 간 공유하면 안 됨.
        EntityManager em = emf.createEntityManager();
        //code
        EntityTransaction tx = em.getTransaction();
        tx.begin(); // 트랜잭션 만들고 시작. 모든 변경은 트랜잭션 내부에서 진행되어야 함.

        try { // try로 트랜잭션 수행
            Member member = new Member();
            member.setId(1L); // 멤버의 아이디값 세팅
            member.setName("hgr"); // 멤버의 이름 세팅
            em.persist(member); // persist: 연결된 DB에 저장

        /* 조회, 수정하는 방법
        *   Member findMember = em.find(Member.class, 1L); // 1이라는 키를 가진 컬럼을 조회한다.
        *   findMember.setName("hgr2"); // 1이라는 키를 가진 컬럼의 이름을 수정한다. 자동으로 update 쿼리를 날려줌
        * */
            tx.commit(); // 트랜잭션 끝
        } catch (Exception E) { // 트랜잭션에서 익셉션이 발생했을 경우, 해당 트랜잭션을 롤백
            tx.rollback();
        } finally { // 관련 em을 닫아줌
            em.close();
        }
        emf.close();
    }
}

```
