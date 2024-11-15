 <div align="center">
  <img alt="Application image" src="https://cssh.northeastern.edu/informationethics/wp-content/uploads/sites/44/2020/07/ai@2x.png" width="400" />
</div>
<br>
  <div align="center">
    <img src="https://img.shields.io/badge/-Python-black?style=for-the-badge&logoColor=white&logo=python&color=61DAFB" alt="Python" />
</div>

# Közmű APPLICATION v2 - Magyar nyelvű

Egy Python-alapú, grafikus felületet biztosító program a közműdiktálások kezelésére. A program tkinter könyvtárat használ a vizuális megjelenítéshez, és minden diktálási adatot egy CSV fájlban tárol.

## 🚀AZ ÖTLET - PROMPT

Készíts egy jól működő programot vizuális megjelenítéssel python nyelven CSV fájlba történő mentéssel, ami összesíti a közművek diktálási értékeit m3-ben, kWh-ban, számlák összegeit, két legutolsó diktálási érték közötti különbséget vagyis a fogyasztást, diktálás dátumait, ezekből keletkező számlák összegét forintban és be lehet írni az újabb diktálásokat és számlák összegét. Legyen benne Gáz, Áram, Víz diktálása...

## A Program Funkciói

- 🚀Közműtípusok: Gáz, Áram, Víz.
- 🚀Diktálási Adatok Bevitele: Előző és új diktálási értékek (m³ vagy kWh), számlaösszeg (Ft), és dátum.
- 🚀Diktálási Adatok Megjelenítése és szerkesztése: Előző és új diktálási értékek (m³ vagy kWh), számlaösszeg (Ft), és mentés dátuma.
- 🚀Fogyasztás Számítása: Két egymást követő diktálási érték különbsége.
- 🚀Fájlba Mentés: Az adatokat egy .csv fájlba mentjük.

## A Program Magyarázat

- 1. Kezdő Ablak és Felület: Az ablakban címkék és beviteli mezők jelennek meg, ahol a közmű típusát, előző és új diktálási értéket, valamint a számla összegét lehet megadni.

- 2. Fájlba Mentés: A save_data függvény a megadott adatokat egy fájlba menti. A fájl neve ozmu_diktalasok.csv, és minden új adatot egy új sorba ír.

- 3. Hibakezelés: Ha a felhasználó hibás adatot ad meg (pl. szöveget egy szám mezőben), a program figyelmeztetést jelenít meg.

- 4. Beviteli mezők törlése: Sikeres mentés után a beviteli mezők kiürülnek, hogy új adatokat lehessen megadni.


## Feladatok fejlesztéshez - TODO

- 🚀Add Dictation: Adds a new utility dictation entry with the date of the last save and the date of the dictation(leolvasás dátuma)
- 🚀Edit Dictation: Edits an existing dictation entry and updates the CSV file.
- 🚀Delete Dictation: Deletes an entry from the CSV file.

## Issues - TODO

- The program would calculate consumption as the difference between the current dictation and the earlier date's dictation value.

## Libraries Used

- 🚀pandas: For data manipulation and saving/loading CSV files.
- 🚀tkinter: For the graphical user interface.
- 🚀tkcalendar: For the date picker widget.

## Data Handling

- 🚀File Handling: The data is saved in a CSV file (utility_data.csv). The program initializes the CSV file if it does not exist and saves data after every operation.
- 🚀Default Values: The default rate is set to 100 HUF per m3 or kWh, but this can be modified by the user when adding or editing a dictation.

- 🚀Consumption Calculation: The program calculates consumption as the difference between the current and previous dictation values. Consumption and bill amounts are recalculated whenever a dictation is added or modified.

- 🚀Display Data: Shows the data in a table format using ttk.Treeview.

**Projekt futtatása**

```bash
python main.py

```

**Fejlesztés másolat - utolsó mentés timestamp-je külön kerüljön a leolvasás napjától**

```bash
python kozmu.py

```

**Saved data**
A kozmu_diktalasok.csv fájlba mentett adatok például így fognak kinézni:

```bash
�ram,13463,13643,180,9680,2024-11-09
G�z,13463,13643,180,9680,2024-11-09
```