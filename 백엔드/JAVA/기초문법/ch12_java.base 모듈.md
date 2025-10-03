### java.base 모듈

- 모든 모듈이 의존하는 기본 모듈
- 모듈 중 유일하게 requires하지 않아도 사용할 수 있다
- 포함된 패키지는 다음과 같다.

  - java.lang: 자바 언어의 기본 클래스 제공
  - java.util: 자료 구조, 컬렉션 클래스 제공
  - java.text: 날짜 및 숫자를 원하는 형태의 문자열로 만들어주는 포맷 클래스 제공
  - java.time: 날짜 및 시간을 조작, 연산하는 클래스 제공
  - java.io: 입출력 스트림 클래스
  - java.net: 네트워크 통신과 관련된 클래스
  - java.nio: 데이터 저장을 위한 Buffer, 새로운 입출력 클래스 제공

- java.lang 패키지에 있는 클래스와 인터페이스는 import 없이 사용 가능
- Object: 자바 클래스의 최상위 클래스
- System
  - 키보드로부터 입력받을 때
  - 모니터로 출력할 때
  - 프로세스를 종료시킬 때
  - 진행 시간을 읽을 떄
  - 시스템 속성을 읽을 때
- String: 문자열을 저장하고 조작할 때
- StringBuilder: 효율적인 문자열 조작 기능이 필요할 때
- java.util.StringTokenizer: 구분자로 연결된 문자열을 분리할 때
- Byte, Short, Integer...: 기본 타입의 값을 포장할 때, 문자열을 기본 타입으로 변환할 때
- Math: 수학 쓸 때
- Class: 클래스의 메타 정보 등을 조사할 때

### Object 클래스

- 클래스를 선언할 때 extends로 다른 클래스를 상속받지 않는다면 암시적으로 java.lang.Object 클래스를 상속받는다. 즉, 자바의 모든 클래스는 Object의 자식이거나 자손 클래스이다.
- 따라서, Object가 가진 메서드는 모든 객체에서 사용 가능하다.

  - equals: 객체 동등 비교. 비교 연산자 ==와 동일
    - 주로 equals()를 재정의하여, 동등 비교용으로 사용.
    - 예를 들어, String의 경우 객체가 다르더라도 내부의 데이터가 같은지 비교하기 위해 사용
  - hashCode: 객체를 식별하는 정수. 객체의 메모리 번지를 이용해서 해시코드를 생성함.

    - 따라서, 객체마다 다른 정수값을 리턴한다.
    - equals()와 용도가 비슷한데, 두 객체가 동등한지를 비교할 때 사용한다.
    - 얘도 재정의할 때, 객체가 다르더라도 객체 내부의 데이터값이 동일하면 동일한 해시값을 뱉도록 재정의한다.
    - 보통 두 객체가 동등 객체인지 비교할 때, hashCode() 리턴값과 equals() 값을 모두 비교한다.
    - ```java
        @Getter @Setter
        public class Student {
            private int no;
            private String name;

            public Student (int no, String name) {
                this.no = no;
                this.name = name;
            }
            @Override
            public int hashCode() {
                int hashCode = no + name.hashCode(); // 학번 + 이름해시코드로 새 해시코드 정의
                return hashCode;
            }
            @Override
            public boolean equals (Object obj) {
                if (obj instanceof Student target) {
                    if (no == target.getNo() && name.equals(target.getName())) {
                        return true;
                    }
                }
                return false;
            }
        }
      ```

  - toString
    - 객체의 문자 정보를 리턴한다
    - '클래스명@16진수해시코드'
    - Date는 날짜와 시간을, String은 저장된 문자열을 리턴하도록 toString을 재정의한다.
    - System.out.println의 매개값이 객체가 올 경우 toString을 호출한다.

### 레코드 선언

- 데이터 전달을 위한 DTO 작성 시 반복되는 코드가 너무 많다.
- 이를 위해 자바14부터 레코드가 도입되었다.
- 예를 들어 PersonDTO는 name, age 필드를 갖고 있다고 가정하자.

```java
public record Person(String name, int age) {}
```

- 이렇게 레코드를 선언하면 name, age의 private final 필드가 자동 생성된다.
- 생성자 및 getter가 자동 추가된다.
- hashCode(), equals(), toString() 재정의한 코드도 자동 생성된다.

### 롬복

