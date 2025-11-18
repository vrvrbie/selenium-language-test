from selenium.webdriver.common.by import By


def test_add_to_cart_button_presence(browser):
    """
    Тест проверяет наличие кнопки добавления в корзину на странице товара
    """
    # Открываем страницу товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    # ДЛЯ ПРОВЕРКИ ЗАДАНИЯ - РАСКОММЕНТИРУЙТЕ СЛЕДУЮЩУЮ СТРОКУ:
    # import time; time.sleep(30)

    # Ищем кнопку добавления в корзину по уникальному селектору
    add_to_cart_button = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")

    # Проверяем, что кнопка существует на странице
    assert len(add_to_cart_button) > 0, "Кнопка добавления в корзину не найдена на странице"

    # Проверяем, что кнопка отображается
    assert add_to_cart_button[0].is_displayed(), "Кнопка добавления в корзину не отображается"

    # Дополнительно: выводим текст кнопки для отладки
    button_text = add_to_cart_button[0].text
    print(f"Найдена кнопка с текстом: '{button_text}'")