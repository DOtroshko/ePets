import locators.locators_elements

from locators.locators_elements import PageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class AuthBoxPage(BasePage):
    locators = PageLocators()

    def fill_all_field(self):
        self.element_is_present(self.locators.MUI_BUTTON_BASE).click()
        #self.element_is_present(self.locators.PK_TYPES_BLOCK).click()
        #self.element_is_present(self.locators.PK_TYPES_BLOCK).click()
        #print(self.locators.PK_CA_SELECT, "Тестовий ЦСК АТ")
