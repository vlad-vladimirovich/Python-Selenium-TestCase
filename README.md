## Предисловие
Этот репозиторий содержит базовый пример использования PageObject паттерн с Selenium Webdriver и Python unittest

Когда вы хотите написать тесты, вы должны вывести свой тестовый класс из `BaseTest`, который содержит базовые функции для ваших тестов. Затем вы можете вызвать страницу и связанные с ней методы в соответствии с шагами в тестовых случаях
```php
class TestYandexSearch(BaseTest):

    def test_search(self):
        page = MainPage(self.driver)
        page.find_object()
```
## Информация
1) Версия Python 3.8.10
2) Бразуер GoogleChrome версия 91.0.4472.101


## Инструкция по запуску тестов

1) Установить requirements.txt:

    ```bash
    pip3 install -r requirements
    ```
2) Загрузить Selenium WebDriver https://chromedriver.chromium.org/downloads (выберите версию, совместимую с вашим браузером)
3) Если вы хотите запустить все тесты, вам следует ввести:

    ```bash
    python -m unittest
    ```
3) Если вы хотите запустить только класс, вам следует ввести:

    ```bash
    python -m unittest tests.test_yandex.TestYandexSearch or TestYandexImages
    ```
    
