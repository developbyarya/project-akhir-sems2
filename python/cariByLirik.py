import tkinter as tk

class CariByLirik:
    def __init__(self, root, pencarian, *handler):
        self.window = tk.Toplevel(root)
        self.window.title("Cari lagu dari Lirik")
        self.widget()
        self.pencarian = pencarian
        self.ambil_lirik = handler[0]
    def widget(self):
        title_label = tk.Label(self.window, text="Cari dari Lirik", anchor="center")
        title_label.pack()

        self.input_lirik = tk.Entry(self.window)
        self.input_lirik.pack()

        cari_button = tk.Button(self.window, text="Cari", anchor="center", command=self.cari)
        cari_button.pack()
        
    def cari(self):
        lirik_dicari = self.input_lirik.get()
        hasil = self.pencarian(lirik_dicari)
        if len(hasil) == 0:
            notfound_label = tk.Label(self.window, text="judul tidak ditemukan", anchor="center")
            notfound_label.pack()
            return



        for judul in hasil:
            hasil_lirik = self.ambil_lirik(judul)
            song_label = tk.Label(self.window, text=judul, anchor="center")
            song_label.pack()

            lirik_text = tk.Text(self.window, width=20, height=15)
            lirik_text.insert("1.0", hasil_lirik)
            lirik_text.config(state="disabled")
            lirik_text.pack()

        close_btn = tk.Button(self.window, text="close", command=self.window.destroy, anchor='center')
        close_btn.pack()


