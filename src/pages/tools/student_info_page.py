from src.pages.base_page import BasePage


class StudentInfoPage(BasePage):
    """Student info create, edit, delete, and search workflows."""

    def search_student(self, keyword):
        self.type(("css selector", "input[placeholder*='Search'], input[placeholder*='검색']"), keyword)
        return self
