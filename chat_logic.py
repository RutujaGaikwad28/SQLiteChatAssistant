
import sqlite3

def process_query(user_input):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    try:
        user_input = user_input.lower().strip().replace('.', '').strip()

        if "show me all employees in" in user_input:
            dept = user_input.split("show me all employees in")[-1].strip().replace("department", "").strip()
            cursor.execute("SELECT Name FROM Employees WHERE LOWER(Department) LIKE ?", ('%' + dept + '%',)) #Added % for partial matching
            result = cursor.fetchall()
            return format_employee_list(result, dept)

        elif "who is the manager of" in user_input:
            dept = user_input.split("who is the manager of")[-1].strip().replace("department", "").strip()
            cursor.execute("SELECT Manager FROM Departments WHERE LOWER(Name) LIKE ?", ('%' + dept + '%',))
            result = cursor.fetchone()
            return format_manager(result, dept)

        elif "list all employees hired after" in user_input:
            date = user_input.split("list all employees hired after")[-1].strip()
            cursor.execute("SELECT Name FROM Employees WHERE Hire_Date > ?", (date,))
            result = cursor.fetchall()
            return format_employee_list(result, date, hired_after=True)

        elif "what is the total salary expense for" in user_input:
            dept = user_input.split("what is the total salary expense for")[-1].strip().replace("department", "").strip()
            cursor.execute("SELECT SUM(Salary) FROM Employees WHERE LOWER(Department) LIKE ?", ('%' + dept + '%',))
            result = cursor.fetchone()
            return format_salary_expense(result, dept)

        else:
            return "Sorry, I didn't understand that query. Please try again."

    except Exception as e:
        return f"Error processing query: {str(e)}"

    finally:
        conn.close()

def format_employee_list(result, dept, hired_after=False):
    if result:
        employee_names = ", ".join([row[0] for row in result])
        if hired_after:
            return f"Employees hired after {dept}: {employee_names}"
        else:
            return f"Employees in {dept.capitalize()}: {employee_names}"
    else:
        if hired_after:
             return f"No employees hired after {dept}."
        else:
            return f"No employees found in {dept.capitalize()} department."


def format_manager(result, dept):
    if result:
        return f"The manager of {dept.capitalize()} is {result[0]}."
    else:
        return f"Department {dept.capitalize()} not found."

def format_salary_expense(result, dept):
    if result and result[0] is not None:  # Check for None result
        return f"Total salary expense for {dept.capitalize()}: {result[0]}"
    else:
        return f"Department {dept.capitalize()} not found or no salary data available."























# # chat_logic.py
# import sqlite3

# def process_query(user_input):
#     conn = sqlite3.connect('database.db')
#     cursor = conn.cursor()

#     try:
#         user_input = user_input.lower().strip().replace('.', '').strip()

#         if "show me all employees in" in user_input:
#             dept = user_input.split("show me all employees in")[-1].strip().replace("department", "").strip()
#             cursor.execute("SELECT Name FROM Employees WHERE LOWER(Department) LIKE ?", ('%' + dept + '%',))
#             result = cursor.fetchall()
#             return format_employee_list(result, dept)

#         elif "who is the manager of" in user_input:
#             dept = user_input.split("who is the manager of")[-1].strip().replace("department", "").strip()
#             cursor.execute("SELECT Manager FROM Departments WHERE LOWER(Name) LIKE ?", ('%' + dept + '%',))
#             result = cursor.fetchone()
#             return format_manager(result, dept)

#         elif "list all employees hired after" in user_input:
#             date = user_input.split("list all employees hired after")[-1].strip()
#             cursor.execute("SELECT Name FROM Employees WHERE Hire_Date > ?", (date,))
#             result = cursor.fetchall()
#             return format_employee_list(result, date, hired_after=True)

#         elif "what is the total salary expense for" in user_input:
#             dept = user_input.split("what is the total salary expense for")[-1].strip().replace("department", "").strip()
#             cursor.execute("SELECT SUM(Salary) FROM Employees WHERE LOWER(Department) LIKE ?", ('%' + dept + '%',))
#             result = cursor.fetchone()
#             return format_salary_expense(result, dept)

#         else:
#             return "Sorry, I didn't understand that query. Please try again."

#     except Exception as e:
#         return f"Error processing query: {str(e)}"

#     finally:
#         conn.close()

# def format_employee_list(result, dept, hired_after=False):
#     if result:
#         employee_names = ", ".join([row[0] for row in result])
#         if hired_after:
#             return f"Employees hired after {dept}: {employee_names}"
#         else:
#             return f"Employees in {dept.capitalize()}: {employee_names}"
#     else:
#         if hired_after:
#              return f"No employees hired after {dept}."
#         else:
#             return f"No employees found in {dept.capitalize()} department."


# def format_manager(result, dept):
#     if result:
#         return f"The manager of {dept.capitalize()} is {result[0]}."
#     else:
#         return f"Department {dept.capitalize()} not found."

# def format_salary_expense(result, dept):
#     if result and result[0] is not None:
#         return f"Total salary expense for {dept.capitalize()}: {result[0]}"
#     else:
#         return f"Department {dept.capitalize()} not found or no salary data available."