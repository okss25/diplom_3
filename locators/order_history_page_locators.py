from selenium.webdriver.common.by import By


class OrderHistoryPageLocators:
    # Карточка заказа в истории заказов
    order_card = (By.CSS_SELECTOR, '.OrderHistory_listItem')
    # Заголовок карточки заказа с названием бургера
    order_card_title = (By.CSS_SELECTOR, '.OrderHistory_listItem h2')
    # Номер заказа в карточке заказа
    order_card_id = (By.CSS_SELECTOR, '.OrderHistory_textBox p.text_type_digits-default')