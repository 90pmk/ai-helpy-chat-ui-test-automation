import pytest

from src.data.student_data import STUDENT_DATA
from src.pages.tools.detail_special_page import DetailSpecialPage


pytestmark = [pytest.mark.tools]


# Feature: 세부 특기사항 단계 전환
# Scenario: 세부 특기사항 도구의 수업 정보를 입력하면 학생 정보 단계로 이동할 수 있다
# Given: 로그인한 사용자가 도구 페이지에 있다
# When: 사용자가 세부 특기사항 도구에서 필수 수업 정보를 입력하고 다음 단계로 이동한다
# Then: 학생 이름 검색 입력창이 표시되고 검색어를 입력할 수 있어야 한다
@pytest.mark.full
def test_prepare_detail_special_first_step(tools_page):
    tools_page.open_student_record_tool()
    detail_special_page = DetailSpecialPage(tools_page.driver, locale=tools_page.locale)
    if not detail_special_page.is_class_info_step_active():
        pytest.skip("최초 진입 상태가 아니어서 수업 정보 입력 탭 검증을 건너뜁니다.")
    detail_special_page.select_school_level_by_key("values.elementary_school")
    detail_special_page.select_grade("1학년")
    detail_special_page.input_subject("국어")
    detail_special_page.input_unit("1")
    detail_special_page.go_next()
    detail_special_page.input_student_keyword(STUDENT_DATA["search_keyword"])

    assert detail_special_page.attribute_of(DetailSpecialPage.STUDENT_SEARCH_INPUT, "value") == STUDENT_DATA["search_keyword"]
    assert "/ai-helpy-chat/tools/" in detail_special_page.driver.current_url


# Feature: 세부 특기사항 재진입
# Scenario: 수업 정보가 이미 저장된 상태로 재진입하면 학생 정보 입력 및 생성 탭이 열린다
# Given: 로그인한 사용자가 이전에 세부 특기사항 수업 정보를 저장한 상태다
# When: 사용자가 세부 특기사항 도구에 다시 진입한다
# Then: 학생 정보 입력 및 생성 탭이 활성화되고 학생 이름 검색 입력창이 표시되어야 한다
@pytest.mark.full
def test_load_detail_special_student_info_step_on_reentry(tools_page):
    tools_page.open_student_record_tool()
    detail_special_page = DetailSpecialPage(tools_page.driver, locale=tools_page.locale)

    if detail_special_page.is_class_info_step_active():
        pytest.skip("재진입 상태가 아니어서 학생 정보 입력 및 생성 탭 검증을 건너뜁니다.")

    assert detail_special_page.is_student_info_step_active()
    assert detail_special_page.is_visible(DetailSpecialPage.STUDENT_SEARCH_INPUT)
    assert "/ai-helpy-chat/tools/" in detail_special_page.driver.current_url
