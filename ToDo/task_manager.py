from database import get_connection

# ------------------ USERS ------------------ #
def create_user(name, email, password):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", 
                       (name, email, password))
        conn.commit()

def get_user_by_email(email):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        return cursor.fetchone()

# ------------------ TASKS ------------------ #
def add_task(title, description, due_date, user_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (title, description, due_date, user_id) VALUES (?, ?, ?, ?)", 
                       (title, description, due_date, user_id))
        conn.commit()

def list_tasks(user_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, status, due_date FROM tasks WHERE user_id = ?", (user_id,))
        return cursor.fetchall()

def update_task_status(task_id, status):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (status, task_id))
        conn.commit()

def delete_task(task_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
