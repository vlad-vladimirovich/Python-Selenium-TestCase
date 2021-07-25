from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from utils import locators
import time


class MainPage(BasePage):
    """ Производный от класса "BasePage". Он содержит методы,
    которые будут использоваться для создания шагов тестирования
    """

    def __init__(self, driver):
        self.locator = locators.MainPageLocators
        super().__init__(driver)

    def find_object(self):
        """ Проверяет наличие поля поиска, вводит в поиск 'Тензор' """
        global searchbar
        searchbar = self.find_element(*self.locator.SEARCH_BAR)
        time.sleep(2)
        searchbar.send_keys('Тензор')
        time.sleep(2)

    def find_suggest(self):
        """ Проверяет наличие таблицы с подсказками """
        self.find_element(*self.locator.SUGGEST_LIST)
        searchbar.send_keys(Keys.ENTER)
        time.sleep(2)

    def results(self):
        """ Проверяет наличие рузальтатов поиска """
        self.find_element(*self.locator.SEARCH_RESULTS)
        time.sleep(2)

    def first_five_results(self):
        """ Проверяет наличие нужных ссылок """
        links = self.driver.find_elements_by_xpath("//div[@class='Path Organic-Path path organic__path']/a")[:5]
        for elem in links:
            if elem.get_attribute("href") == "https://tensor.ru/":
                break
        time.sleep(2)

    def block_img_link(self):
        """ Проверяет наличие ссылки """
        self.find_element(*self.locator.BLOCK_IMG_LINK).click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def open_category(self):
        """ Открывает нужную категорию """
        self.find_element(*self.locator.CATEGORY_LINK).click()
        time.sleep(2)

    def open_category_check(self):
        """ Получает название категории """
        self.find_element(*self.locator.OPEN_CATEGORY_CHECK)
        return self.find_element(*self.locator.OPEN_CATEGORY_CHECK).text

    def first_img(self):
        """ Открывает картинку """
        self.find_element(*self.locator.OPEN_FIRST_IMG).click()
        time.sleep(2)

    def opened_image(self):
        """ Получает ссылку открытой картинки """
        global first_src
        links = self.find_element(*self.locator.OPENED_IMG)
        first_src = links.get_attribute('src')
        time.sleep(2)

    def next_button(self):
        """ Нажатие кнопки 'далее' """
        self.find_element(*self.locator.NEXT_BUTTON).click()
        time.sleep(2)

    def prev_button(self):
        """ Нажатие кнопки 'назад' """
        self.find_element(*self.locator.PREV_BUTTON).click()
        time.sleep(2)

    def check_image(self):
        """ Получает ссылку текущей картинки,
        сравнивает её и ранее открытую ссылки
        """
        links = self.find_element(*self.locator.OPENED_IMG)
        current_src = links.get_attribute('src')
        assert first_src == current_src, (
            'Это другая картинка')
