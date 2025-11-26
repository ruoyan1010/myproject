import mysql.connector

def load_users():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        database="testdb"
    )
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(50)
        )
    """)

    cursor.execute("INSERT INTO users(name) VALUES ('Alice'), ('Bob')")
    conn.commit()

    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    print("Users in DB:", rows)

    conn.close()

if __name__ == "__main__":
    load_users()
