 <div align="center">
  <img alt="Application image" src="https://cssh.northeastern.edu/informationethics/wp-content/uploads/sites/44/2020/07/ai@2x.png" width="400" />
</div>
<br>
  <div align="center">
    <img src="https://img.shields.io/badge/-Python-black?style=for-the-badge&logoColor=white&logo=python&color=61DAFB" alt="Python" />

# Közmű APPLICATION

## 🚀Leírás

Egy Python-alapú, grafikus felületet biztosító program a közműdiktálások kezelésére. A program PyQt5 könyvtárat használ a vizuális megjelenítéshez, és minden diktálási adatot egy TXT fájlban tárol.

## 🚀AZ ÖTLET - PROMPT

Készíts egy jól működő programot vizuális megjelenítéssel python nyelven fájlba történő mentéssel, ami összesíti a közművek diktálási értékeit m3-ben, kWh-ban, összegeit, két legutolsó diktálási érték közötti különbséget vagyis a fogyasztást, diktálás dátumait, ezekből keletkező számlák összegét forintban és be lehet írni az újabb diktálásokat és számlák összegét. Legyen benne Gáz, Áram, Víz diktálása.

## 🚀A Program Funkciói

Közműtípusok: Gáz, Áram, Víz.
Diktálási Adatok Bevitele: Előző és új diktálási értékek (m³ vagy kWh), számlaösszeg (Ft), és dátum.
Fogyasztás Számítása: Két egymást követő diktálási érték különbsége.
Fájlba Mentés: Az adatokat egy .txt fájlba mentjük.


**Program magyarázat**
Kezdő Ablak és Felület: Az ablakban címkék és beviteli mezők jelennek meg, ahol a közmű típusát, előző és új diktálási értéket, valamint a számla összegét lehet megadni.
Fájlba Mentés: A save_data függvény a megadott adatokat egy fájlba menti. A fájl neve kozmu_adatok.txt, és minden új adatot egy új sorba ír.
Hibakezelés: Ha a felhasználó hibás adatot ad meg (pl. szöveget egy szám mezőben), a program figyelmeztetést jelenít meg.
Beviteli mezők törlése: Sikeres mentés után a beviteli mezők kiürülnek, hogy új adatokat lehessen megadni.

**Running the Project**

```bash
pip install pyqt5

python kozmu.py

```
