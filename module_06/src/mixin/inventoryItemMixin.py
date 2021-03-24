"""Item mixin methods"""


class InventoryItemMixin:
    """Inventory item mixin"""

    __ADDED_LABEL = 'ADD TO CART'

    __REMOVE_LABEL = 'REMOVE'

    def get_title(self) -> str:
        """Get title for item."""
        return self._title.get_text()

    def get_description(self) -> str:
        """Get description."""
        return self._description.get_text()

    def get_price(self) -> str:
        """Get price."""
        return self._price.get_text()

    def is_in_the_cart(self) -> str:
        """Get item status"""
        return self._inv_btn.get_text() == InventoryItemMixin.__REMOVE_LABEL

    def add_to_cart(self):
        """Add to cart."""
        if self._inv_btn.get_text() == InventoryItemMixin.__ADDED_LABEL:
            self._inv_btn.click()
        else:
            raise ValueError(f'Inventory item is already in the cart')

    def remove_from_cart(self):
        """Remove from cart."""
        if self._inv_btn.get_text() == InventoryItemMixin.__REMOVE_LABEL:
            self._inv_btn.click()
        else:
            raise ValueError(f'Inventory item is not in the cart')