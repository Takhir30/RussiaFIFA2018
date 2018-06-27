import tkinter as tk
import example as fb


root = tk.Tk()

root.title('FIFA 2018')

w = root.winfo_screenwidth() # ширина экрана
h = root.winfo_screenheight() # высота экрана
w = w//2 # середина экрана
h = h//2
w = w - 200 # смещение от середины
h = h - 150
root.geometry(f'400x300+{w}+{h}')


def close_window():
    root.destroy()


def raise_frame(frame):
    frame.tkraise()


def results_show(group):
    text_title = ['Country', 'Games', 'Won', 'Draw', 'Lost', 'Gf', 'Ga', 'Diff', 'Points']
    column = 0
    for i in text_title:
        tk.Label(group_stage_page, text=i).grid(row=0, column=column)
        column += 1

    group_results = fb.group_results(group)[1]
    row = 1
    for result in group_results:
        column = 0
        for attribute in result:
            var = tk.StringVar()
            tk.Label(group_stage_page, textvariable=var).grid(row=row, column=column)
            var.set(attribute)
            column += 1
        row += 1
        

img = tk.PhotoImage(file='254645_w.png')

start_page = tk.Frame(root)
second_page = tk.Frame(root)
third_page = tk.Frame(root)
group_stage_page = tk.Frame(root)
final_stage_page = tk.Frame(root)
frames = [start_page, second_page, third_page, group_stage_page, final_stage_page]


for frame in frames:
    frame.grid(row=0, column=0, sticky='news')

# Start page
tk.Label(start_page, bg='#27292d', image=img, width=400).pack()
tk.Button(start_page, text='Start', width=20, height=2, command=lambda:raise_frame(second_page)).pack()
tk.Button(start_page, text='Close', width=20, height=2, command=close_window).pack()

# Second page
tk.Label(second_page, bg='#27292d', image=img, width=400).pack()
tk.Button(second_page, text='Default mode', width=20, height=2, command=lambda:raise_frame(third_page)).pack()
tk.Button(second_page, text='User mode', width=20, height=2).pack()

# Third page
tk.Label(third_page, bg='#27292d', image=img, width=400).pack()
tk.Button(third_page, text='Group stage', width=20, height=2, command=lambda:[raise_frame(group_stage_page), results_show('A')]).pack()
tk.Button(third_page, text='Final stage', width=20, height=2, command=lambda:raise_frame(final_stage_page)).pack()

# Group stage page


tk.Button(group_stage_page, text='<', width=2, height=2).place(x=95, y=145)
tk.Label(group_stage_page, text='Group A', width=20, height=2).place(x=120, y=145)
tk.Button(group_stage_page, text='>', width=2, height=2).place(x=270, y=145)

# Final stage


raise_frame(start_page)
root.mainloop()
