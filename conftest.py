import subprocess
from selenium import webdriver
import pytest


@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    service = webdriver.ChromeService(service_args=['--log-level=INFO'], log_output=subprocess.STDOUT)
    driver = webdriver.Chrome(options=options, service=service)
    driver.set_page_load_timeout(10)

    yield driver

    driver.close()
