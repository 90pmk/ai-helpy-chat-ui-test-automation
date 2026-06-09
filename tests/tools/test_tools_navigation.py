import pytest


pytestmark = [pytest.mark.tools]


# Feature: 도구 홈 이동
# Scenario: 도구 페이지를 열면 도구 홈 경로로 이동한다
# Given: 로그인한 사용자가 앱 셸에 있다
# When: 사용자가 도구 페이지를 연다
# Then: 브라우저는 도구 홈 경로로 이동해야 한다
@pytest.mark.smoke
def test_open_tools_page(tools_page):
    tools_page.open_tools_page()

    assert "/ai-helpy-chat/tools" in tools_page.driver.current_url


# Feature: 퀴즈 도구 이동
# Scenario: 퀴즈 도구 카드를 열면 상세 경로로 이동한다
# Given: 로그인한 사용자가 도구 홈 페이지에 있다
# When: 사용자가 퀴즈 도구 카드를 연다
# Then: 브라우저는 퀴즈 도구 상세 경로로 이동해야 한다
@pytest.mark.full
def test_open_quiz_tool(tools_page):
    tools_page.open_quiz_tool()

    assert "/ai-helpy-chat/tools/" in tools_page.driver.current_url


# Feature: 수업지도안 도구 이동
# Scenario: 수업지도안 도구 카드를 열면 상세 경로로 이동한다
# Given: 로그인한 사용자가 도구 홈 페이지에 있다
# When: 사용자가 수업지도안 도구 카드를 연다
# Then: 브라우저는 수업지도안 도구 상세 경로로 이동해야 한다
@pytest.mark.full
def test_open_lesson_plan_tool(tools_page):
    tools_page.open_lesson_plan_tool()

    assert "/ai-helpy-chat/tools/" in tools_page.driver.current_url


# Feature: 세부 특기사항 도구 이동
# Scenario: 세부 특기사항 도구 카드를 열면 상세 경로로 이동한다
# Given: 로그인한 사용자가 도구 홈 페이지에 있다
# When: 사용자가 세부 특기사항 도구 카드를 연다
# Then: 브라우저는 세부 특기사항 도구 상세 경로로 이동해야 한다
@pytest.mark.full
def test_open_student_record_tool(tools_page):
    tools_page.open_student_record_tool()

    assert "/ai-helpy-chat/tools/" in tools_page.driver.current_url


# Feature: 행동특성 도구 이동
# Scenario: 행동특성 도구 카드를 열면 상세 경로로 이동한다
# Given: 로그인한 사용자가 도구 홈 페이지에 있다
# When: 사용자가 행동특성 도구 카드를 연다
# Then: 브라우저는 행동특성 도구 상세 경로로 이동해야 한다
@pytest.mark.full
def test_open_behavior_tool(tools_page):
    tools_page.open_behavior_tool()

    assert "/ai-helpy-chat/tools/" in tools_page.driver.current_url


# Feature: PPT 도구 이동
# Scenario: PPT 도구 카드를 열면 상세 경로로 이동한다
# Given: 로그인한 사용자가 도구 홈 페이지에 있다
# When: 사용자가 PPT 도구 카드를 연다
# Then: 브라우저는 PPT 도구 상세 경로로 이동해야 한다
@pytest.mark.full
def test_open_ppt_tool(tools_page):
    tools_page.open_ppt_tool()

    assert "/ai-helpy-chat/tools/" in tools_page.driver.current_url


# Feature: 심층 조사 도구 이동
# Scenario: 심층 조사 도구 카드를 열면 상세 경로로 이동한다
# Given: 로그인한 사용자가 도구 홈 페이지에 있다
# When: 사용자가 심층 조사 도구 카드를 연다
# Then: 브라우저는 심층 조사 도구 상세 경로로 이동해야 한다
@pytest.mark.full
def test_open_deep_investigation_tool(tools_page):
    tools_page.open_deep_investigation_tool()

    assert "/ai-helpy-chat/tools/" in tools_page.driver.current_url
