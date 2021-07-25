class BasePage(object):
    """ Класс включает в себя базовый функционал и инициализацию драйвера """

    def __init__(self, driver, base_url='https://yandex.ru/'):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    def find_element(self, *locator):
        """ Возвращает искомый элемент """
        return self.driver.find_element(*locator)

    def open(self, url):
        """ Открывает необходимую веб-страницу """
        url = self.base_url + url
        self.driver.get(url)

    def get_current_url(self):
        """ Возвращает текущий url веб-страницы """
        return self.driver.current_url
