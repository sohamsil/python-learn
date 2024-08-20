from dotenv import load_dotenv
import os
import psycopg2 as db

def insert_rows(cur,conn):
    try: 
        print("Enter following values :\n")
        name = input("Name : ")
        street = input("Street : ")
        city = input("City : ")
        zip = input("Zip : ")

        query = "INSERT INTO users (name,street,city,zip) VALUES(%s,%s,%s,%s) RETURNING *"
        data = (name,street,city,zip)
        
        # cur.mogrify(query,data)
        cur.execute(query,data)
        conn.commit()

        print("Insertion completed!\n\n")

    except Exception as e:
        print("Data insertion error : {}" .format(e))

def read_rows(cur):
    try:
        print("Choose following option :\n")
        userio = input("1 Read all rows\n2 Read one row\n")
        match userio:
            case "1":
                query = "SELECT * FROM users"
            case "2":
                userid = input("Enter User ID : ")
                query = f"SELECT * FROM users WHERE id ={userid}"
            case _:
                print("Wrong input!")
                exit
        
        cur.execute(query)
        output = cur.fetchall()

        if not output:
            print("User ID not found!")
        else:
            print("Output:\n")
            for row in output:
                print(row)
        
    except Exception as e:
        print(e)

def delete_rows(cur,conn):
    try:
        delete = True

        while delete :
            userio = input("Enter User ID for deletetion : ")

            searchQuery = f"SELECT id FROM users WHERE id={userio}"
            cur.execute(searchQuery)
            if cur.fetchall():
                deleteQuery = f"DELETE FROM users WHERE id={userio}"
                cur.execute(deleteQuery)
                conn.commit()
                print("Deletion completed!\n\n")
                delete = False
            else :
                print("User not found!")

    except Exception as e:
        print(e) 

if __name__ == "__main__":
    
    # Load environment variables from dotenv
    load_dotenv()

    # Read DB conection details from dotenv
    DB_NAME = os.getenv('DB_NAME')
    DB_HOST = os.getenv('DB_HOST')
    DB_USERNAME = os.getenv('DB_USERNAME')
    DB_PASSWORD = os.getenv('DB_PASSWORD')

    # Create connection to database
    conn_string = f"host={DB_HOST} dbname={DB_NAME} user={DB_USERNAME} password={DB_PASSWORD}"

    conn = db.connect(conn_string)
    cur = conn.cursor()


    # Take input from user
    userio = ''

    while userio != '4':
        userio = input("Input choice from below:\n1 Insert Data \n2 Read Data \n3 Delete Data \n4 Enter 4 to exit\n")

        match userio:
            case "1":
                insert_rows(cur,conn)
            case "2":
                read_rows(cur)
            case "3":
                delete_rows(cur,conn)
            case "4":
                print("Exit") 
                cur.close()
                conn.close()
                exit
            case _:
                print("Wrong input!") 


    