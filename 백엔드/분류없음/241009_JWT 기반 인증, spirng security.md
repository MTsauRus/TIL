## JWT
- 세션 인증 기반 방식과 달리 stateless 방식이다.
  - 모바일 환경에 적합
  - 분산 서버 환경에서도 잘 동작
- 헤더 기반 인증
  - authorization header를 통해 토큰을 전달
- 모바일 환경의 로컬 저장소에 토큰을 저장, 로그인 유지 가능
- 보안 강화

## 구현 과정
- SecurityConfig 설정
- JWT 생성 검증 유틸리티
- 로그인 컨트롤러에서 JWT 발급
- JWT 인증 필터링
