import tkinter as tk
from tkinter import ttk

#СОЗДАЕМ РОДИТЕЛЬСКОЕ ОКНО
root = tk.Tk()
root.title("CHESS")
root.geometry('1000x600')
tabControl = ttk.Notebook(root)

#СОЗДАЕМ ВКЛАДКИ ДЛЯ ПЕРЕКЛЮЧЕНИЯ
test_a = ttk.Frame(tabControl)
test_b = ttk.Frame(tabControl)
test_c = ttk.Frame(tabControl)

tabControl.add(test_a, text='TEST A')
tabControl.add(test_b, text='TEST B')
tabControl.add(test_c, text='TEST C')
tabControl.pack(expand=0, fill="both")


#СОЗДАЕМ КЛИКАБЕЛЬНЫЕ КЛЕТОЧКИ
for xA in range(8):
    for yA in range(8):
        if (xA + yA) % 2 == 1:
            btn = tk.Button(test_a ,text='', width= 10, height= 4, bg='black',  )
            btn.grid(row=xA, column=yA)
        else:
            btn = tk.Button(test_a ,text='', width= 10, height= 4, bg='white',  )
            btn.grid(row=xA, column=yA)

for xB in range(8):
    for yB in range(8):
        if (xB + yB) % 2 == 1:
            btn = tk.Button(test_b ,text='', width= 10, height= 4, bg='black',  )
            btn.grid(row=xB, column=yB)
        else:
            btn = tk.Button(test_b ,text="", width= 10, height= 4, bg='white',    )
            btn.grid(row=xB, column=yB)

for xC in range(8):
    for yC in range(8):
        if (xC + yC) % 2 == 1:
            btn = tk.Button(test_c ,text='', width= 10, height= 4, bg='black',  )
            btn.grid(row=xC, column=yC)
        else:
            btn = tk.Button(test_c ,text="", width= 10, height= 4, bg='white',   )
            btn.grid(row=xC, column=yC)





root.mainloop()