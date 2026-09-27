import mysql.connector
from backend.authentication import authentication
from backend.database import mydb

print(
    "Hello! Welcome to the E-Comm", "\n",
    "What would you like to do:", "\n",
    "1. Login", "\n",
    "2. Product Catalog", "\n",
    "3. Search Product", "\n",
    "4. Manage Cart", "\n",
    )

Q= int(input("Enter Task No.: "))
match Q:
    case 1:
        authentication()

    case 2:
        pass

    case 3:
        pass

    case 4:
        pass

    case _:
        print("Invalid Request")
