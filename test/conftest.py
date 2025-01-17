import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from page.API_Page import Travel
from data.DataProvider import DataProvider
from configuration.ConfigProvider import ConfigProvider


@pytest.fixture
def driver():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    return browser

@pytest.fixture
def resp():
    return Travel()

@pytest.fixture
def test_data():
    return DataProvider()

@pytest.fixture
def api_client() -> Travel:
    DataProvider.get_token()
    return Travel(
        ConfigProvider().get('api', 'base_url'), DataProvider.get_token())
