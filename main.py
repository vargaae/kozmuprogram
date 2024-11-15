import tkinter as tk
from tkinter import messagebox, ttk
import csv
from datetime import datetime

# Alap beállítások a Tkinter alkalmazáshoz
root = tk.Tk()
root.title("Közmű Diktálások Kezelése")
root.geometry("800x600")

# Fájl, ahová a diktálásokat mentjük
FILENAME = "kozmu_diktalasok.csv"

# Adatlista, ahová a betöltött adatokat mentjük
records = []

# Adatok betöltése fájlból
def load_data():
    global records
    try:
        with open(FILENAME, newline='') as csvfile:
            reader = csv.reader(csvfile)
            records = [row for row in reader]
            for row in records:
                tree.insert("", tk.END, values=row)
    except FileNotFoundError:
        pass

# Adatok mentése fájlba
def save_data():
    with open(FILENAME, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(records)
    messagebox.showinfo("Mentés", "Az adatok sikeresen elmentve!")

# Új diktálás hozzáadása
def add_record():
    utility_type = utility_type_var.get()
    previous_reading = int(previous_reading_entry.get())
    current_reading = int(current_reading_entry.get())
    bill_amount = (bill_amount_entry.get())
    # TODO:  date = datetime.now().strftime("%Y-%m-%d")
    save_date = datetime.now().strftime("%Y-%m-%d")

    # Fogyasztás kiszámítása
    consumption = current_reading - previous_reading

    # Új rekord mentése a listába és a fájlba
    new_record = [utility_type, previous_reading, current_reading, consumption, bill_amount, save_date]
    # TODO: new_record = [utility_type, save_date, previous_reading, current_reading, consumption, bill_amount, date]
    records.append(new_record)
    tree.insert("", tk.END, values=new_record)
    save_data()

# Rekord kiválasztása szerkesztésre
def edit_record():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Figyelmeztetés", "Nincs kiválasztott rekord!")
        return
    item = tree.item(selected_item)
    values = item["values"]

    # Kitöltjük a mezőket a kiválasztott rekord adataival
    utility_type_var.set(values[0])
    previous_reading_entry.delete(0, tk.END)
    previous_reading_entry.insert(0, values[1])
    current_reading_entry.delete(0, tk.END)
    current_reading_entry.insert(0, values[2])
    bill_amount_entry.delete(0, tk.END)
    bill_amount_entry.insert(0, values[3])
    # TODO:  bill_amount_entry.insert(0, values[4])

    # A rekord eltávolítása a listából és a táblából
    records.remove(values)
    tree.delete(selected_item)

# A frissített rekord mentése
def save_edited_record():
    add_record()

# GUI elemek
frame = tk.Frame(root)
frame.pack(pady=20)

# Mezők a rekordokhoz
tk.Label(frame, text="Közmű típusa:").grid(row=0, column=0)
utility_type_var = tk.StringVar()
utility_type_combo = ttk.Combobox(frame, textvariable=utility_type_var)
utility_type_combo['values'] = ("Gáz", "Áram", "Víz")
utility_type_combo.grid(row=0, column=1)

tk.Label(frame, text="Előző érték:").grid(row=1, column=0)
previous_reading_entry = tk.Entry(frame)
previous_reading_entry.grid(row=1, column=1)

tk.Label(frame, text="Új érték:").grid(row=2, column=0)
current_reading_entry = tk.Entry(frame)
current_reading_entry.grid(row=2, column=1)

tk.Label(frame, text="Számla összeg (Ft):").grid(row=3, column=0)
bill_amount_entry = tk.Entry(frame)
bill_amount_entry.grid(row=3, column=1)

# Gombok
add_button = tk.Button(frame, text="Hozzáadás", command=add_record)
add_button.grid(row=4, column=0, pady=10)

edit_button = tk.Button(frame, text="Szerkesztés", command=edit_record)
edit_button.grid(row=4, column=1, pady=10)

save_button = tk.Button(frame, text="Változások mentése", command=save_edited_record)
save_button.grid(row=4, column=2, pady=10)

# Táblázat az adatok megjelenítéséhez
tree = ttk.Treeview(root, columns=("utility_type", "previous_reading", "current_reading", "consumption", "bill_amount", "save_date"), show="headings")
# TODO: tree = ttk.Treeview(root, columns=("utility_type", "previous_reading", "current_reading", "consumption", "bill_amount", "date", "save_date"), show="headings")
tree.heading("utility_type", text="Közmű típusa")
tree.heading("previous_reading", text="Előző érték")
tree.heading("current_reading", text="Új érték")
tree.heading("consumption", text="Fogyasztás")
tree.heading("bill_amount", text="Számla összeg (Ft)")
# tree.heading("date", text="Diktálás dátuma")
tree.heading("save_date", text="Mentés dátuma")
tree.pack()

# Adatok betöltése fájlból, ha vannak
load_data()

# Alkalmazás futtatása
root.mainloop()
