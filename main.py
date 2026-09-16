print(
    "Hello! Welcome to the E-Comm"
    "What would you like to do:" \
    "1. Login" \
    "2. Product Catalog" \
    "3. Search Product" \
    "4. Manage Cart"
    )

Q= input("Enter Task Name: ")
match Q:
    case 1:
        print("Okay")
    case _:
        print("Invalid Request!")

