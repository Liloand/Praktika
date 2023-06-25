import tkinter as tk
import pymysql.cursors
from tkinter.messagebox import showinfo, showerror
import subprocess

# Создание окна приложения
root = tk.Tk()
root.title('File Compare')
root.geometry('1000x600')
root.resizable(False, False)


def connect_to_database():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="Pa$$w0rd",
        database="db_for_parser"
    )
    return conn


def get_logs():
    # Connect to the database
    conn = connect_to_database()
    if conn:
        showinfo(title="Успешное подключение", message="Подключение к базе данных выполнено успешно!")
    else:
        showerror(title="Неудачное подключение", message="Подключение к базе данных выполнено неуспешно!")

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM log")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    # Create a label for each row of data
    for i in range(len(data)):
        row = data[i]
        show_logs.insert(tk.END, row)
        show_logs.insert(tk.END, "\n")

    # Run the window loop


def clear_logs():
    show_logs.delete('1.0', tk.END)


show_button = tk.Button(root, text="Подключить бд и вывести данные", command=get_logs)

show_button.pack()



label_start_date = tk.Label(root, text="Начальная дата (DD/MM/YYYY): ")
label_start_date.pack()
entry_start_date = tk.Entry(root)
entry_start_date.pack()

label_end_date = tk.Label(root, text="Конечная дата (DD/MM/YYYY): ")
label_end_date.pack()
entry_end_date = tk.Entry(root)
entry_end_date.pack()
show_logs = tk.Text(root)


def filtered_by_ip_address():
    show_logs.delete('1.0', tk.END)
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT ip_address from log")
    data = cursor.fetchall()

    for i in range(len(data)):
        row = data[i]
        show_logs.insert(tk.END, row)
        show_logs.insert(tk.END, "\n")
    cursor.close()
    conn.close()


def filtered_by_date():
    show_logs.delete('1.0', tk.END)
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT date_Log from log")
    data = cursor.fetchall()

    for i in range(len(data)):
        row = data[i]
        show_logs.insert(tk.END, row)
        show_logs.insert(tk.END, "\n")
    cursor.close()
    conn.close()


def get_logs_filtered_by_date_range():
    show_logs.delete('1.0', tk.END)
    start_date = entry_start_date.get()
    end_date = entry_end_date.get()

    try:
        conn = connect_to_database()
        cursor = conn.cursor()
        sql = "SELECT * FROM log WHERE date_Log BETWEEN %s AND %s"
        cursor.execute(sql, (start_date, end_date))
        logs = []
        for row in cursor.fetchall():
            logs.append(row)
        for log in logs:
            show_logs.insert(tk.END, log)
            show_logs.insert(tk.END, "\n")
        cursor.close()
        conn.close()

    except Exception as e:
        show_logs.insert(tk.END, "Error: " + str(e))


ip_filter_button = tk.Button(root, text="Фильтр по IP", command=filtered_by_ip_address)
date_filter_button = tk.Button(root, text="Фильтр по дате", command=filtered_by_date)
date_range_button = tk.Button(root, text="Показать по дню", command=get_logs_filtered_by_date_range)

ip_filter_button.pack(side=tk.LEFT)
date_filter_button.pack(side=tk.LEFT)
date_range_button.pack(side=tk.LEFT)


show_logs.pack()

root.mainloop()