- @Data 어노테이션은 다음의 메서드를 생성한다.

  - getter, setter, hashcode(), equals(), toString()

- @NoArgsConstructor: 기본 생성자
- @AllArgsConstructor: 모든 필드 초기화 생성자
- @RequiredArgsConstructor: 매개변수가 없는 생성자 포함, final 및 @NotNull 필드가 있다면 이 필드만 초기화시키는 생성자 포함
- @EqualsAndHashCode

### System 클래스

- System 클래스를 이용하면 운영체제의 일부 기능을 이용할 수 있다.
- out, in: 키보드 IO
- err: 콘솔 에러 출력
- exit(): 프로세스 종료. 0인 경우 정상 종료, 비정상인 경우 1이나 -1
- currentTimeMillis(): 현재 시간을 밀리초 단위의 long 값으로 리턴
- nanoTime()
- getProperty(): 운영체제와 사용자 정보 제공
- getenv()운영체제의 환경 변수 정보 제공

### 문자열 클래스

- String

  - 문자열 리터럴은 자동으로 String 객체로 생성
  - Byte 배열을 문자열로 변환하는 방법을 제공한다.
    - `String str = new String(byte[] bytes);`
    - `String str = new String(byte[] bytes, String charsetName);`

- StringBuilder

  - String은 내부 문자열을 수정할 수 없다.
  - String에서 값을 변경하면 값을 수정하는 것이 아니라, 새로운 String 객체를 생성하는 것 뿐이다. 단지 참조를 바꾼다.
  - 잦은 문자열 변경을 하는 경우 StringBuilder를 사용해야 한다.
  - StringBuilder는 내부 버퍼에 문자열을 저장해두고 그 안에서 수정 및 삭제 작업을 진행한다.
  - append(): 문자열 끝에 추가
  - insert(int index|str): 인덱스에 추가
  - delete(시작, 끝)
  - replace(시작, 끝, 문자열)
  - toString(): 완성된 문자열을 리턴
  - 메소드 체이닝을 지원한다.

- StringTokenizer
  - 문자열이 구분자로 연결되어 있는 경우 String의 split이나 StringTokenizer를 사용하자.
  - split은 정규 표현식을 사용
  - StringTokenizer는 문자로 구분함
  - `StringTokenizer st = new StringTokenizer(data, "/")`
  - countTokens(): 분리할 수 있는 문자열의 총 수
  - hasMoreTokens(): 남아있는 문자열이 있는지 여부
  - nextToken(): 문자열을 하나씩 가져옴. 가져올게 없으면 예외를 발생시키므로 hasMoreTokens를 먼저 호출하자.

### 포장 클래스(Wrapper)

- 기본 타입의 값을 갖는 객체를 생성할 수 있다.
- 기본 타입의 값을 포장 객체로 만드는 과정을 박싱, 반대로 기본 타입의 값을 얻어내는 과정을 언박싱이라고 한다.
- `Integer obj = 100; obj.getIntValue();`
- <mark>대부분의 포장 클래스에는 parse+기본타입 정적 메서드가 있다.</mark>
  - 이를 통해 문자열을 해당 기본 타입으로 변환할 수 있다.
- 포장 객체 값 비교를 위해 ==를 사용할 수 없다.
  - 비교 연산자는 객체 참조값을 비교하기 때문이다.
  - 물론 예외도 있다. true/false, -128~127, \u0000 ~ \u007f 사이의 값은 비교 연산자를 사용하면 그 값으로 비교한다.
  - 그냥 쓰지 말자. equals()를 쓰자.

### 수학 클래스 (Math)

- 모든 메서드가 정적이다.
- Math.abs
- ceil
- floor
- max, min
- round
- random: 0.0 ~ 1.0 사이의 double 타입 난수.
  - start부터 시작하는 n개의 정수 중 하나의 정수를 얻는 방법
  - `int num = (int) (Math.random() * n) + start;`
- Math.random 대신 java.util.Random을 사용할 수도 있다. boolean, int, double 난수를 얻을 수 있다.
- java.util.Random.nextBoolean, nextDouble, nextInt

### 날짜와 시간 클래스

- Date

  - 날짜를 표현하는 클래스
  - `Date now = new Date();`
  - 원하는 포맷으로 얻으려면 `SimpleDateFormat` 클래스를 사용하자.
  - `SimpleDateFormat sdf = new SimpleDateFormat("yyyy.mm.dd HH:mm:ss");`
  - `sdf.format(now);`

