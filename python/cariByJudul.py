import tkinter as tk

class CariByJudulSeq:
    def __init__(self, root, *handler):
        self.window = tk.Toplevel(root)
        self.window.title("Cari Lagu by Judul")
        self.widget()
        self.handler = handler[0]
        self.ambil_lirik = handler[1]
        
    def widget(self):
        title = tk.Label(self.window, text="Cari Judul Lagu", anchor='center')
        title.pack()

        self.in_judul = tk.Entry(self.window)
        self.in_judul.pack()

        penyanyi_label = tk.Label(self.window, text="Penyanyi", anchor="center")
        penyanyi_label.pack()
        
        self.in_penyanyi = tk.Entry(self.window)
        self.in_penyanyi.pack()

        save_button = tk.Button(self.window, text="Cari", command=self.cari)
        save_button.pack()
    def cari(self):
        judul = self.in_judul.get()
        penyanyi = self.in_penyanyi.get()

        # cari Lagu
        hasil = self.handler(judul, penyanyi)
        if (hasil == ""):
            hasil_label = tk.Label(self.window, text="Tidak ditemukan", anchor='center', pady=15)
            hasil_label.pack()
            return

        hasil_label = tk.Label(self.window, text=hasil, anchor='center', pady=15)
        hasil_label.pack()

        lirik = self.ambil_lirik(f"{hasil}.txt")
        lirik_text = tk.Text(self.window, width=20, height=15)
        lirik_text.insert("1.0", lirik)
        lirik_text.config(state="disabled")
        lirik_text.pack()

        close_btn = tk.Button(self.window, text="close", command=self.window.destroy, anchor='center')
        close_btn.pack()




class CariByJudulBin:
    def __init__(self, root, *handler):
        self.window = tk.Toplevel(root)
        self.window.title("Cari Lagu by Judul")
        self.widget()
        self.handler = handler[0]
        self.ambil_lirik = handler[1]
        
    def widget(self):
        title = tk.Label(self.window, text="Cari Judul Lagu", anchor='center')
        title.pack()

        self.in_judul = tk.Entry(self.window)
        self.in_judul.pack()

        penyanyi_label = tk.Label(self.window, text="Penyanyi", anchor="center")
        penyanyi_label.pack()
        
        self.in_penyanyi = tk.Entry(self.window)
        self.in_penyanyi.pack()

        save_button = tk.Button(self.window, text="Cari", command=self.cari)
        save_button.pack()
    def cari(self):
        judul = self.in_judul.get()
        penyanyi = self.in_penyanyi.get()

        # cari Lagu
        hasil = self.handler(judul, penyanyi)
        if (hasil == ""):
            hasil_label = tk.Label(self.window, text="Tidak ditemukan", anchor='center', pady=15)
            hasil_label.pack()
            return

        hasil_label = tk.Label(self.window, text=hasil, anchor='center', pady=15)
        hasil_label.pack()

        lirik = self.ambil_lirik(f"{hasil}.txt")
        lirik_text = tk.Text(self.window, width=20, height=15)
        lirik_text.insert("1.0", lirik)
        lirik_text.config(state="disabled")
        lirik_text.pack()

        close_btn = tk.Button(self.window, text="close", command=self.window.destroy, anchor='center')
        close_btn.pack()
