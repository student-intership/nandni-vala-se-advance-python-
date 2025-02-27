import pymysql

mydb = pymysql.connect(host="localhost", user="root", password="", database="student01")
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
        subject = input("Enter Subject: ")
        mobile_no = input("Enter Mobile Number: ")

        try:
            query = "INSERT INTO  student(name, subject, mobile_no) VALUES (%s, %s, %s)"
            args = (name, subject, mobile_no)
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
        subject = input("Enter Updated Subject: ")

        try:
            query = "UPDATE student SET name = %s, subject = %s WHERE id = %s"
            args = (name, subject, id)
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
            query = "DELETE FROM student WHERE id = %s"
            args = (id,)
            mycursor.execute(query, args)
            mydb.commit()
            print("Data Deleted!!")
        except pymysql.MySQLError as e:
            print("Error while deleting data:", e)

    elif ch == 4:
        try:
            query = "SELECT * FROM student "
            mycursor.execute(query)
            data = mycursor.fetchall()

            if data:
                print(f"{'ID':<5} {'Name':<15} {'Subject':<15} {'Mobile No':<15}")
                print("-" * 50)
                for row in data:
                    print(f"{row[0]:<5} {row[1]:<15} {row[2]:<15} {row[3]:<15}")
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