- Calendar
  - 달력을 표현하는 추상 클래스
  - 역법이 다 다르므로 추상 클래스로 해놓음.
  - `Calendar.getInstance()` 하면 컴퓨터 설정 timezone 기준으로 Calendar 객체를 가져올 수 있다.

```java
public class CalendarExample {
    public static void main(String[] args) {
        Calendar c = Calendar.getInstance();
        System.out.println(c.get(Calendar.YEAR));
        System.out.println(c.get(Calendar.MONTH));
        System.out.println(c.get(Calendar.DAY_OF_MONTH));
        System.out.println(c.get(Calendar.HOUR_OF_DAY));
        System.out.println(c.get(Calendar.MINUTE));
        System.out.println(c.get(Calendar.SECOND));
        System.out.println(c.get(Calendar.MILLISECOND));
        System.out.println(c.get(Calendar.DAY_OF_WEEK));
    }
}
```

- LocalDateTime
  - 현재 시간을 얻으려면 LocalDateTime.now()를 하자
  - plusHours, minusWeeks와 같이 사용하자
  - isAfter, isBefore, isEqual, until 등의 메서드를 제공한다.

### 형식 클래스 (Formatting)

- java.text
- DecimalFormat: 숫자를 원하는 형식의 문자열로(ex: 123456 -> 123,456)
- SimpleDateFormat: 날짜를 문자열로

### 정규 표현식 클래스

- java.util.regex의 Pattern 클래스는 정규 표현식으로 문자열을 검증하는 matches() 메서드를 제공
- `Pattern.matches("정규식", "검증문자열");`

### 리플렉션

- 클래스와 인터페이스의 메타 정보를 Class 객체로 관리한다.
- 메타 정보는 패키지 정보, 타입 정보, 멤버 정보 등을 의미
- Class 객체를 얻는 방법은 세 가지가 있다.

1. `Class clazz = 클래스이름.class;` : 클래스로부터 얻`는 방법
2. `Class clazz = Class.forName("패키지/.../클래스이름");` : 클래스로부터 얻는 방법
3. `Class clazz = 객체참조변수.getClass();` : 객체로부터 얻는 방법

- 리소스 경로 얻기
  - URL getResources(String name): 리소스 파일의 URL 리턴
  - InputStream getResourceAsStream(String name): 리소스 파일의 InputStream 리턴
  - URL.getPath()는 절대 경로를 리턴

### 어노테이션

- 세 가지 용도로 사용한다.

  - 컴파일 시 사용하는 정보 전달 (@Override)
  - 빌드 툴이 코드를 자동으로 생성할 때 사용하는 정보 전달
  - 실행 시 특정 기능을 처리할 때 사용하는 정보 전달

- 어노테이션 정의는 인터페이스 정의와 유사하다.
- `public @interface AnnotationName`
- 어노테이션은 속성을 가질 수 있다. 타입과 이름으로 구성되며, 이름 뒤에 괄호를 붙여야 한다.
- 속성의 기본 값을 default 키워드로 지정할 수 있다.

```java
public @interface AnnotationName {
  String prop1();
  int prop2() default 1;
  String value(); // 기본 속성이다.
}
```

```java
package ch12;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;
import java.lang.reflect.Method;

public class AnnotationExample {
    public static void main(String[] args) throws Exception {
        Method[] declaredMethods = Service.class.getDeclaredMethods();
        for (Method declaredMethod : declaredMethods) {
            PrintAnnotation annotation = declaredMethod.
                    getAnnotation(PrintAnnotation.class);
            printLine(annotation);

            declaredMethod.invoke(new Service());

            printLine(annotation);
            }
        }

        static void printLine(PrintAnnotation annotation) {
        if (annotation != null) {
            int number = annotation.number();
            for (int i = 0; i < number; i++) {
                String value = annotation.value();
                System.out.println(value);
            }
            System.out.println();
        }
    }
}

@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
@interface PrintAnnotation {
    String value() default "-";
    int number() default 15;
}

class Service {
    @PrintAnnotation
    public void method1() {
        System.out.println("method1");
    }
    @PrintAnnotation("*")
    public void method2() {
        System.out.println("method2");
    }
    @PrintAnnotation(value = "#", number = 15)
    public void method3() {
        System.out.println("method3");
    }
}

```
