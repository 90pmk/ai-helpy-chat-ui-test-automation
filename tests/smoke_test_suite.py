import pytest


pytestmark = pytest.mark.smoke


# Feature: 스모크 스위트 기본 확인
# Scenario: 스모크 기본 테스트에서 로그인 입력창이 보인다
# Given: 로그인 페이지 fixture가 준비되어 있다
# When: 스모크 sanity 테스트를 실행한다
# Then: 이메일 입력창이 보여야 한다
def test_smoke_suite_marker_definition(login_page):
    assert login_page.is_email_input_visible()
