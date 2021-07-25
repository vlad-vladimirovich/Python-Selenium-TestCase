import unittest
from selenium import webdriver


class BaseTest(unittest.TestCase):
    """ Класс содержит базовые функции для тестов """

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://yandex.ru/')

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(BaseTest)
    unittest.TextTestRunner(verbosity=1).run(suite)
