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
