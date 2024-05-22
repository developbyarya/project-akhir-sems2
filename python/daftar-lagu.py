import tkinter as tk

class TambahLagu:
    def __init__(self, root, handler=None):
        self.window = tk.Toplevel(root)
        self.window.title("TambahLagu")
        self.widget()
        self.handler = handler
    def widget(self):
        song_label = tk.Label(self.window, text="Song: ")
        self.song_input = tk.Entry(self.window)
        song_label.pack()
        self.song_input.pack()


        singer_label = tk.Label(self.window, text="Singer: ")
        self.singer_input = tk.Entry(self.window)
        singer_label.pack()
        self.singer_input.pack()


        lyric_label = tk.Label(self.window, text="Lyric: ")
        self.lyric_input = tk.Text(self.window, height=10, width=30)
        lyric_label.pack()
        self.lyric_input.pack()

        save_button = tk.Button(self.window, text="Simpan", command=self.save)
        save_button.pack()
    def save(self):
        title = self.song_input.get() + " - " + self.singer_input.get()
        lyric = self.lyric_input.get("1.0", "end-1c")
        self.handler(title, lyric)

        self.window.destroy()


