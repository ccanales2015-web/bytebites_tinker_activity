import pytest

from models import Customer, FoodItem, Menu, Transaction


# R1: A transaction containing a Spicy Burger (8.99) and a Large Soda (2.49)
# should compute a total equal to the sum of their prices, about 11.48.
def test_compute_total_with_multiple_items():
    burger = FoodItem("Spicy Burger", 8.99, "Burgers", 4.5)
    soda = FoodItem("Large Soda", 2.49, "Drinks", 4.1)
    transaction = Transaction()
    transaction.add_item(burger)
    transaction.add_item(soda)

    assert transaction.compute_total() == pytest.approx(11.48)


# R2: A new transaction with no items should compute a total of 0.0,
# not None or an error.
def test_compute_total_empty_transaction_returns_zero():
    transaction = Transaction()

    assert transaction.compute_total() == 0.0


# R3: Filtering a menu by "Drinks" should return only the items in the
# "Drinks" category, in menu order, so a menu with a Large Soda, a Spicy
# Burger, and a Lemonade should return the Large Soda and the Lemonade.
def test_filter_by_category_returns_only_matching_items():
    soda = FoodItem("Large Soda", 2.49, "Drinks", 4.1)
    burger = FoodItem("Spicy Burger", 8.99, "Burgers", 4.5)
    lemonade = FoodItem("Lemonade", 1.99, "Drinks", 3.8)
    menu = Menu()
    menu.add_item(soda)
    menu.add_item(burger)
    menu.add_item(lemonade)

    assert menu.filter_by_category("Drinks") == [soda, lemonade]


# O1: Filtering a menu by a category that no item belongs to, such as
# "Pizza", should return an empty list rather than None or an error.
def test_filter_by_category_no_matches_returns_empty_list():
    burger = FoodItem("Spicy Burger", 8.99, "Burgers", 4.5)
    soda = FoodItem("Large Soda", 2.49, "Drinks", 4.1)
    menu = Menu()
    menu.add_item(burger)
    menu.add_item(soda)

    assert menu.filter_by_category("Pizza") == []


# O2: Sorting a menu by popularity should return the items from highest to
# lowest rating, so a Large Soda (4.1), a Chocolate Cake (4.8), and a Spicy
# Burger (4.5) should come back as the cake, then the burger, then the soda.
def test_sort_by_popularity_orders_highest_first():
    soda = FoodItem("Large Soda", 2.49, "Drinks", 4.1)
    cake = FoodItem("Chocolate Cake", 4.99, "Desserts", 4.8)
    burger = FoodItem("Spicy Burger", 8.99, "Burgers", 4.5)
    menu = Menu()
    menu.add_item(soda)    # lower rating added first
    menu.add_item(cake)
    menu.add_item(burger)

    assert menu.sort_by_popularity() == [cake, burger, soda]


# O3: Sorting a menu by popularity should not change the menu itself, so
# after sorting, the menu's items should still be in the order they were
# added: the Large Soda first, then the Spicy Burger.
def test_sort_by_popularity_does_not_change_menu():
    soda = FoodItem("Large Soda", 2.49, "Drinks", 4.1)
    burger = FoodItem("Spicy Burger", 8.99, "Burgers", 4.5)
    menu = Menu()
    menu.add_item(soda)
    menu.add_item(burger)

    menu.sort_by_popularity()

    assert menu.items == [soda, burger]


# O4: Following Design Assumption 1, a customer is verified only if their
# purchase history contains at least one transaction, so a new customer
# with no purchases should not be verified.
def test_new_customer_is_not_verified():
    customer = Customer("Alex")

    assert customer.is_verified() is False


# O5: Following Design Assumption 1, a customer is verified once their
# purchase history contains at least one transaction, even if that
# transaction has no food items, so recording one purchase should make
# the customer verified.
def test_customer_is_verified_after_one_purchase():
    customer = Customer("Alex")
    transaction = Transaction()

    customer.add_purchase(transaction)

    assert customer.is_verified() is True
