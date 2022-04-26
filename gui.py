from tkinter import *
from tkinter import ttk
import tkinter
from dao.vaccination_by_province_dao import *

dose_dao = DaoFactory('dose')
dose_method = dose_dao.create_dao()


def dose_search():
    result = dose_method.get_query_by_province(dose_search_var.get())
    dose_search_result.set(result)


def dose_update():
    data = {
        "province": dose_update_province.get(),
        "over_60_1st_dose": dose_update_over_60_1st_dose.get(),
        "total_1st_dose": dose_update_total_1st_dose.get(),
        "total_2nd_dose": dose_update_total_2nd_dose.get(),
        "total_3rd_dose": dose_update_total_3rd_dose.get()
    }
    result = dose_method.update_by_province(data)
    dose_update_result.set(result)
    get_dose_data()


def get_dose_data():
    dose_data_table = dose_method.get_query()
    for i in dose_tree.get_children():
        dose_tree.delete(i)

    for i in dose_data_table:
        dose_tree.insert("", "end", values=i)


def dose_select(a):
    item = dose_tree.focus()
    value = dose_tree.item(item)["values"]
    dose_update_province.set(value[1])
    dose_update_over_60_1st_dose.set(value[2])
    dose_update_total_1st_dose.set(value[3])
    dose_update_total_2nd_dose.set(value[4])
    dose_update_total_3rd_dose.set(value[5])


root = Tk()
root.title("Thailand vaccination by province")

main_frame = Frame(root)
main_frame.grid(row=0, column=0)

canvas = Canvas(main_frame)
canvas.grid(row=0, column=0)

scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
scrollbar.grid(row=0, column=0, sticky=NS+E)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(
    scrollregion=canvas.bbox("all"), width=1450, height=800))

frame = Frame(canvas)

canvas.create_window((0, 0), window=frame, anchor="nw")

style = ttk.Style()
style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=(
    'Calibri', 12), rowheight=30)  # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=(
    'Calibri', 16, 'bold'))  # Modify the font of the headings
style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {
             'sticky': 'nswe'})])  # Remove the borders

dose_cols = ['id', 'Province', 'Age over 60 1st dose',
             'Total 1st dose', 'Total 2nd dose', 'Total 3rd dose', 'Last updated']
dose_tree = ttk.Treeview(frame, columns=dose_cols, style="mystyle.Treeview")

dose_tree['show'] = 'headings'
for i in dose_cols:
    dose_tree.column(column=f'{i}', width=160, minwidth=100, stretch=False)
    dose_tree.heading(column=f'{i}', text=f'{i}', anchor=CENTER)
get_dose_data()

dose_search_var = tkinter.StringVar()
dose_search_result = tkinter.StringVar()

dose_update_province = tkinter.StringVar()
dose_update_over_60_1st_dose = tkinter.IntVar()
dose_update_total_1st_dose = tkinter.IntVar()
dose_update_total_2nd_dose = tkinter.IntVar()
dose_update_total_3rd_dose = tkinter.IntVar()
dose_update_result = tkinter.StringVar()

dose_tree.bind('<ButtonRelease-1>', dose_select)

Label(frame, text="Vaccination by dose", font=('Calibri', 20, 'bold')).grid(
    row=0, column=0, columnspan=6, pady=20)
dose_tree.grid(row=1, column=0, columnspan=6)
Label(frame, text="province", font=20).grid(
    row=2, column=0, columnspan=6, padx=10, pady=10)
tkinter.Entry(frame, textvariable=dose_search_var, font=(
    'calibre', 10, 'normal')).grid(row=3, column=0, columnspan=6)
Button(frame, text="Search", command=dose_search).grid(
    row=4, column=0, columnspan=6, pady=10)
Label(frame, textvariable=dose_search_result, font=('Calibri', 14, 'bold')).grid(
    row=5, column=0, columnspan=6, pady=5)

Label(frame, text="province", font=20).grid(
    row=6, column=2, sticky=tkinter.E, padx=10, pady=10)
tkinter.Entry(frame, textvariable=dose_update_province, font=(
    'calibre', 10, 'normal')).grid(row=6, column=3, sticky=tkinter.W)

Label(frame, text="new age over 60 1st dose", font=20).grid(
    row=7, column=0, sticky=tkinter.E, padx=10, pady=10)
tkinter.Entry(frame, textvariable=dose_update_over_60_1st_dose, font=(
    'calibre', 10, 'normal')).grid(row=7, column=1, sticky=tkinter.W)

Label(frame, text="new total 1st dose", font=20).grid(
    row=8, column=0, sticky=tkinter.E, padx=10, pady=10)
tkinter.Entry(frame, textvariable=dose_update_total_1st_dose, font=(
    'calibre', 10, 'normal')).grid(row=8, column=1, sticky=tkinter.W)

Label(frame, text="new total 2nd dose", font=20).grid(
    row=7, column=4, sticky=tkinter.E, padx=10, pady=10)
tkinter.Entry(frame, textvariable=dose_update_total_2nd_dose, font=(
    'calibre', 10, 'normal')).grid(row=7, column=5, sticky=tkinter.W)

Label(frame, text="new total 3rd dose", font=20).grid(
    row=8, column=4, sticky=tkinter.E, padx=10, pady=10)
tkinter.Entry(frame, textvariable=dose_update_total_3rd_dose, font=(
    'calibre', 10, 'normal')).grid(row=8, column=5, sticky=tkinter.W)

Button(frame, text="Update", command=dose_update).grid(
    row=9, column=0, columnspan=8)
Label(frame, textvariable=dose_update_result, font=('Calibri', 14, 'bold')).grid(
    row=10, column=0, columnspan=6, pady=5)

auth_dao = DaoFactory('auth')
auth_method = auth_dao.create_dao()


