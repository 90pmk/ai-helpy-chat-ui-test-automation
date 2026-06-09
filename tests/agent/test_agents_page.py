import pytest


pytestmark = [pytest.mark.agents]


# Feature: 에이전트 홈 이동
# Scenario: 에이전트 페이지를 열면 에이전트 경로로 이동한다
# Given: 로그인한 사용자가 앱 셸에 있다
# When: 사용자가 에이전트 페이지를 연다
# Then: 브라우저는 에이전트 경로로 이동해야 한다
@pytest.mark.smoke
def test_open_agents_page(agents_page):
    agents_page.open_agents_page()

    assert "/ai-helpy-chat/agents" in agents_page.driver.current_url


# Feature: 내 에이전트 이동
# Scenario: 내 에이전트 메뉴를 열면 내 에이전트 경로로 이동한다
# Given: 로그인한 사용자가 에이전트 페이지에 있다
# When: 사용자가 내 에이전트 섹션을 연다
# Then: 브라우저는 내 에이전트 경로로 이동해야 한다
@pytest.mark.full
def test_open_my_agents_page(agents_page):
    agents_page.open_my_agents_page()

    assert "/ai-helpy-chat/agents/mine" in agents_page.driver.current_url


# Feature: 에이전트 빌더 이동
# Scenario: 에이전트 빌더를 열면 빌더 경로로 이동한다
# Given: 로그인한 사용자가 에이전트 페이지에 있다
# When: 사용자가 에이전트 빌더를 연다
# Then: 브라우저는 에이전트 빌더 경로로 이동해야 한다
@pytest.mark.full
def test_open_agent_builder(agent_builder_page):
    agent_builder_page.open_builder()

    assert "/ai-helpy-chat/agents/builder" in agent_builder_page.driver.current_url
