import pytest

from src.pages.login_page import LoginPage


pytestmark = [pytest.mark.ui]


# Feature: 로그인 페이지 렌더링
# Scenario: 로그인 페이지 로드 시 이메일 입력창이 보인다
# Given: 브라우저가 로그인 페이지를 연다
# When: 로그인 페이지가 로드된다
# Then: 이메일 입력창이 보여야 한다
def test_login_page_loads_successfully(driver):
    page = LoginPage(driver).open_login_page()

    assert page.is_email_input_visible()


# Feature: 로그인 페이지 렌더링
# Scenario: 로그인 페이지에 필수 요소가 모두 표시된다
# Given: 로그인 페이지가 열려 있다
# When: 페이지 렌더링이 완료된다
# Then: 로그인에 필요한 요소가 모두 보여야 한다
def test_login_page_renders_required_elements(login_page):
    assert login_page.is_email_input_visible()
    assert login_page.is_password_input_visible()
    assert login_page.is_login_button_visible()
    assert login_page.is_forgot_password_link_visible()
    assert login_page.is_signup_link_visible()


# Feature: 비밀번호 입력 동작
# Scenario: 비밀번호 입력창은 기본적으로 마스킹된다
# Given: 로그인 페이지가 열려 있다
# When: 토글을 누르기 전 비밀번호 입력창을 확인한다
# Then: 비밀번호 타입은 password여야 한다
def test_password_field_is_masked_by_default(login_page):
    assert login_page.get_password_input_type() == "password"


# Feature: 비밀번호 보기 토글
# Scenario: 비밀번호 보기 토글로 입력 타입이 변경된다
# Given: 로그인 페이지가 열려 있다
# When: 사용자가 비밀번호 보기 토글을 켰다가 다시 끈다
# Then: 비밀번호 입력 타입이 text와 password로 변경되어야 한다
def test_password_toggle_changes_input_type(login_page):
    assert login_page.get_password_input_type() == "password"

    login_page.toggle_password_visibility()
    assert login_page.get_password_input_type() == "text"

    login_page.toggle_password_visibility()
    assert login_page.get_password_input_type() == "password"


# Feature: 비밀번호 찾기 이동
# Scenario: 비밀번호 찾기 링크를 누르면 복구 페이지로 이동한다
# Given: 로그인 페이지가 열려 있다
# When: 사용자가 비밀번호 찾기 링크를 클릭한다
# Then: 브라우저는 비밀번호 복구 페이지로 이동해야 한다
def test_forgot_password_link_navigates_to_recovery_page(login_page):
    login_page.click_forgot_password()
    login_page.wait_for_url_contains("recover/password")

    assert "recover/password" in login_page.driver.current_url


# Feature: 회원가입 이동
# Scenario: 회원가입 링크를 누르면 회원가입 페이지로 이동한다
# Given: 로그인 페이지가 열려 있다
# When: 사용자가 회원가입 링크를 클릭한다
# Then: 브라우저는 회원가입 페이지로 이동해야 한다
def test_signup_link_navigates_to_signup_page(login_page):
    login_page.click_signup()
    login_page.wait_for_url_contains("signup")

    assert "signup" in login_page.driver.current_url
