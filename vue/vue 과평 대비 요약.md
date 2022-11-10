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

- Template Syntax
  
  - Vue 2 guide > [템플릿 문법 — Vue.js](https://vue2.hphk.io/v2/guide/syntax.html)
  
  - 렌더링 된 DOM
  
  - HTML 기반 template syntax
  
  - 선언적으로 바인딩 : Vue instance와 DOM을 연결

- Text Interpolation
  
  - 가장 기본적인 바인딩(연결) 방법
  
  - 중괄호 2개로 표기
  
  - DTL과 동일한 형태로 작성

- Directives 
  
  - v-접두사가 있는 특수 속성에는 값을 할당 할 수 있음
  
  - 값에는 JS 표현식 작성 가능
  
  - directive의 역할은 표현식의 값이 변경될 때 반응적으로 DOM에 적용하는 것
  
  - V-on : submit.prevent="onSubmt" (`:` 을 통해 전달인자를 받을 수 있음, `.`으로 표시되는 특수 접미사 -directive를 특별한 방법으로 바인딩 해야 함)

- v-text
  
  - Template Inetrpolation과 함께 가장 기본적인 바인딩 방법
  
  - {{}}와 동일한 역할

- v-html 
  
  - RAW HTML을 표현할 수 있는 방법
  
  - 사용자가 입력하거나 제공하는 컨텐츠에는 절대 사용 금지

- v-show 
  
  - 표현식에 작성된 값에 따라 element를 보여 줄 것인지 결정
  
  - boolean 값이 변경 될 때 마다 반응
  
  - 대상 element의 display 속성을 기본 속성과 none으로 toggle
  
  - 요소 자체는 항상 DOM에 렌더링 됨

- v-if 
  
  - v-show와 사용 방법은 동일, isActive의 값이 변경 될 때 반응
  
  - 단, 값이 false인 경우 DOM에서 사라짐
  
  - v-if, v-else-if, v-else 형태로 사용

- v-show VS v-if
  
  - v-show : 표현식 결과와 관계 없이 렌더링 되므로 초기 렌더링에 필요한 비용은 v-if보다 높을 수 있음. display 속성 변경으로 표현 여부를 판단하므로 렌더링 후 toggle 비용은 적음
  
  - v-if : 표현식 결과가 false인 경우 렌더링조차 되지 않으므로 초기 렌더링 비용은 v-show보다 낮을 수 있음. 단, 표현식 값이 자주 변경되는 경우 잦은 재 렌더링으로 비용이 증가할 수 있음

- v-for 
  
  - for .. in .. 형식으로 작성
  
  - 반복한 데이터 타입에 모두 사용 가능
  
  - index를 함께 출력하고자 한다면 (char, index) 형태로 사용 가능
  
  - 배열 역시 문자열과 동일하게 사용 가능
  
  - 각 요소가 객체라면 dot notation으로 접근 가능

- 특수 속성 key
  
  - v-for 사용 시 반드시 key 속성을 각 요소에 작성
  
  - 주로 v-for directive 작성 시 사용
  
  - vue 화면 구성 시 이전과 달라진 점을 확인 하는 용도로 활용, 따라서 key 중복x
  
  - 각 요소가 고유한 값을 가지고 있다면 생략 가능

- v-on 
  
  - `:`을 통해 전달받은 인자를 확인
  
  - 값으로 JS표현식 작성
  
  - addEventL
  
  ----

- Node.js 
  
  JS는 브라우저를 조작하는 유일한 언어 
  
  Node.js로 브라우저가 아닌 환경에서도 구동할 수 있게 됨

- NPM

- router-link
  
  - a태그와 비슷한 기능 -> URL 이동
  
  - routes에 등록된 컴포넌트와 매핑됨
  
  - 히스토리 모드에서 클릭 이벤트 차단하여 a태그와 달리 브라우저가 페이지를 재로드 하지 않도록 함
  
  - 목표 경로는 'to' 속성으로 지정,  필요에 따라 다른 태그로 바꿀 수 있음

- router-view 
  
  - 주어진 URL에 대해 일치하는 컴포넌트를 렌더링 하는 컴포넌트
  - 실제 컴포넌트가 DOM에 부착되어 보이는 자리를 의미
  - router-link를 클릭하면 routes에 매핑된 컴포넌트를 렌더링
  - Django에서의 block tag와 비슷함. App.vue는 base.html 역할, router-view는 blcok태그로 감싼 부분

- src/router/index.js 
  
  - 라우터에 관련된 정보 및 설정이 작성 되는 곳
  
  - Django에서의 urls.py에 해당, routes에 URL와 컴포넌트를 매핑

- src/Views 
  
  - router-view에 들어갈 component 작성
  
  - 기존 컴포넌트를 작성하던 곳은 components폴더 뿐이었지만 이제 두 폴도로 나뉘어짐
  
  - views/ 
    
    - routes에 매핑되는 컴포넌트
    
    - 다른 컴포넌트와 구분하기 위해  View로 끝나도록 만드는 것을 권장
  
  - components/ 
    
    - routes에 매핑된 컴포넌트의 하위 컴포넌트를 모아두는 폴더

Vue Router 실습

- 주소를 이동하는 2가지 방법
  
  1. 선언적 방식 네비게이션
     
     - router-link의 'to' 속성으로 주소 전달(App.vue)
     
     - 이름을 가지는 routes, Django에서 path 함수의 name 인자의 활용과 같은 방식
     
     - 동적인 값을 사용하기 때문에 v-bind를 사용해야 정상 작동
  
  2. 프로그래밍 방식 네비게이션
     
     - Vue 인스턴스 내부에서 라우터 인스턴스에 $router로 접근 할 수 있음
     
     - 다른 URL로 이동하려면 this.$router.push를 사용
     
     - history stack에 이동할 URL을 넣는(push) 방식, histroy stack에 기록이 남기 때문에 사용자가 브라우저의 뒤로 가기 버튼을 클릭하면 이전 URL로 이동 가능
     
     - <router-link :to=" 클릭과  $router.push 호출은 같은 동작

- Dynamic Route Matching
  
  - 동적 인자 전달 : URL의 특정 값을 변수처럼 사용 가능
  
  - ex) Django에서의 variable routing
  
  - route 추가 시, 동적 인자 명시 ex) HelloView.vue 작성 및 route 추가
  
  - $route.params로 변수에 접근 가능
  
  - 다만 HTML에서 직접 사용하기 보다는 data에 넣어서 사용 권장
  
  - 선언적 방식 네비게이션
    
    - params를 이용하여 동적 인자 전달 가능(교재 4/ page 67 참고)
  
  - 프로그래밍 방식 네비게이션

