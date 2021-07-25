from tests.base_test import BaseTest
from pages.main_page import *


class TestYandexSearch(BaseTest):

    def test_search(self):
        page = MainPage(self.driver)  # Переходим на яндекс
        page.find_object()  # Проверяем наличие поля поиска, ввод в поиск 'Тензор'
        page.find_suggest()  # Проверяем наличие таблицы с подсказками
        page.results()  # Проверяем наличие результатов поиска
        page.first_five_results()  # Проверяем условие в первых 5 результатах есть ссылка на 'tensor.ru'


class TestYandexImages(BaseTest):

    def test_images(self):
        page = MainPage(self.driver)  # Переходим на яндекс
        page.block_img_link()  # Ссылка картинки присутствует на странице, нажимаем
        assert page.get_current_url() == 'https://yandex.ru/images/?utm_source=main_stripe_big', (
            'URL не соответствует')  # Проверяем, что перешли
        page.open_category()  # Открываем первую категорию
        result = page.open_category_check()
        self.assertIn('Картинки', result)  # Проверяем что открылась
        page.first_img()  # Открыть первую картинку
        page.opened_image()  # Проверяем, что открылась
        url = page.get_current_url()
        page.next_button()  # Жмём вперед
        assert page.get_current_url() != url, (
            'Картинка не изменилась')  # При нажатии кнопки вперед, картинка изменяется
        page.prev_button()  # Жмём назад
        assert page.get_current_url() == url, (
            'Не первая картинка')  # Картинка изменяется на изображение из шага 6
        page.check_image()  # Проверяем, что эта та же картинка
