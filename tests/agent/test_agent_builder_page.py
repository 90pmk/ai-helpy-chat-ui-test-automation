import pytest

from src.locators.agent_builder_locators import AgentBuilderLocators


pytestmark = [pytest.mark.agents]


# Feature: 에이전트 빌더 채팅 모드
# Scenario: 채팅 모드를 선택하면 대화 입력창이 표시된다
# Given: 로그인한 사용자가 에이전트 빌더 페이지에 있다
# When: 사용자가 대화형 빌더 모드를 선택한다
# Then: 채팅 입력창이 표시되어야 한다
@pytest.mark.full
def test_choose_chat_builder_mode(agent_builder_page):
    agent_builder_page.open_builder().choose_chat_builder_mode()

    assert agent_builder_page.has_chat_builder_prompt()
    assert agent_builder_page.is_chat_builder_mode_selected()


# Feature: 에이전트 빌더 설정 모드
# Scenario: 설정 모드를 선택하면 입력 필드가 표시된다
# Given: 로그인한 사용자가 에이전트 빌더 페이지에 있다
# When: 사용자가 설정형 빌더 모드를 선택한다
# Then: 설정 입력에 사용할 텍스트 필드 또는 텍스트 영역이 표시되어야 한다
@pytest.mark.full
def test_choose_form_builder_mode(agent_builder_page):
    agent_builder_page.open_builder().choose_form_builder_mode()

    inputs = agent_builder_page.find_all(AgentBuilderLocators.TEXT_INPUTS)
    textareas = agent_builder_page.find_all(AgentBuilderLocators.TEXTAREAS)

    assert agent_builder_page.is_form_builder_mode_selected()
    assert inputs or textareas
    assert agent_builder_page.has_form_builder_fields()
