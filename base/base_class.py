

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
