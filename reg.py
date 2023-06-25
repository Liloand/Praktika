import tkinter as tk

def register_user():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    email = entry_email.get()
    password = entry_password.get()


    print("Спасибо за регистрацию, " + first_name + " " + last_name)

root = tk.Tk()

# Создаем виджеты для ввода данных
label_first_name = tk.Label(root, text="Введите ваше имя:")
entry_first_name = tk.Entry(root)

label_last_name = tk.Label(root, text="Введите вашу фамилию:")
entry_last_name = tk.Entry(root)

label_email = tk.Label(root, text="Введите ваш адрес электронной почты:")
entry_email = tk.Entry(root)

label_password = tk.Label(root, text="Введите ваш пароль:")
entry_password = tk.Entry(root, show="*")

# Создаем кнопку для отправки данных
register_button = tk.Button(root, text="Зарегистрироваться", command=register_user)

# Размещаем виджеты на форме с помощью сетки
label_first_name.grid(row=0, column=0)
entry_first_name.grid(row=0, column=1)

label_last_name.grid(row=1, column=0)
entry_last_name.grid(row=1, column=1)

label_email.grid(row=2, column=0)
entry_email.grid(row=2, column=1)

label_password.grid(row=3, column=0)
entry_password.grid(row=3, column=1)

register_button.grid(row=4, column=1)

root.mainloop()