def auth_search():
    result = auth_method.get_query_by_province(auth_search_var.get())
    auth_search_result.set(result)


def auth_update():
    data = {
        "province": auth_update_province.get(),
        "total_doses": auth_update_total_doses.get(),
        "AstraZeneca": auth_update_AstraZeneca.get(),
        "Sinovac": auth_update_Sinovac.get(),
        "Sinopharm": auth_update_Sinopharm.get(),
        "Pfizer": auth_update_Pfizer.get(),
        "Johnson_Johnson": auth_update_Johnson_Johnson.get()
    }
    result = auth_method.update_by_province(data)
    auth_update_result.set(result)
    get_auth_data()


def get_auth_data():
    auth_data_table = auth_method.get_query()
    for i in auth_tree.get_children():
        auth_tree.delete(i)

    for i in auth_data_table:
        auth_tree.insert("", "end", values=i)


def auth_select(a):
    item = auth_tree.focus()
    value = auth_tree.item(item)["values"]
    auth_update_province.set(value[1])
    auth_update_total_doses.set(value[2])
    auth_update_AstraZeneca.set(value[3])
    auth_update_Sinovac.set(value[4])
    auth_update_Sinopharm.set(value[5])
    auth_update_Pfizer.set(value[6])
    auth_update_Johnson_Johnson.set(value[7])


auth_cols = ['id', 'Province', 'Total doses', 'AstraZeneca',
             'Sinovac', 'Sinopharm', 'Pfizer', 'Johnson&Johnson', 'Last updated']
auth_tree = ttk.Treeview(frame, columns=auth_cols, style="mystyle.Treeview")

auth_tree['show'] = 'headings'
for i in auth_cols:
    auth_tree.column(column=f'{i}', width=160, minwidth=100, stretch=False)
    auth_tree.heading(column=f'{i}', text=f'{i}', anchor=CENTER)
get_auth_data()


auth_search_var = tkinter.StringVar()
auth_search_result = tkinter.StringVar()

auth_update_province = tkinter.StringVar()
auth_update_total_doses = tkinter.IntVar()
auth_update_AstraZeneca = tkinter.IntVar()
auth_update_Sinovac = tkinter.IntVar()
auth_update_Sinopharm = tkinter.IntVar()
auth_update_Pfizer = tkinter.IntVar()
auth_update_Johnson_Johnson = tkinter.IntVar()
auth_update_result = tkinter.StringVar()

auth_tree.bind('<ButtonRelease-1>', auth_select)

Label(frame, text="Vaccination by authorizations", font=(
    'Calibri', 20, 'bold')).grid(row=11, column=0, columnspan=6, pady=20)
auth_tree.grid(row=12, column=0, columnspan=6)
Label(frame, text="province", font=20).grid(
    row=13, column=0, columnspan=6, padx=10, pady=10)
tkinter.Entry(frame, textvariable=auth_search_var, font=(
    'calibre', 10, 'normal')).grid(row=14, column=0, columnspan=6)
Button(frame, text="Search", command=auth_search).grid(
    row=15, column=0, columnspan=6, pady=10)
Label(frame, textvariable=auth_search_result, font=('Calibri', 14, 'bold')).grid(
    row=16, column=0, columnspan=6, pady=5)

Label(frame, text="province", font=20).grid(
    row=17, column=2, sticky=tkinter.E, padx=10, pady=10)
tkinter.Entry(frame, textvariable=auth_update_province, font=(
    'calibre', 10, 'normal')).grid(row=17, column=3, sticky=tkinter.W)

Label(frame, text="new total dose vaccination", font=20).grid(
    row=18, column=0, sticky=tkinter.E, padx=10, pady=10)
tkinter.Entry(frame, textvariable=auth_update_total_doses, font=(
    'calibre', 10, 'normal')).grid(row=18, column=1, sticky=tkinter.W)

Label(frame, text="new AstraZeneca vaccination", font=20).grid(
    row=19, column=0, sticky=tkinter.E, padx=10, pady=10)
tkinter.Entry(frame, textvariable=auth_update_AstraZeneca, font=(
    'calibre', 10, 'normal')).grid(row=19, column=1, sticky=tkinter.W)

Label(frame, text="new Sinovac vaccination", font=20).grid(
    row=18, column=2, sticky=tkinter.E, padx=10, pady=10)
tkinter.Entry(frame, textvariable=auth_update_Sinovac, font=(
    'calibre', 10, 'normal')).grid(row=18, column=3, sticky=tkinter.W)

Label(frame, text="new Sinopharm vaccination", font=20).grid(
    row=19, column=2, sticky=tkinter.E, padx=10, pady=10)
tkinter.Entry(frame, textvariable=auth_update_Sinopharm, font=(
    'calibre', 10, 'normal')).grid(row=19, column=3, sticky=tkinter.W)

Label(frame, text="new Pfizer vaccination", font=20).grid(
    row=18, column=4, sticky=tkinter.E, padx=10, pady=10)
tkinter.Entry(frame, textvariable=auth_update_Pfizer, font=(
    'calibre', 10, 'normal')).grid(row=18, column=5, sticky=tkinter.W)

Label(frame, text="new Johnson&Johnson vaccination", font=20).grid(
    row=19, column=4, sticky=tkinter.E, padx=10, pady=10)
tkinter.Entry(frame, textvariable=auth_update_Johnson_Johnson, font=(
    'calibre', 10, 'normal')).grid(row=19, column=5, sticky=tkinter.W)

Button(frame, text="Update", command=auth_update).grid(
    row=20, column=0, columnspan=8)
Label(frame, textvariable=auth_update_result, font=('Calibri', 14, 'bold')).grid(
    row=21, column=0, columnspan=6, pady=5)
# root.geometry("1500x1000")


root.mainloop()
