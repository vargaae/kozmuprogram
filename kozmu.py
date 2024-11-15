import tkinter as tk
from tkinter import messagebox, ttk
import csv
from datetime import datetime

# Alap beállítások a Tkinter alkalmazáshoz
root = tk.Tk()
root.title("Közmű Diktálások Kezelése")
root.geometry("1550x550")

# Fájl, ahová a diktálásokat mentjük
FILENAME = "kozmu_diktalasok_dev.csv"

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
    bill_amount = int(bill_amount_entry.get())
    date = str(date_entry.get())
    # date = datetime.now().strftime("%Y-%m-%d")
    save_date = datetime.now().strftime("%Y-%m-%d")

    # Fogyasztás kiszámítása
    consumption = current_reading - previous_reading

    # Új rekord mentése a listába és a fájlba
    # new_record = [utility_type, previous_reading, current_reading, consumption, bill_amount, save_date]
    new_record = [utility_type, previous_reading, current_reading, consumption, bill_amount, date, save_date]
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
    consumption_entry.delete(0, tk.END)
    consumption_entry.insert(0, values[3])
    bill_amount_entry.delete(0, tk.END)
    bill_amount_entry.insert(0, values[4])
    date_entry.delete(0, tk.END) # DIKTÁLÁS DÁTUMA kivétele a recordok közül szerkesztésre
    date_entry.insert(0, values[5]) # DIKTÁLÁS DÁTUMA szerkesztőbe illesztése
    save_date_entry.delete(0, tk.END)
    save_date_entry.insert(0, values[6])

    # A rekord eltávolítása a listából és a táblából
    records.remove(values)
    tree.delete(selected_item)
    
# Rekord kiválasztása törlésre
def delete_record():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Figyelmeztetés", "Nincs kiválasztott rekord!")
        return
    item = tree.item(selected_item)
    values = item["values"]

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

tk.Label(frame, text="Fogyasztás (kWh/m^3):").grid(row=3, column=0)
consumption_entry = tk.Entry(frame)
consumption_entry.grid(row=3, column=1)

tk.Label(frame, text="Számla összeg (Ft):").grid(row=4, column=0)
bill_amount_entry = tk.Entry(frame)
bill_amount_entry.grid(row=4, column=1)

tk.Label(frame, text="Leolvasás dátuma:").grid(row=5, column=0)
date_entry = tk.Entry(frame) # DIKTÁLÁS DÁTUMA 
date_entry.grid(row=5, column=1) # DIKTÁLÁS DÁTUMA 

tk.Label(frame, text="Mentés Dátuma:").grid(row=6, column=0)
save_date_entry = tk.Entry(frame)
save_date_entry.grid(row=6, column=1)

# Gombok
add_button = tk.Button(frame, text="Új Rekord Hozzáadása", command=add_record)
add_button.grid(row=7, column=0, pady=10)

delete_button = tk.Button(frame, text="Kijelölt Rekord Törlése", command=delete_record)
delete_button.grid(row=7, column=1, pady=10)

edit_button = tk.Button(frame, text="Kijelölt Rekord Szerkesztése", command=edit_record)
edit_button.grid(row=8, column=0, pady=10)

save_button = tk.Button(frame, text="Szerkesztett Rekord Változásainak Mentése", command=save_edited_record)
save_button.grid(row=8, column=1, pady=10)

# Táblázat az adatok megjelenítéséhez
# tree = ttk.Treeview(root, columns=("utility_type", "previous_reading", "current_reading", "consumption", "bill_amount", "save_date"), show="headings")
tree = ttk.Treeview(root, columns=("utility_type", "previous_reading", "current_reading", "consumption", "bill_amount", "date", "save_date"), show="headings")
tree.heading("utility_type", text="Közmű típusa")
tree.heading("previous_reading", text="Előző érték")
tree.heading("current_reading", text="Új érték")
tree.heading("consumption", text="Fogyasztás")
tree.heading("bill_amount", text="Számla összeg (Ft)")
tree.heading("date", text="Leolvasás dátuma") # DIKTÁLÁS DÁTUMA
tree.heading("save_date", text="Mentés dátuma")
tree.pack()

# Adatok betöltése fájlból, ha vannak
load_data()

# Alkalmazás futtatása
root.mainloop()
