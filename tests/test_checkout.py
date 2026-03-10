# Import the Checkout class
from src.checkout import Checkout


# Test that the total is 0 when no items are scanned
def test_total_is_0_when_no_items_scanned():
    # Arrange
    checkout = Checkout()

    # Act
    total = checkout.total()

    # Assert
    assert total == 0
