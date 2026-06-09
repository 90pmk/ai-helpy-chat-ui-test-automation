import pytest

from src.data.chat_data import CHAT_MESSAGES
from src.locators.chat_locators import ChatLocators


pytestmark = [pytest.mark.chats]


# Feature: 채팅 홈 이동
# Scenario: 새 대화를 시작하면 채팅 홈 경로를 유지한다
# Given: 로그인한 사용자가 앱 셸에 있다
# When: 사용자가 채팅 영역에서 새 대화를 시작한다
# Then: 브라우저는 채팅 홈 경로에 있어야 한다
@pytest.mark.smoke
def test_open_new_chat_entry(chat_page):
    chat_page.open_chat_page().open_new_chat()

    assert "/ai-helpy-chat" in chat_page.driver.current_url


# Feature: 채팅 검색 패널
# Scenario: 검색 패널을 열면 검색 입력창이 표시된다
# Given: 로그인한 사용자가 채팅 페이지에 있다
# When: 사용자가 검색 패널을 연다
# Then: 검색 입력창이 보여야 한다
@pytest.mark.full
def test_open_search_panel(chat_page):
    chat_page.open_chat_page().open_search_panel()

    assert chat_page.exists(ChatLocators.SEARCH_PANEL_INPUT)


# Feature: 채팅 검색 입력
# Scenario: 검색어를 입력하면 검색 입력값이 유지된다
# Given: 로그인한 사용자가 채팅 페이지에 있다
# When: 사용자가 검색 패널에 검색어를 입력한다
# Then: 검색 입력창 값은 입력한 검색어와 같아야 한다
@pytest.mark.full
def test_search_chat_by_keyword(chat_page):
    chat_page.open_chat_page().open_search_panel().search_chat(CHAT_MESSAGES["search_keyword"])

    assert chat_page.attribute_of(ChatLocators.SEARCH_PANEL_INPUT, "value") == CHAT_MESSAGES["search_keyword"]


# Feature: 채팅 고급 모드
# Scenario: 이미지 생성 모드를 선택하면 선택 표시가 나타난다
# Given: 로그인한 사용자가 채팅 페이지에 있다
# When: 사용자가 플러스 메뉴에서 이미지 생성을 선택한다
# Then: 선택된 모드 chip에 이미지 생성이 표시되어야 한다
@pytest.mark.full
def test_select_image_generation_mode(chat_page):
    chat_page.open_chat_page().select_image_generation()

    assert chat_page.has_selected_mode_chip("actions.image_generate")
