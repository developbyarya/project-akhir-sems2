import tkinter as tk
from python.tambahLagu import TambahLagu 
from python.cariByJudul import CariByJudulSeq, CariByJudulBin
from python.cariByLirik import CariByLirik
import cpp

root = tk.Tk()

root.geometry("500x300")

canvas = tk.Canvas(root, height=300, width=500)
canvas.place(relx=.5, rely=.5, anchor=tk.CENTER)

buttons = [
            {"title": "Input Lagu", "action": lambda: TambahLagu(root, cpp.tambah_lagu)},
            {"title": "Cari Lagu by Judul (sequential)", 
             "action": lambda : CariByJudulSeq(root, cpp.cari_judul_sequential, cpp.ambil_lirik)},
            {"title": "Cari Lagu by Judul (binary)", 
             "action": lambda : CariByJudulBin(root, cpp.cari_judul_sequential, cpp.ambil_lirik)},
            {"title": "Cari Lagu by Lirik", "action": lambda : CariByLirik(root, cpp.cari_by_lirik, cpp.ambil_lirik)},
            {"title": "Daftar Lagu", "action": lambda : None},
        ]


row = 1
for b in buttons:
    button = tk.Button(canvas, text=b["title"], command=b["action"])
    button.grid(row=row-1, column=0, padx=10, pady=10)
    row += 1


root.mainloop()
