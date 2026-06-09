import pytest

from src.data.quiz_data import QUIZ_DIFFICULTIES, QUIZ_TOPICS, QUIZ_TYPES


pytestmark = [pytest.mark.tools]


# Feature: 퀴즈 도구 입력 준비
# Scenario: 퀴즈 도구에서 필수 입력값을 채울 수 있다
# Given: 로그인한 사용자가 도구 페이지에 있다
# When: 사용자가 퀴즈 도구를 열고 필수 항목을 입력한다
# Then: 선택한 드롭다운 값과 내용 입력값이 상세 페이지에 유지되어야 한다
@pytest.mark.full
def test_prepare_quiz_generation_form(quiz_tool_page):
    quiz_tool_page.open_tools_page().open_quiz_tool()
    quiz_tool_page.select_dropdown_value("quiz_configs.0.option_type", QUIZ_TYPES["single_choice"])
    quiz_tool_page.select_dropdown_value("quiz_configs.0.difficulty", QUIZ_DIFFICULTIES["easy"])
    quiz_tool_page.input_content(QUIZ_TOPICS["qa"])

    assert quiz_tool_page.get_dropdown_display_text("quiz_configs.0.option_type") == "\uac1d\uad00\uc2dd (\ub2e8\uc77c \uc120\ud0dd)"
    assert quiz_tool_page.get_dropdown_display_text("quiz_configs.0.difficulty") == "\uc0c1"
    assert quiz_tool_page.attribute_of(("name", "content"), "value") == QUIZ_TOPICS["qa"]
    assert "/ai-helpy-chat/tools/" in quiz_tool_page.driver.current_url
