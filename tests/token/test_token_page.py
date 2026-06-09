import pytest


pytestmark = [pytest.mark.token]


# Feature: 토큰 페이지 확인
# Scenario: 토큰 페이지 텍스트를 수집할 수 있다
# Given: 로그인한 사용자가 토큰 페이지에 있다
# When: 페이지의 표시 텍스트를 수집한다
# Then: 반환값은 문자열이어야 한다
@pytest.mark.full
def test_token_page_collects_visible_text(token_page):
    page_text = token_page.get_page_text()

    assert isinstance(page_text, str)


# Feature: 토큰 경고 목록 수집
# Scenario: 토큰 페이지에서 경고 메시지 목록을 수집할 수 있다
# Given: 로그인한 사용자가 토큰 페이지에 있다
# When: 페이지의 경고 메시지 목록을 수집한다
# Then: 반환값은 문자열 리스트여야 한다
@pytest.mark.full
def test_token_page_collects_alerts(token_page):
    alerts = token_page.get_alert_texts()

    assert isinstance(alerts, list)
    assert all(isinstance(item, str) for item in alerts)
