import tkinter as tk
import example as fb
import os
import random as rm


group_results, match_results, all_final_matches = fb.fifa_2018(fb.groups)


root = tk.Tk()
root.title('FIFA 2018')
w = root.winfo_screenwidth() # ширина экрана
h = root.winfo_screenheight() # высота экрана
w = w//2 # середина экрана
h = h//2
w = w - 200 # смещение от середины
h = h - 150
root.geometry(f'400x300+{w}+{h}')


# Close app button
def close_window():
    root.destroy()


# Raise frame button
def raise_frame(frame):
    frame.tkraise()


# Results frame generator
groups_in = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
def results_show(frame, group):
    row = 0
    for match in match_results[groups_in[group]]:
        tk.Label(frame, text=match).grid(row=row, column=0, columnspan=8)
        row += 1
    text_title = ['Country', 'Games', 'Won', 'Draw', 'Lost', 'Gf', 'Ga', 'Diff', 'Points']
    column = 0
    for i in text_title:
        tk.Label(frame, text=i).grid(row=7, column=column, columnspan=2)
        column += 2
    row = 8
    for result in group_results[groups_in[group]]:
        column = 0
        for attribute in result:
            var = tk.StringVar()
            tk.Label(frame, textvariable=var).grid(row=row, column=column, columnspan=2)
            var.set(attribute)
            column += 2
        row += 1
    tk.Button(frame, text='Back', width=20, height=2, command=lambda:raise_frame(group_stage)).grid(row=12, column=5, rowspan=2, columnspan=6)


# WorldCup img
img = tk.PhotoImage(file='254645_w.png')

#All frames
start_page = tk.Frame(root)
second_page = tk.Frame(root)
default_mode = tk.Frame(root)
user_mode = tk.Frame(root)
your_choice = tk.Frame(root)
random = tk.Frame(root)
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
one_eighth = tk.Frame(root)
quaterfinal = tk.Frame(root)
semifinal = tk.Frame(root)
third_place = tk.Frame(root)
final = tk.Frame(root)

frames = [start_page, second_page, user_mode, your_choice, random, default_mode,
          group_stage, group_A, group_B, group_C, group_D, group_E, group_F,
          group_G, group_H, final_stage_page, one_eighth, quaterfinal,
          semifinal, third_place, final]

# Frame raiser
for frame in frames:
    frame.grid(row=0, column=0, sticky='news')

# Start page
tk.Label(start_page, bg='#27292d', image=img, width=400).pack()
tk.Button(start_page, text='Start', width=20, height=2, command=lambda:raise_frame(second_page)).pack()
tk.Button(start_page, text='Close', width=20, height=2, command=close_window).pack()

# Second page
tk.Label(second_page, bg='#27292d', image=img, width=400).pack()
tk.Button(second_page, text='Default mode', width=20, height=2, command=lambda:raise_frame(default_mode)).pack()
tk.Button(second_page, text='User mode', width=20, height=2, command=lambda:raise_frame(user_mode)).pack()

# User mode
tk.Label(user_mode, bg='#27292d', image=img, width=400).pack()
tk.Button(user_mode, text='Choose yourself', width=20, height=2, command=lambda:raise_frame(your_choice)).pack()
tk.Button(user_mode, text='Random', width=20, height=2, command=lambda:[raise_frame(random)]).pack()
tk.Button(user_mode, text='Back', width=20, height=2, command=lambda:raise_frame(second_page)).pack()

# Your choice
# tk.Label(your_choice, text='Enter 32 teams').grid(row=0, column=4)
# tk.Entry(your_choice).grid(row=1, column=4)
# row = 2
# column =0
# for flag in flags_list[:]:
#     if column == 10:
#         column = 0
#         row += 1
#     text = flag.capitalize()[:-4].replace('_', ' ')
#     tk.Button(your_choice, text=text).grid(row=row, column=column, columnspan=2)
#     column += 2

directory = os.getcwd()+'\\flags'
flags_list = os.listdir(directory)
countries = [i.capitalize()[:-4].replace('_', ' ') if len(i)>7 else i.upper()[:-4] for i in flags_list]
fm_pool = rm.sample(countries, 32)

