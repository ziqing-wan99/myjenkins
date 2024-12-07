import os

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # Create a WebDriver Instance
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.mark.order(2)
def test_homepage_element(driver):
    driver.get("https://www.python.org")  # Load a Website
    assert 'Welcome to Python.org' in driver.title
    assert 'https://www.python.org/' == driver.current_url