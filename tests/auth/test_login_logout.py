import pytest

from src.constants.messages import get_message_candidates
from src.pages.login_page import LoginPage


pytestmark = [pytest.mark.auth]


def require_credentials(credentials):
    if not credentials["username"] or not credentials["password"]:
        pytest.skip("USERNAME_1/PASSWORD_1 environment variables are required.")

# Feature: 로그인 인증
# Scenario: 유효한 계정으로 로그인에 성공한다
# Given: 사용 가능한 테스트 계정이 준비되어 있다
# When: 사용자가 올바른 계정 정보로 로그인한다
# Then: 인증 후 앱 셸이 열려야 한다
def test_login_success(driver, credentials):
    require_credentials(credentials)

    page = LoginPage(driver).open_login_page()
    page.login(credentials["username"], credentials["password"])
    page.wait_for_url_contains("ai-helpy-chat", timeout=30)

    assert "ai-helpy-chat" in driver.current_url


# Feature: 로그인 검증
# Scenario: 잘못된 비밀번호 입력 시 오류 메시지가 표시된다
# Given: 유효한 사용자 아이디를 알고 있다
# When: 사용자가 잘못된 비밀번호를 입력하고 로그인한다
# Then: 로그인 실패 오류 메시지가 표시되어야 한다
def test_wrong_password_shows_error(login_page, credentials):
    if not credentials["username"]:
        pytest.skip("USERNAME_1 environment variable is required.")

    login_page.enter_email(credentials["username"])
    login_page.enter_password("wrongpassword123!!")

    assert login_page.get_entered_email() == credentials["username"]
    assert login_page.get_entered_password() == "wrongpassword123!!"

    login_page.click_login()

    error_message = login_page.get_password_error_message()
    expected_candidates = get_message_candidates("errors.login.invalid_credentials", login_page.locale)
    assert any(candidate in error_message for candidate in expected_candidates)


# Feature: 로그인 검증
# Scenario: 비밀번호 없이 로그인하면 이메일 입력값이 유지된다
# Given: 유효한 사용자 아이디가 입력되어 있다
# When: 사용자가 비밀번호 없이 로그인 버튼을 누른다
# Then: 로그인 페이지에 머물고 이메일 입력값이 유지되어야 한다
def test_empty_password_keeps_user_input(login_page, credentials):
    if not credentials["username"]:
        pytest.skip("USERNAME_1 environment variable is required.")

    login_page.enter_email(credentials["username"]).click_login()

    assert login_page.get_entered_email() == credentials["username"]
    assert "signin" in login_page.driver.current_url


# Feature: 로그인 검증
# Scenario: 이메일 없이 로그인하면 비밀번호 입력값이 유지된다
# Given: 유효한 비밀번호가 입력되어 있다
# When: 사용자가 이메일 없이 로그인 버튼을 누른다
# Then: 로그인 페이지에 머물고 비밀번호 입력값이 유지되어야 한다
def test_empty_email_keeps_password_input(login_page, credentials):
    if not credentials["password"]:
        pytest.skip("PASSWORD_1 environment variable is required.")

    login_page.enter_password(credentials["password"]).click_login()

    assert login_page.get_entered_password() == credentials["password"]
    assert "signin" in login_page.driver.current_url


@pytest.mark.parametrize(
    "invalid_email",
    [
        "qa4team",
        "qa4team@",
        "@elicer.com",
        "qa4team@elicer",
        "qa4 team@elicer.com",
    ],
)
# Feature: 이메일 형식 검증
# Scenario: 잘못된 이메일 형식 입력 시 오류 메시지가 표시된다
# Given: 로그인 폼이 열려 있다
# When: 사용자가 잘못된 이메일 형식을 입력하고 로그인한다
# Then: 이메일 형식 오류 메시지가 표시되어야 한다
def test_invalid_email_format_shows_error(login_page, invalid_email):
    login_page.login(invalid_email, "wrongpassword123!!")

    error_message = login_page.get_email_error_message()
    expected_candidates = get_message_candidates("errors.login.invalid_email", login_page.locale)
    assert any(candidate in error_message for candidate in expected_candidates)
