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


def results_show(frame, group):
    text_title = ['Country', 'Games', 'Won', 'Draw', 'Lost', 'Gf', 'Ga', 'Diff', 'Points']
    column = 0
    for i in text_title:
        tk.Label(frame, text=i).grid(row=0, column=column, columnspan=2)
        column += 2

    group_results = fb.group_results(group)[1]
    row = 1
    for result in group_results:
        column = 0
        for attribute in result:
            var = tk.StringVar()
            tk.Label(frame, textvariable=var).grid(row=row, column=column, columnspan=2)
            var.set(attribute)
            column += 2
        row += 1
    tk.Button(frame, text='Back', width=20, height=2, command=lambda:raise_frame(group_stage)).grid(row=6, column=5, rowspan=2, columnspan=6)

img = tk.PhotoImage(file='254645_w.png')

start_page = tk.Frame(root)
second_page = tk.Frame(root)
third_page = tk.Frame(root)
group_stage = tk.Frame(root)
group_A = tk.Frame(root)
group_B = tk.Frame(root)
group_C = tk.Frame(root)
group_D = tk.Frame(root)
group_E = tk.Frame(root)
group_F = tk.Frame(root)
group_G = tk.Frame(root)
group_H = tk.Frame(root)
final_stage_page = tk.Frame(root)
frames = [start_page, second_page, third_page, group_stage, group_A, group_B, group_C,
          group_D, group_E, group_F, group_G, group_H, final_stage_page]


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
tk.Button(third_page, text='Group stage', width=20, height=2, command=lambda:raise_frame(group_stage)).pack()
tk.Button(third_page, text='Final stage', width=20, height=2, command=lambda:raise_frame(final_stage_page)).pack()


# Group stage page
tk.Button(group_stage, text='Group A', width=10, height=2, command=lambda:raise_frame(group_A)).place(x=10, y=25)
tk.Button(group_stage, text='Group B', width=10, height=2, command=lambda:raise_frame(group_B)).place(x=110, y=25)
tk.Button(group_stage, text='Group C', width=10, height=2, command=lambda:raise_frame(group_C)).place(x=210, y=25)
tk.Button(group_stage, text='Group D', width=10, height=2, command=lambda:raise_frame(group_D)).place(x=310, y=25)
tk.Button(group_stage, text='Group E', width=10, height=2, command=lambda:raise_frame(group_E)).place(x=10, y=100)
tk.Button(group_stage, text='Group F', width=10, height=2, command=lambda:raise_frame(group_F)).place(x=110, y=100)
tk.Button(group_stage, text='Group G', width=10, height=2, command=lambda:raise_frame(group_G)).place(x=210, y=100)
tk.Button(group_stage, text='Group H', width=10, height=2, command=lambda:raise_frame(group_H)).place(x=310, y=100)

tk.Button(group_stage, text='Back', width=20, height=2, command=lambda:raise_frame(third_page)).place(x=120, y=175)

# Group A
results_show(group_A, 'A')


# Group B
results_show(group_B, 'B')


# Group C
results_show(group_C, 'C')

# Group D
results_show(group_D, 'D')

# Group E
results_show(group_E, 'E')

# Group F
results_show(group_F, 'F')

# Group G
results_show(group_G, 'G')

# Group H
results_show(group_H, 'H')


# Final stage
raise_frame(start_page)
root.mainloop()
