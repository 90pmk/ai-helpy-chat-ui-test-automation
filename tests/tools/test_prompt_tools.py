import pytest

from src.data.lesson_data import LESSON_DATA
from src.data.student_data import STUDENT_DATA
from src.pages.tools.behavior_page import BehaviorPage
from src.pages.tools.deep_investigation_page import DeepInvestigationPage
from src.pages.tools.lesson_plan_page import LessonPlanPage


pytestmark = [pytest.mark.tools]


# Feature: 수업지도안 입력 유지
# Scenario: 수업지도안 도구에 주제를 입력하면 입력값이 유지된다
# Given: 로그인한 사용자가 도구 페이지에 있다
# When: 사용자가 수업지도안 도구를 열고 주제를 입력한다
# Then: 입력한 주제는 내용 입력 필드에 유지되어야 한다
@pytest.mark.full
def test_prepare_lesson_plan_content(tools_page):
    tools_page.open_lesson_plan_tool()
    lesson_plan_page = LessonPlanPage(tools_page.driver, locale=tools_page.locale)
    lesson_plan_page.input_content(LESSON_DATA["default_topic"])

    assert lesson_plan_page.get_content_value() == LESSON_DATA["default_topic"]
    assert "/ai-helpy-chat/tools/" in lesson_plan_page.driver.current_url


# Feature: 행동특성 입력 유지
# Scenario: 행동특성 도구에 요청사항을 입력하면 입력값이 유지된다
# Given: 로그인한 사용자가 도구 페이지에 있다
# When: 사용자가 행동특성 도구를 열고 요청사항을 입력한다
# Then: 입력한 요청사항은 프롬프트 입력 필드에 유지되어야 한다
@pytest.mark.full
def test_prepare_behavior_prompt(tools_page):
    tools_page.open_behavior_tool()
    behavior_page = BehaviorPage(tools_page.driver, locale=tools_page.locale)
    behavior_page.input_prompt(STUDENT_DATA["sample_record"])

    assert behavior_page.get_prompt_value() == STUDENT_DATA["sample_record"]
    assert "/ai-helpy-chat/tools/" in behavior_page.driver.current_url


# Feature: 심층 조사 입력 유지
# Scenario: 심층 조사 도구에 조사 요청을 입력하면 입력값이 유지된다
# Given: 로그인한 사용자가 도구 페이지에 있다
# When: 사용자가 심층 조사 도구를 열고 조사 요청을 입력한다
# Then: 입력한 조사 요청은 프롬프트 입력 필드에 유지되어야 한다
@pytest.mark.full
def test_prepare_deep_investigation_prompt(tools_page):
    tools_page.open_deep_investigation_tool()
    deep_investigation_page = DeepInvestigationPage(tools_page.driver, locale=tools_page.locale)
    deep_investigation_page.input_prompt(LESSON_DATA["default_topic"])

    assert deep_investigation_page.get_prompt_value() == LESSON_DATA["default_topic"]
    assert "/ai-helpy-chat/tools/" in deep_investigation_page.driver.current_url
