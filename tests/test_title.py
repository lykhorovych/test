import pytest


def test_title(browser):
    browser.get("https://www.qa-practice.com/")

    assert browser.current_url == "https://www.qa-practice.com/"
    assert browser.title == "Home Page | QA Practice"