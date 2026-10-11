# ByteBites - Class Models
#
# Customer: Stores a customer's name and purchase history.
# FoodItem: Stores a food item's name, price, category, and popularity rating.
# Menu: Maintains a collection of food items and supports category filtering.
# Transaction: Stores selected food items and calculates their total cost.


class FoodItem:
    """A single item for sale, such as a "Spicy Burger" or "Large Soda"."""

    def __init__(
        self,
        name: str,
        price: float,
        category: str,
        popularity_rating: float,
    ) -> None:
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating


class Menu:
    """The full collection of food items, filterable by category."""

    def __init__(self) -> None:
        self.items: list[FoodItem] = []

    def add_item(self, item: FoodItem) -> None:
        """Add a food item to the menu."""
        pass

    def filter_by_category(self, category: str) -> list[FoodItem]:
        """Return the menu items that belong to the given category."""
        pass


class Transaction:
    """A group of selected food items with a computed total cost."""

    def __init__(self) -> None:
        self.items: list[FoodItem] = []

    def add_item(self, item: FoodItem) -> None:
        """Add a selected food item to this transaction."""
        pass

    def compute_total(self) -> float:
        """Return the sum of the prices of all items in this transaction."""
        pass


class Customer:
    """A user tracked by name and past purchase history."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.purchase_history: list[Transaction] = []

    def add_purchase(self, transaction: Transaction) -> None:
        """Record a transaction in this customer's purchase history."""
        pass

    def is_verified(self) -> bool:
        """Return True if the customer is a real user.

        Design assumption: a customer is verified if their purchase_history
        contains at least one transaction.
        """
        pass