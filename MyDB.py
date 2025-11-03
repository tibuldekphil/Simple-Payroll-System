import mysql.connector
from tkinter import messagebox

def Database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="payroll_system"
    )

#== Used in Register Company Module ===
def insert_Company(company, address, email, tel):
    db = Database()
    cursor = db.cursor()
    try:
        command_Insert_company = """
        INSERT INTO company (name, address, email, telephone)
        VALUES (%s, %s, %s, %s)
        """
        company_values = (company, address, email, tel)
        cursor.execute(command_Insert_company, company_values)
        db.commit()

        company_id = cursor.lastrowid

        create_admin_query = """
        INSERT INTO user_account (company_id, username, password_hash, user_type)
        VALUES (%s, %s, %s, %s)
        """

        Default_account = (company_id, "admin", "admin123", "admin")
        cursor.execute(create_admin_query, Default_account)
        db.commit()

        messagebox.showinfo("Success", 
                            "Company registered successfully!\n\n"
                            f"Company ID: {company_id}\n"
                            f"Default Admin Account:\n"
                            f"  Username: admin\n"
                            f"  Password: admin123"
        )

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
    finally:
        cursor.close()
        db.close()