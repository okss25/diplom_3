from locators.order_history_page_locators import OrderHistoryPageLocators
from pages.base_page import BasePage
import allure


class OrderHistoryPage(BasePage):

    @allure.step('Прогрузка карточки заказа')
    def wait_visibility_of_order_card(self):
        self.wait_visibility_of_element(OrderHistoryPageLocators.order_card)

    @allure.step('Текст карточки заказа')
    def get_text_of_order_card_title(self):
        return self.get_text_on_element(OrderHistoryPageLocators.order_card_title)

    @allure.step('Номер заказа в карточке')
    def get_id_of_order_card(self):
        return self.get_text_on_element(OrderHistoryPageLocators.order_card_id)