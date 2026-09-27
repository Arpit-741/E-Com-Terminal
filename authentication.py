from database import mydb

mycursor = mydb.cursor()

def login():
    u_name= input("Enter ID: ")
    pwd= input("Enter Password: ")

    cursor = mydb.cursor()
   
    query = """
        SELECT * FROM login
        WHERE U_ID = %s AND Password = %s
    """
    mycursor.execute(query, (u_name, pwd))
    result = mycursor.fetchone()

    if result:
        print("Login successful!")
    else:
        print("Invalid username or password.")

    mycursor.close()

def reg():
    u_name = input("Enter User Name: ")
    pwd = input("Enter Your Password: ")
    sql = "INSERT INTO login (U_ID, password) VALUES (%s, %s)"
    val = (u_name, pwd)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    mycursor.close()
    pass
    #return

def logout():
    pass


def authentication():

    print(
        "What would like to do now:", "\n",
        "1. Login", "\n",
        "2. Register", "\n",
        "3. Logout", "\n",
        "4. Exit", "\n",
        )

    op = int(input("Enter Option: "))
    match op:
        case 1:
            login()
            print("Okay")

        case 2:
            reg()
            print("Done")

        case 3:
            pass

        case 4:
            pass
