from datetime import datetime

class Base:
    '''Базовый класс, содержит уникальные методы'''

    def __init__(self, driver):
        self._driver = driver


    def get_current_url(self):
        '''Метод для возврата url'''

        get_url = self._driver.current_url
        print(f'Current url: {get_url}')

    def assert_word(self, word, expect_result):
        '''Метод для проверки надписи'''

        value_word = word.text
        assert value_word == expect_result, 'Ошибка! Надпись неверна'
        print('Надпись верна. Проверка пройдена успешно')

    def get_screenshot(self):
        '''Метод для получения скриншота'''

        now_date = datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
        name_screenshot = f"screenshot{now_date}.png"
        self._driver.save_screenshot(f"screen/{name_screenshot}")
        print("Скриншот выполнен")

    def assert_url(self, expect_result):
        '''Метод для проверки надписи'''

        get_url = self._driver.current_url
        assert get_url == expect_result, 'Ошибка! Url неверный'
        print('Url верный. Проверка пройдена успешно')