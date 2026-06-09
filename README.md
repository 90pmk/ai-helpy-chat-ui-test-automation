# AI Helpy Chat UI Test Automation

AI Helpy Chat UI를 대상으로 Selenium과 Pytest 기반 End-to-End 테스트를 수행하는 QA 자동화 프로젝트입니다.

## Project Overview

이 프로젝트는 사용자 관점에서 AI Helpy Chat의 주요 UI 흐름을 검증하기 위해 작성했습니다. 브라우저 기반 시나리오를 자동 실행하여 로그인, 채팅, 도구, 에이전트, 토큰 화면의 기본 동작과 화면 전환을 확인합니다.

## Tech Stack

- Python
- Selenium
- Pytest
- Jenkins
- Chrome

## Setup

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

인증이 필요한 테스트는 로컬 `.env` 또는 환경 변수에 아래 값을 설정해야 합니다.

```env
USERNAME_1=
PASSWORD_1=
BASE_URL=
```

`.env`에는 실제 계정 정보가 들어가므로 Git에 올리지 않습니다.

## Run Tests

```bash
pytest -v
pytest -m smoke -v
pytest -m full -v
pytest -m "smoke or full" -v
```

기능 영역별 실행:

```bash
pytest -m auth -v
pytest -m ui -v
pytest -m chats -v
pytest -m tools -v
pytest -m agents -v
pytest -m token -v
```

디렉터리 기준 실행:

```bash
pytest tests/auth -v
pytest tests/ui -v
pytest tests/chats -v
pytest tests/tools -v
pytest tests/agent -v
pytest tests/token -v
```

## Markers

- `smoke`: 최소 핵심 확인
- `full`: 보다 넓은 기능 검증
- `auth`: 인증 관련 테스트
- `ui`: 렌더링과 페이지 요소 테스트
- `chats`: 채팅 기능 테스트
- `tools`: 도구 기능 테스트
- `agents`: 에이전트 기능 테스트
- `token`: 토큰 관련 테스트

`pytest -m full`은 `full` marker만 실행하며 `smoke`를 자동 포함하지 않습니다. 둘 다 실행하려면 `pytest -m "smoke or full" -v`를 사용합니다.

## Jenkins / CI

로컬 기본값은 브라우저 표시 모드입니다. Headless 실행이 필요하면 아래 환경 변수를 사용합니다.

```env
HEADLESS=true
```

Jenkins 또는 CI에서는 아래 값을 사용할 수 있습니다.

```env
CI=true
```

권장 실행 순서:

```bash
pytest tests/ui/test_login_page.py -v
pytest -m smoke -v
pytest -m "auth or chats or tools or agents or token" -v
pytest -m "smoke or full" -v
```

## Project Structure

```text
src/
  components/       Shared UI component helpers
  constants/        URLs, messages, timeouts
  data/             Reusable test input data
  locators/         Selenium selectors
  pages/            Page Object Model classes
  utils/            Driver, auth, config, screenshot, waits
tests/
  auth/             Authentication flow tests
  ui/               Login page rendering and structure tests
  chats/            Chat navigation and mode-selection tests
  tools/            Tool navigation and form tests
  agent/            Agent navigation tests
  token/            Token page tests
```

## Page Object Scope

Core page objects:

- `src/pages/base_page.py`: 공통 Selenium 동작, `open`, `find`, `click`, `js_click`, `type`, visible text, URL wait
- `src/pages/login_page.py`: 로그인 폼, 비밀번호 찾기/회원가입 이동, 검증 메시지, 비밀번호 보기 토글
- `src/pages/app_shell_page.py`: 인증 이후 공통 레이아웃, 채팅/도구/에이전트 이동, 앱 셸 로드 확인
- `src/pages/chat_page.py`: 채팅 홈, 새 대화, 검색, 플러스 메뉴, 선택된 채팅 모드 확인
- `src/pages/token_page.py`: 토큰 페이지 텍스트 수집과 토큰 영역 표시 확인
- `src/pages/agents_page.py`: 에이전트 홈, 내 에이전트, 빌더 이동
- `src/pages/agent_builder_page.py`: 에이전트 빌더 진입과 옵션 선택

Tool page objects:

- `src/pages/tools/tools_home_page.py`: 도구 홈 진입, `data-ai-tool-ident` 기반 카드 선택, 상세 URL 확인
- `src/pages/tools/quiz_tool_page.py`: 퀴즈 드롭다운, 내용 입력, 생성 시작/중지
- `src/pages/tools/detail_special_page.py`: 학교급/학년/과목/단원 입력, 다음 단계 이동, 학생 검색
- `src/pages/tools/student_info_page.py`: 학생 검색 입력
- `src/pages/tools/behavior_page.py`: 행동특성 도구 페이지 동작
- `src/pages/tools/lesson_plan_page.py`: 수업지도안 도구 페이지 동작
- `src/pages/tools/deep_investigation_page.py`: 심층 조사 도구 페이지 동작

Shared components:

- `src/components/header_component.py`: 인증 이후 상단 헤더 동작
- `src/components/sidebar_component.py`: 채팅, 도구, 에이전트 사이드바 이동
- `src/components/menu_component.py`: 공통 메뉴 항목 선택
- `src/components/dialog_component.py`: 공통 dialog 확인/제출 처리
- `src/components/toast_component.py`: 토스트 메시지 표시 확인

Locator policy:

- selector는 `src/locators/*.py`, `src/locators/tools/*.py`에 분리합니다.
- 우선순위는 `data-* attribute`, `id`, `name`, `href/form`, CSS selector 순입니다.
- 가능한 경우 class 단독 의존은 피합니다.

## Artifacts

테스트 실행 중 생성되는 결과물은 Git에 올리지 않습니다.

- 실패 스크린샷: `screenshots/` 또는 `tests/**/screenshots/`
- HTML/DOM 참고 자료: `reports/dom`

위 산출물은 테스트 실행 시 다시 생성될 수 있으므로 `.gitignore`에서 제외합니다.

## Notes

- 도구 이동은 `data-ai-tool-ident`와 상세 route 확인을 기준으로 검증합니다.
- 채팅 고급 기능 검증은 선택된 모드 표시 UI에 의존합니다.
- 순간적으로 사라지는 편집 상태는 HTML보다 스크린샷이 더 유용할 수 있습니다.
