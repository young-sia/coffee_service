import sqlite3

# Connect to the database
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Check questions
cursor.execute("SELECT id, text, 'order' FROM core_question ORDER BY 'order'")
questions = cursor.fetchall()

print(f"Total questions in database: {len(questions)}\n")
for q in questions:
    print(f"{q[2]}. {q[1]}")

conn.close()
