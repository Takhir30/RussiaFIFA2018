import tkinter as tk

root = tk.Tk()

def close_window():
    root.destroy()

def raise_frame(frame):
    frame.tkraise()

img = tk.PhotoImage(file='254645_w.png')

start_page = tk.Frame(root)
second_page = tk.Frame(root)
third_page = tk.Frame(root)

for frame in (start_page, second_page, third_page):
    frame.grid(row=0, column=0, sticky='news')

tk.Label(start_page, bg='#27292d', image=img).pack()
tk.Button(start_page, text='Start', width=20, height=2, command=lambda:raise_frame(second_page)).pack()
tk.Button(start_page, text='Close', width=20, height=2, command=close_window).pack()


tk.Label(second_page, bg='#27292d', image=img).pack()
tk.Button(second_page, text='Default mode', width=20, height=2, command=lambda:raise_frame(third_page)).pack()
tk.Button(second_page, text='User mode', width=20, height=2).pack()


tk.Label(third_page, bg='#27292d', image=img).pack()
tk.Button(third_page, text='Group stage', width=20, height=2).pack()
tk.Button(third_page, text='Final stage', width=20, height=2).pack()


raise_frame(start_page)
root.mainloop()
