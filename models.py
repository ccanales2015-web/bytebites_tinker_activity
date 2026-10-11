# ByteBites - Class Models
#
# Customer: Stores a customer's name and purchase history and checks
#           whether the customer is verified.
# FoodItem: Stores a food item's name, price, category, and popularity rating.
# Menu: Maintains a collection of food items and supports category filtering
#       and popularity sorting (sorting is an activity-driven addition).
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
    """All food items, filterable by category and sortable by popularity."""

    def __init__(self) -> None:
        self.items: list[FoodItem] = []

    def add_item(self, item: FoodItem) -> None:
        """Add a food item to the menu."""
        self.items.append(item)

    def filter_by_category(self, category: str) -> list[FoodItem]:
        """Return the menu items that belong to the given category."""
        matching_items = []
        for item in self.items:
            if item.category == category:
                matching_items.append(item)
        return matching_items

    def sort_by_popularity(self) -> list[FoodItem]:
        """Return a new list of menu items sorted by popularity rating, highest first."""
        return sorted(self.items, key=lambda item: item.popularity_rating, reverse=True)


class Transaction:
    """A group of selected food items with a computed total cost."""

    def __init__(self) -> None:
        self.items: list[FoodItem] = []

    def add_item(self, item: FoodItem) -> None:
        """Add a selected food item to this transaction."""
        self.items.append(item)

    def compute_total(self) -> float:
        """Return the sum of the prices of all items in this transaction."""
        total = 0.0
        for item in self.items:
            total = total + item.price
        return total


class Customer:
    """A user tracked by name and purchase history, with verification."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.purchase_history: list[Transaction] = []

    def add_purchase(self, transaction: Transaction) -> None:
        """Record a transaction in this customer's purchase history."""
        self.purchase_history.append(transaction)

    def is_verified(self) -> bool:
        """Return True if the customer is a real user.

        Design assumption: a customer is verified if their purchase_history
        contains at least one transaction.
        """
        return len(self.purchase_history) > 0