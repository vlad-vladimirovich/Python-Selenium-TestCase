from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """ Класс содержащий все, необходимые нам элементы веб страницы """
    SEARCH_BAR = (By.CLASS_NAME, 'input__control.input__input.mini-suggest__input')
    SUGGEST_LIST = (By.CSS_SELECTOR, '.mini-suggest__popup.mini-suggest__popup_theme_flat.mini-suggest__popup_visible')
    SEARCH_RESULTS = (By.XPATH, '//*[@id="search-result"]')
    BLOCK_IMG_LINK = (By.XPATH, "//a[@data-id='images']")
    CATEGORY_LINK = (By.XPATH, "//a[@class='Link PopularRequestList-Preview']")
    OPEN_CATEGORY_CHECK = (By.CLASS_NAME, 'tabs-navigation__tab-over-inner')
    OPEN_FIRST_IMG = (By.XPATH, "//a[@class='serp-item__link']")
    OPENED_IMG = (By.CLASS_NAME, 'MMImage-Origin')
    NEXT_BUTTON = (
        By.XPATH,
        "//div[@class='CircleButton CircleButton_type_next CircleButton_type MediaViewer-Button "
        "MediaViewer_theme_fiji-Button MediaViewer-ButtonNext MediaViewer_theme_fiji-ButtonNext']"
    )
    PREV_BUTTON = (
        By.XPATH,
        "//div[@class='CircleButton CircleButton_type_prev CircleButton_type MediaViewer-Button "
        "MediaViewer_theme_fiji-Button MediaViewer-ButtonPrev MediaViewer_theme_fiji-ButtonPrev']"
    )
