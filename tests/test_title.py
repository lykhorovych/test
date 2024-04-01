import pytest


def test_title(browser):
    browser.get("https://epicentrk.ua/")

    assert browser.title == "Епіцентр • Національна мережа торговельних центрів"