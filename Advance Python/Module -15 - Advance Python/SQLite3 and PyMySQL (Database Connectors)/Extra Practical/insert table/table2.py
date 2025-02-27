import pymysql

mydb = pymysql.connect(host="localhost", user="root", password="", database="Table1")
mycursor = mydb.cursor()

while True:
    menu = """
    press 1 for insert data
    press 2 for update data
    press 3 for delete data
    press 4 for fetch data
    press 5 for exit
    """
    print(menu)

    try:
        ch = int(input("Enter Choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if ch == 1:
        name = input("Enter Name: ")
        salary = input("Enter Salary: ")
        

        try:
            query = "INSERT INTO  table1(name, salary) VALUES (%s, %s)"
            args = (name, salary)
            mycursor.execute(query, args)
            mydb.commit()
            print("Data Inserted!!")
        except pymysql.MySQLError as e:
            print("Error while inserting data:", e)

    elif ch == 2:
        try:
            id = int(input("Enter ID for updating data: "))
        except ValueError:
            print("Invalid ID. Please enter a number.")
            continue

        name = input("Enter Updated Name: ")
        salary = input("Enter Updated salary: ")

        try:
            query = "UPDATE table1 SET name = %s, salary = %s WHERE id = %s"
            args = (name, salary, id)
            mycursor.execute(query, args)
            mydb.commit()
            print("Data Updated!!")
        except pymysql.MySQLError as e:
            print("Error while updating data:", e)


    elif ch == 3:
        try:
            id = int(input("Enter ID to delete: "))
        except ValueError:
            print("Invalid ID. Please enter a number.")
            continue

        try:
            query = "DELETE FROM table1 WHERE id = %s"
            args = (id,)
            mycursor.execute(query, args)
            mydb.commit()
            print("Data Deleted!!")
        except pymysql.MySQLError as e:
            print("Error while deleting data:", e)

    elif ch == 4:
        try:
            query = "SELECT * FROM table1"
            mycursor.execute(query)
            data = mycursor.fetchall()

            if data:
                print(f"{'ID':<5} {'Name':<15} {'Salary':<15}")
                print("-" * 40)
                for row in data:
                    print(f"{row[0]:<5} {row[1]:<15} {row[2]:<15}")
            else:
                print("No data found!")
        except pymysql.MySQLError as e:
            print("Error while fetching data:", e)

    elif ch == 5:
        print("Thank You!")
        mycursor.close()
        mydb.close()
        break

    else:
        print("Invalid Choice!")

