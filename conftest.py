import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    """
    Добавляем возможность передавать язык в командной строке
    Пример: pytest --language=es test_items.py
    """
    parser.addoption('--language',
                     action='store',
                     default='en',
                     help="Choose language: es, fr, ru, etc.")


@pytest.fixture(scope="function")
def browser(request):
    """
    Фикстура для создания браузера с указанным языком
    """
    # Получаем язык из командной строки
    user_language = request.config.getoption("language")

    # Настраиваем опции Chrome
    options = Options()
    options.add_experimental_option('prefs', {
        'intl.accept_languages': user_language
    })

    print(f"\nЗапускаем браузер с языком: {user_language}")
    browser = webdriver.Chrome(options=options)

    # Передаем браузер тесту
    yield browser

    # Закрываем браузер после теста
    print("\nЗакрываем браузер")
    browser.quit()