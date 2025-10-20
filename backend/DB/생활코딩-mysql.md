[생활코딩 - DATABASE2 MySQL](https://www.youtube.com/watch?v=h_XDmyz--0w&list=PLuHgQVnccGMCgrP_9HL3dAcvdt8qOZxjW)

- cmd에서 root로 로그인하는 방법

  - `cd C:\Program Files\MySQL\MySQL Server 8.4\bin`
  - `mysql -uroot -p`
    - -u{username} -p: 비밀번호 입력창이 나옴
  - 비밀번호 입력

- 데이터베이스 생성

  - create database {databasename};
  - show databases;
  - use {databasename};
    - 이후에 입력되는 모든 쿼리는 이 데이터베이스에 반영

- 현재 테이블 구조 확인하기
- `desc topic;`: describe. 현재 스키마를 보여줌

- insert

  - `insert into topic (title, description, created, author, profile) values ('mysql', 'mysql is ...', NOW(), 'hgr', 'developer');`
  - NOW()와 같이 현재 시간을 입력해주는 함수도 있다.

- update

  - `update topic set description='Oracle is...' where id=1`

- database server

  - 우리가 cmd를 통해 접속한 mysql은 "mysql monitor"라는 database client이다. 우리는 이 클라이언트를 이용하여, 명령어를 통해 database server를 제어했다.

  - mysql monitor
    - 명령어 기반
    - 어디서든 실행 가능
    - 명령어를 기억해야 함
  - mysql workbench
    - GUI 기반
    - 직관적
