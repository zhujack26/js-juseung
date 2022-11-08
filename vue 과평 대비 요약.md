- Front-end Framework  : Web App(SPA)을 만들 때 사용하는 도구

- SPA (Single Page Application)
  
  - 이전까지는 사용자의 요청에 대해 적절한 페이지 별 template을 반환
  
  - SPA는 서버에서 최초 1장의 HTML만 전달받아 모든 요청에 대응하는 방식
  
  - CSR 방식으로 요청을 처리

- SSR(Server Side Rendering) : Sever가 사용자의 요청에 적합한 HTML을 렌더링하여 제공, 새 문서 보여주기 위해 브라우저는 새로고침 진행

- CSR(Client Side Rendering) 
  
  - 최초 한 장의 HTML을 받아오는 것은 동일하나, 빈 문서
  
  - 각 요청에 대한 대응을 JS를 사용하여 필요한 부분만 다시 렌더링
  
  - 필요한 페이지를 서버에 AJAX로 요청
  
  - 서버는 화면을 그리기 위해 필요한 데이터를 JSON 방식으로 전달
  
  - JSON 데이터를 JS로 처리, DOM 트리에 반영(렌더링)

- CSR 방식 사용 이유
  
  - 모든 HTML페이지를 서버로부터 받아서 표시하지 않아도 된다. (트래픽 감소, 응답 속도 증가)
  
  - 매번 새 문서를 받아 새로고침x 필요한 부분 고치므로 요청이 끊김없이 진행( UX 현상)
  
  - BE와 FE의 작업 영역 명확히 분리(협업 용이)

- CSR 단점 
  
  - 첫 구동 시 필요한 데이터가 많으면 최초 작동 시작까지 오랜 시간 소요
  
  - 검색 엔진 최적화(SEO)가 어려움

- Vue로 코드 작성하기
  
  1) Vue CDN 가져오기
  
  2) Vue instance 생성
  
  3) el, data 설정
  
  4) 선언적 렌더링 {{}}
  
  5) input tag에 v-model 작성 : input에 값 입력 -> Vue data 반영 -> DOM 반영
  - Vanila JS만으로 모든 데이터 조작 - > 불필요한 코드의 반복
  
  - Vye를 통해 데이터를 관리 - > 하나의 Data로 관리, 변경 사항도 한 번에 반영

- MVVM Parttern 
  
  - View - 우리 눈에 보이는 부분 = DOM
  
  - Model - 실제 데이터 = JSON
  
  - View Model(Vue):
    
    - View를 위한 Model
    
    - View와 연결(binding)되어 Action을 주고 받음
    
    - Model이 변경되면 View Model도 변경되고 바인딩된 View도 변경됨
    
    - View에서 사용자가 데이터를 변경하면 View Model의 데이터가 변경되고 바인딩된 다른 View도 변경됨
    
    - MVC 패턴에서 Controller를 제외하고 View Model을 넣은 패턴
    
    - View는 Model을 모르고, Model도 View를 모른다 == DOM은 Data를 모른다, Data도 DOM을 모른다(독립성 증가, 적은 의존성)

- Vue instance 
  
  - 1개의 객체, 아주 많은 속성과 메서드를 이미 가지고 있고, 이러한 기능들을 사용하는 것  ex) facebook
  
  - JS는 동일한 형태의 객체를 또 만드려면 또 다른 객체를 선언하여 생성

- 생성자 함수(참고)
  
  - 동일한 구조의 객체를 여러 개 만들고 싶으면
  
  - new 연산자로 사용하는 함수
  
  - 함수 이름은 반드시 대문자로 시작

- el(elment)
  
  - Vue instance와 DOM을 mount(연결)하는 옵션
    
    - View와 Model을 연결하는 역할
    
    - HTML id 혹은 class와 마운트 가능
    
    - Vue instance와 연결되지 않은 DOM 외부는 Vue의 영향을 받지 않음

- data 
  
  - Vue instance의 데이터 객체 혹은 인스턴스 속성
  
  - 데이터 객체는 반드시 기본 객체 {} (Object)여야 함
  
  - 객체 내부의 아이템들은 value로 모든 타입의 객체를 가질 수 있음
  
  - 정의된 속성은 interpolation {{}}을 통해 view에 렌더링 가능함
  
  - this.message 형태로 접근 가능

- methods
  
  - Vue instance의 method들을 정의하는 곳
  
  - this.$data.message -> this.message
  
  - method를 호출하여 data 변경 가능
    
    - DOM에 바로 변경된 결과 반영
    
    - Vue의 강력한 반응성
  
  - methods with Arrow Function [주의]
    
    - 메서드 정의 시, Arrow Function 사용하면 안됨
    
    - Arrow Function의 this는 함수가 선언될 대 상위 스코프를 가리킴(window)
