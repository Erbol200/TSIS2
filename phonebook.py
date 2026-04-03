# phonebook.py
from connect import get_connection

conn = get_connection()
cur = conn.cursor()

# 1. Добавляем контакты
cur.execute("CALL upsert_contact(%s, %s, %s)", ('Ali', 'Khan', '87001234567'))
cur.execute("CALL upsert_contact(%s, %s, %s)", ('Bob', 'Smith', '87771234567'))
conn.commit()

# 2. Вставка массива контактов
cur.execute(
    "CALL bulk_insert_contacts(%s, %s, %s)",
    (['Mike', 'Sara'], ['Tyson', 'Connor'], ['1234567890', 'abc123'])
)
conn.commit()

# 3. Выборка с поиском
cur.execute("SELECT * FROM search_contacts(%s)", ('Ali',))
rows = cur.fetchall()
print("Search result:", rows)

# 4. Пагинация
cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (2, 0))
rows = cur.fetchall()
print("Paginated:", rows)

# 5. Удаление
cur.execute("CALL delete_contact(%s)", ('Mike',))
conn.commit()

cur.execute("SELECT * FROM contacts")
rows = cur.fetchall()
print("Final contacts:", rows)

cur.close()
conn.close()