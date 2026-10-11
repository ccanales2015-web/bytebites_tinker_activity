from models import Customer, FoodItem, Menu, Transaction

# Create sample food items
burger = FoodItem("Spicy Burger", 8.99, "Burgers", 4.5)
soda = FoodItem("Large Soda", 2.49, "Drinks", 4.1)

# Create a menu and transaction
menu = Menu()
transaction = Transaction()

# Create a customer
customer = Customer("Alex")

# Inspect stored attributes
print("Food item:", vars(burger))
print("Second food item:", vars(soda))
print("Menu items:", menu.items)
print("Transaction items:", transaction.items)
print("Customer:", vars(customer))


# Helper: turn a list of FoodItem objects into a list of their names
def item_names(items):
    names = []
    for item in items:
        names.append(item.name)
    return names


# --- Menu: add_item() ---
# Add the lower-rated soda BEFORE the higher-rated burger
menu.add_item(soda)
menu.add_item(burger)
print("\nMenu after adding items:", item_names(menu.items))
print("  Expected: ['Large Soda', 'Spicy Burger']")

# --- Menu: filter_by_category() ---
print("\nFilter 'Drinks':", item_names(menu.filter_by_category("Drinks")))
print("  Expected: ['Large Soda']")
print("Filter 'Pizza':", item_names(menu.filter_by_category("Pizza")))
print("  Expected: []")

# --- Menu: sort_by_popularity() ---
print("\nSorted by popularity:", item_names(menu.sort_by_popularity()))
print("  Expected: ['Spicy Burger', 'Large Soda']")
print("Original menu after sorting:", item_names(menu.items))
print("  Expected: ['Large Soda', 'Spicy Burger']  (unchanged)")
print("Empty menu sorted:", Menu().sort_by_popularity())
print("  Expected: []")

# --- Transaction: add_item() and compute_total() ---
print("\nEmpty transaction total:", transaction.compute_total())
print("  Expected: 0.0")
transaction.add_item(burger)
transaction.add_item(soda)
print("Transaction items:", item_names(transaction.items))
print("  Expected: ['Spicy Burger', 'Large Soda']")
print("Transaction total:", transaction.compute_total())
print("  Expected: about 11.48")

# --- Customer: add_purchase() and is_verified() ---
print("\nVerified before any purchase:", customer.is_verified())
print("  Expected: False")
customer.add_purchase(transaction)
print("Verified after one purchase:", customer.is_verified())
print("  Expected: True")