import pytest


def test_title(browser):
    browser.get("https://rozetka.com.ua/ua/")

    assert browser.title == "Інтернет-магазин ROZETKA™: офіційний сайт найпопулярнішого онлайн-гіпермаркету в Україні"