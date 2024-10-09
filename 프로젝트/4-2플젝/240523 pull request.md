## Employee

### EmployeeEntity

- employeeId를 `@Generatedvalue`, `Long` 타입으로 변경하였습니다.
- `@OneToMany` 관계를 맺고 있는 receipt에 `cascade` 옵션을 적용하기 위해 `List<Reciept>` 타입의 간이 필드를 만들었습니다.
- workingHistories 필드를 만들었습니다. 역시 `cascade`를 적용하기 위함입니다.
- partTime 필드를 위한 PartTime Enum class를 만들었습니다.
- NONE은 '퇴사' 혹은 '해고'된 직원을 의미합니다.

### EmployeeRepository

- JpaRepository를 상속받았습니다. 다른 특이사항은 없습니다.

### EmployeeDTO

- `@NotBlank`, `@Min` 어노테이션을 활용하여 포괄적인 방식으로 예외처리하였습니다.
- 주민번호, 계좌번호의 입력 형식 제한 등, 추가 예외 처리의 계획이 있습니다.

### EmployeeService, EmployeeController: `@RequestMapping("/employee")`

- `Service.getAllEmployees`
  - 모든 직원 리스트를 가져온 후 DTO로 반환합니다.
- `Controller.findAll`
  - `@GetMapping`
  - `getAllEmployees`를 실행시킵니다. <br><br><br>
- `Service.saveEmployee`
  - EmployeeDTO를 Employee로 변환한 후 DB에 저장합니다.
- `Controller.join`
  - `@PostMapping("/join")`
  - `saveEmployee`를 실행시킵니다.<br><br><br>
- `Service.updateEmployee`
  - employeeId를 식별자로 하는 직원의 `partTime` 값을 `NONE`으로 수정합니다.
- `Controller.retirementEmployee`
  - `@PutMapping("/retirement/{employeeId}")`
  - `updateEmployee`를 실행시킵니다.<br><br><br>
- `Service.deleteEmployee`
  - employeeId를 식별자로 하는 직원 row를 삭제합니다.
  - reciept, employeeWorkingHistory는 cascade에 의해 같이 삭제됩니다.
- `Controller.deleteEmployee`
  - `@DeleteMapping("/delete/{employeeId}")`
  - `deleteEmployee`를 실행시킵니다.<br><br><br>

## EmployeeWorkingHistory

- 직원의 출퇴근 히스토리를 관리하는 도메인입니다.
- 코드 줄마다 최대한 주석을 작성하였습니다.

### EmployeeWorkingHistoryEntity

- 히스토리 id, 직원 id, 출근 시간, 퇴근 시간, 일한 시간으로 구성되어 있습니다.

### EmployeeWorkingHistoryDTO

- 서비스 메소드 별 요구 필드
  - findAllEmployeeWorkingHistories: 해당 직원의 출퇴근 기록을 모두 불러오는 메소드
    - BE 단에서 네 가지 필드 모두 채워서 보내드립니다.
  - addWorkingHistory: 임의로 직원의 출퇴근 기록을 추가하는 메소드
    - 필요 필드: employeeId, startDateTime, endDateTime

### EmployeeWorkingHistoryService, EmployeeWorkingHistoryController `@RequestMapping("/employee/work")`

- `Service.findAllEmployeeWorkingHistories`, `Controller.findAllHistories`
  - `@GetMapping("{employeeId})`
  - 해당 직원의 출퇴근 히스토리를 모두 불러옵니다.<br><br><br>
- `Service.startWorking`, `Controller.startWorking`
  - `@GetMapping("/{employeeId}/start")`
  - 출근할 때 사용하는 메서드입니다.
  - 출근한 후 버튼을 누르면 해당 직원의 WorkingHistory가 생성됩니다.
  - 생성되는 WorkingHistory의 값은 다음과 같습니다.
    - employeeId: 출근 버튼을 누른 직원의 아이디 값입니다.
    - startDateTime: 출근 버튼을 누른 시점의 시간이 입력됩니다. `LocalDateTime.now().withNano(0)`이 입력됩니다.
    - endDateTime: 출근 시간으로부터 8시간을 더한 값이 입력됩니다. 디폴트 업무 시간으로 8시간을 잡았습니다.
    - workingHour: 디폴트 값인 8시간을 입력합니다.<br><br><br>
- `Service.endWorking`, `Controller.endWorking`
  - `@PutMapping("/{employeeId}/end")`
  - 이름은 퇴근용 메소드지만, 기본적으로 누르지 않습니다.
  - 디폴트 값으로 8시간 근무가 세팅되어있기 때문입니다.
  - 조퇴, 연장근무 등 임의로 퇴근시간을 변경해야 할 때 사용됩니다. <br><br><br>
- `Service.addWorkingHistory`, `Controller.addWorkingHistory`
  - `@PostMapping("/addHistory")`
  - 임의로 직원 id, 출근 시간, 퇴근 시간을 입력해서 출퇴근 히스토리를 추가합니다.<br><br><br>
- `Service.deleteEmployeeWorkingHistory`, `Controller.deleteWorkingHistory`
  - `@DeleteMapping("/delete/{employeeWorkingHistoryId}")`
  - employeeworkingHistoryId를 가진 row를 삭제합니다.

<br><br><br>

## TODO

- Employee의 직원 퇴직 로직에 정산 관련 메소드 추가하기
- partTime = "NONE" (퇴직한 직원)에 대해 출퇴근 메소드가 동작하지 않도록 예외 처리하기
