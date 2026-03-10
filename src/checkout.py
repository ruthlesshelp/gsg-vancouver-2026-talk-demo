"""Checkout implementation for the checkout system."""


class Checkout:
    def scan(self, sku: str) -> None:
        """Scan an item by its SKU."""
        raise NotImplementedError("Checkout.scan() not implemented")

    def total(self) -> int:
        """Get the total amount rounded to the nearest penny."""
        raise NotImplementedError("Checkout.total() not implemented")
