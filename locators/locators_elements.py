from selenium.webdriver.common.by import By
import selenium


class PageLocators:

    #enter_to_platform
    MUI_BUTTON_BASE = (By, "div:nth-child(2)>button>span.MuiButton-label")

    #pk_read

    PK_TYPES_BLOCK = (By.CSS_SELECTOR, "Method...)#id: pkTypeFileTitle (radio btn)")
    PK_CA_SELECT = (By.CSS_SELECTOR, '#pkCASelect')#id: pkCASelect (menu) Тестовий ЦСК АТ "ІІТ"
    PK_READ_FILE_SELECT_BTN = (By.ID, "#pkReadFileSelectButton") #id: pkReadFileSelectButton
    PK_READ_PASSWORD_BLOCK = (By.ID, "#kReadFilePasswordTextField")#id: pkReadFilePasswordTextField
    PK_READ_FILE_BUTTON_BLOCK = (By.ID, "#pkReadFileButton")#id: pkReadFileButton