# Random
random_group ={}
row = 0
column = 0
n = 0
for i in groups_in:
    country_stats = {}
    if i == 'E':
        n = 6
        column = 0
    row = 0 + n
    tk.Label(random, text=f'Group {i}').grid(row=row, column=column, columnspan=2)
    row += 1
    for _ in range(4):
        country = fm_pool.pop(0)
        tk.Label(random, text=country).grid(row=row, column=column, columnspan=2)
        country_stats[country] = {'games': 0, 'won': 0, 'draw': 0, 'lost': 0, 'gf': 0, 'ga': 0, 'diff': 0, 'points': 0}
        row += 1
    column += 2
    random_group[i] = country_stats
tk.Button(random, text='Next', height=2, command=lambda:raise_frame(default_mode)).grid(row=row+1, column=4)
tk.Button(random, text='Back', height=2, command=lambda:raise_frame(user_mode)).grid(row=row+1, column=3)

# Third page
tk.Label(default_mode, bg='#27292d', image=img, width=400).pack()
tk.Button(default_mode, text='Group stage', width=20, height=2, command=lambda:raise_frame(group_stage)).pack()
tk.Button(default_mode, text='Final stage', width=20, height=2, command=lambda:raise_frame(final_stage_page)).pack()

# Group stage page
tk.Button(group_stage, text='Group A', width=10, height=2, command=lambda:raise_frame(group_A)).place(x=10, y=25)
tk.Button(group_stage, text='Group B', width=10, height=2, command=lambda:raise_frame(group_B)).place(x=110, y=25)
tk.Button(group_stage, text='Group C', width=10, height=2, command=lambda:raise_frame(group_C)).place(x=210, y=25)
tk.Button(group_stage, text='Group D', width=10, height=2, command=lambda:raise_frame(group_D)).place(x=310, y=25)
tk.Button(group_stage, text='Group E', width=10, height=2, command=lambda:raise_frame(group_E)).place(x=10, y=100)
tk.Button(group_stage, text='Group F', width=10, height=2, command=lambda:raise_frame(group_F)).place(x=110, y=100)
tk.Button(group_stage, text='Group G', width=10, height=2, command=lambda:raise_frame(group_G)).place(x=210, y=100)
tk.Button(group_stage, text='Group H', width=10, height=2, command=lambda:raise_frame(group_H)).place(x=310, y=100)
tk.Button(group_stage, text='Back', width=20, height=2, command=lambda:raise_frame(default_mode)).place(x=120, y=175)

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
tk.Button(final_stage_page, text='1/8', width=10, height=2, command=lambda:raise_frame(one_eighth)).place(x=10, y=25)
tk.Button(final_stage_page, text='1/4', width=10, height=2, command=lambda:raise_frame(quaterfinal)).place(x=110, y=25)
tk.Button(final_stage_page, text='1/2', width=10, height=2, command=lambda:raise_frame(semifinal)).place(x=210, y=25)
tk.Button(final_stage_page, text='3d place', width=10, height=2, command=lambda:raise_frame(third_place)).place(x=310, y=25)
tk.Button(final_stage_page, text='Final', width=53, height=2, command=lambda:raise_frame(final)).place(x=10, y=100)
tk.Button(final_stage_page, text='Back', width=20, height=2, command=lambda:raise_frame(default_mode)).place(x=120, y=175)

# 1/8
for match in all_final_matches[:8]:
    tk.Label(one_eighth, text=match).pack()
tk.Button(one_eighth, text='Back', width=20, height=2, command=lambda:raise_frame(final_stage_page)).pack()

# 1/4
for match in all_final_matches[8:12]:
    tk.Label(quaterfinal, text=match).pack()
tk.Button(quaterfinal, text='Back', width=20, height=2, command=lambda:raise_frame(final_stage_page)).pack()

# 1/2
for match in all_final_matches[12:14]:
    tk.Label(semifinal, text=match).pack()
tk.Button(semifinal, text='Back', width=20, height=2, command=lambda:raise_frame(final_stage_page)).pack()

# 3d place
tk.Label(third_place, text=all_final_matches[-2]).pack()
tk.Button(third_place, text='Back', width=20, height=2, command=lambda:raise_frame(final_stage_page)).pack()

# Final
tk.Label(final, text=all_final_matches[-1]).pack()
tk.Button(final, text='Back', width=20, height=2, command=lambda:raise_frame(final_stage_page)).pack()

raise_frame(start_page)
root.mainloop()
