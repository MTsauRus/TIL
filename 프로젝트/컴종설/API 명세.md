- AI검증DTO (FE -> AI)
  - 사진
  - 알람ID
  - 미션타입

## 회원가입

request
url: ~/user/join

- username // 아이디
- password
- name
- phonenumber
- guardianPhoneNumber (nullable)

response

- username
- name
- phoneNumber
- guardianPhoneNumber

## 로그인 요청

url: /login

- username
- password

response

- jwt token

## 유저 조회

GET ~/user/{userId}
response

- username(유저 아이디)

## 알람 관련

### 알람 불러오기

GET /alarm/{userId}

- userId

response

- 알람 다

### 알람 등록

POST /alarm/add

- alarmId // 만들어서 줌
- userId -> username으로 바꿈. username 주세요. 
- title
- timer: 알람 시간
- active: 알람 활성 여부
- repeat: 요일 / integer
- delayTimes: 몇번 울렸는지 (0, 1, 2) / 3이 되면 강제종료
- restrictAlarm: (strict / )
- missionName - string ()
- isVibration
- volume: int
- interval: 반복 간격: int

### 알람 삭제

DELETE /alarm/{alarmId}/delete

- alarmId

### 알람 수정

PUT /alarm/{alarmId}/update

- 알람 등록이랑 동일

## 알려줘

### 알려줘 불러오기

GET ~/remindMe/{userId}

response
where delayTimes >= 1 인 알람 보내기
where repeat != 0 (반복 가능한 알람)
userId todo 다 보내기

### TODO 등록

POST ~/remindMe/{userId}

request
TODO테이블에 있는거

### TODO 삭제/업데이트

## TODO 테이블 보내주기

## 리포트 테이블

### 검증 성공 시 리포트 컬럼 저장

~/verifySuccess/{verificationId}

- verificationId
- userId
- missionName // alarmId로 받고, 미션을 거기서 가져오자. 
- isSuccess
- verificationTime
- value (nullable)

## 리포트 페이지

### duration 내의 리포트 제공

POST ~/report/{userId}

- userId
- missionName
- startDate
- endDate

response

- report table ()
- userId
- missionName
- isSuccess
- verificationTime
- value (nullable)
- regularMeans (정상 수치 평균)
- userMeans (유저 평균)

## 프로필

## 보호자 기능
- 보호자가 미션 생성하는 api
- 보호자가 생성한 미션 검증 결과 따로 저장 (boolean으로 구분하는게 나은듯?)

- 일요일todo
  - 알람, 리포트, 보호자알람생성

테스트목표
로그인, 회원가입.