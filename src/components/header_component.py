from src.components.menu_component import MenuComponent
from src.pages.base_page import BasePage


class HeaderComponent(BasePage):
    """Header area interactions shared across authenticated pages."""

    def open_profile_menu(self):
        MenuComponent(self.driver, timeout=self.timeout, locale=self.locale).open_header_profile_menu()
        return self
