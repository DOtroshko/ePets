from pages.base_page import BasePage
from pages.header_peages import AuthBoxPage
import time

def test(driver):
        page = BasePage(driver, 'https://officer-portal-e-pets-main.apps.envtwo.dev.registry.eua.gov.ua/officer/login')
        page.open()
        time.sleep(5)