- route에 컴포넌트를 등록하는 또 다른 방법
  
  - lazy-loading 
    
    - 모든 파일을 한 번에 로드하려고 하면 모든 걸 다 읽는 시간이 매우 오래 걸림
    
    - 미리 로드를 하지 않고 특정 라우트에 방문할 때 매핑된 컴포넌트의 코드를 로드하는 방식을 활용할 수 있음
    
    - 최초 로드 시간 빨라짐, 당장 사용 않는 컴포넌트는 먼저 로드하지 않는 것이 핵심

- 네이게이션 가드
  
  - Vue router를 통해 특정 URL에 접근할 때 다른 url로 redirect를 하거나 해당 URL로의 접근을 막는 방법
  
  - ex) 사용자의 인증 정보가 없으면 특정 페이지에 접근하지 못하게 함

- 네비게이션 가드의 종류
  
  1. 전역 가드 : app 전역에서 동작
  - Global Before  Guard
    
    - 다른 url 주소로 이동할 때 항상 실행
    
    - router/index.js에 router.beforeEach()를 사용하여 설정
    
    - 콜백 함수의 값으로 다음과 같이 3개의 인자를 받음
      
      - to : 이동할 URL 정보가 담긴 Route 객체
      
      - form : 현재 URL 정보가 담긴 Route 객체
      
      - next : 지정한 URL로 이동하기 위해 호출하는 함수, 콜백 함수 내부에서 반드시 한 번만 호출, 기본적으로 to에 해당하는 URL로 이동
    
    - URL이 변경되어 화면이 전환되기 전 router.beforeEach()가 호출됨, 화면이 전화되지 않고 대기 상태가 됨
    
    - 변겨된 URL로 라우팅하기 위해서는 next()를 호출해줘야 함, next()가 호출되기 전까지 화면이 전환되지 않음
  
  - Login 여부에 따른 라우팅 처리
    
    - Login이 되어있지 않다면 Login 페이지로 이동하는 기능 추가
    
    - LoginView에 대한 라우터 링크 추가..
      
      실습..
  
  - 
  2. 라우터 가드 : 특정 URL에서만 동작
     
     - 전체 route가 아닌 특정 route에 대해서만 가드를 설정하고 싶을 때 사용
     
     - beforeEnter()
       
       - route에 진입 시 실행됨
       
       - 라우터를 등록한 위치에 추가
       
       - 단 매개변수, 쿼리, 해시 값이 변경될 때는 실행되지 않고 다른 경로에서 탐색할 때만 실행됨
       
       - 콜백 함수는 to, from, next 인자로 받음
  - Login 여부에 따른 라우팅 처리

- 컴포넌트 가드 : 라우터 컴포넌트 안에 정의
