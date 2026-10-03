
products = [
    {
        "name":"notebook",
        "category":"school supplies",
        "quantity":20,
        "price":40
    },
    {
        "name":"pencil",
        "category":"school supplies",
        "quantity":40,
        "price":15
    }
]

def add_product(products):
    user_input = input("Enter product name: ").lower()

    for product in products:
        if product["name"].lower() == user_input:
            print(f"The {user_input} already exists in the products.")

            add = int(input("Enter add quantity: "))

            product["quantity"] += add

            print(f"New total quantity: {product['quantity']}")
            return

    category = input("Enter category: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))

    product = {
        "name": user_input,
        "category": category,
        "quantity": quantity,
        "price": price
    }

    products.append(product)

    print("Product added successfully.")

def view_product(products):
    for number, product in enumerate(products, start=1):
        print(f"{number}. {product["name"]}")

    choice = input("Enter the name of the product: ").lower()
    for product in products:
        if choice == product["name"]:
            print(f"name:{product['name']}\ncategory:{product['category']}\nwuantity:{product['quantity']}\nprice:{product["price"]}")

def search_product(products):
    pass

def update_product(products):
    pass

def delete_product(products):
    pass

def menu():
    print("="*20)
    print("SCHOOL SUPPLY INVENTORY SYSTEM".center(20))
    print("="*20)

    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. Exit")




def main(products):
    while True:

        menu()

        choice = input("Choose:")

        if choice == "1":
            add_product(products)
        elif choice == "2":
            view_product(products)
        elif choice == "3":
            search_product(products)
        elif choice =="4":
            update_product(products)
        elif choice == "5":
            delete_product(products)
        elif choice == "6":
            break
        else:
            print("Invalid choice")

main(products)
