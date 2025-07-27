from playwright.sync_api import Page

class InventoryPage:
    INVENTORY_LIST = ".inventory_list"
    INVENTORY_ITEM = ".inventory_item"
    CART_BUTTON = ".shopping_cart_link"
    ADD_TO_CART_BUTTON = "//button[@name='add-to-cart-sauce-labs-backpack']"

    def __init__(self, page: Page):
        self.page = page

    def get_inventory_items(self):
        """Возвращает список всех элементов товаров на странице"""
        try:
            return self.page.query_selector_all(self.INVENTORY_ITEM)
        except AttributeError as e:
            raise AttributeError(f"Ошибка при попытке получить товары: {e}")
        except TimeoutError as e:
            raise TimeoutError(f"Таймаут при получении товаров: {e}")

    def get_item_by_name(self, name: str):
        """Возвращает товар по имени"""
        items = self.get_inventory_items()
        for item in items:
            try:
                title = item.query_selector(".inventory-item-name").inner_text()
                if title == name:
                    return item
            except AttributeError:
                continue
        raise ValueError(f"Item с именем '{name}' не найден на странице")

    def add_item_to_cart_by_name(self, name: str):
        """Добавляет товар по имени"""
        item = self.get_item_by_name(name)
        try:
            button = item.query_selector(self.ADD_TO_CART_BUTTON)
            button.click()
        except AttributeError as e:
            raise AttributeError(f"Ошибка при добавлении товара '{name}' в корзину: {e}")

    def add_item_to_cart_by_index(self, index: int = 0):
        """Добавляет товар по индексу"""
        items = self.get_inventory_items()
        if index < 0 or index >= len(items):
            raise IndexError(f"Некорректный индекс {index}, всего товаров: {len(items)}")
        try:
            button = items[index].query_selector(self.ADD_TO_CART_BUTTON)
            button.click()
        except AttributeError as e:
            raise AttributeError(f"Ошибка при добавлении товара №{index}: {e}")

    def go_to_cart(self):
        try:
            self.page.click(self.CART_BUTTON)
        except TimeoutError:
            raise TimeoutError("Кнопка корзины не найдена на странице")
