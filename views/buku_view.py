import customtkinter as ctk
from tkinter import ttk


class BukuView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Manajemen Data Buku")
        self.geometry("950x480")

        # ===== Frame kiri: form input =====
        frame_kiri = ctk.CTkFrame(self, width=300)
        frame_kiri.pack(side="left", fill="y", padx=10, pady=10)
        frame_kiri.pack_propagate(False)

        ctk.CTkLabel(frame_kiri, text="Form Data Buku",
                     font=("Arial", 18, "bold")).pack(pady=15)

        ctk.CTkLabel(frame_kiri, text="Judul Buku").pack(anchor="w", padx=20)
        self.entry_judul = ctk.CTkEntry(frame_kiri, width=260)
        self.entry_judul.pack(padx=20, pady=(0, 10))

        ctk.CTkLabel(frame_kiri, text="Penulis").pack(anchor="w", padx=20)
        self.entry_penulis = ctk.CTkEntry(frame_kiri, width=260)
        self.entry_penulis.pack(padx=20, pady=(0, 10))

        ctk.CTkLabel(frame_kiri, text="Tahun Terbit").pack(anchor="w", padx=20)
        self.entry_tahun = ctk.CTkEntry(frame_kiri, width=260)
        self.entry_tahun.pack(padx=20, pady=(0, 15))

        self.btn_simpan = ctk.CTkButton(frame_kiri, text="Simpan Data")
        self.btn_simpan.pack(padx=20, pady=4, fill="x")

        self.btn_perbarui = ctk.CTkButton(frame_kiri, text="Perbarui Data")
        self.btn_perbarui.pack(padx=20, pady=4, fill="x")

        self.btn_hapus = ctk.CTkButton(frame_kiri, text="Hapus Data",
                                       fg_color="#c0392b", hover_color="#962d22")
        self.btn_hapus.pack(padx=20, pady=4, fill="x")

        # ===== Frame kanan: tabel data =====
        frame_kanan = ctk.CTkFrame(self)
        frame_kanan.pack(side="right", fill="both", expand=True, padx=(0, 10), pady=10)

        ctk.CTkLabel(frame_kanan, text="Daftar Buku",
                     font=("Arial", 18, "bold")).pack(pady=(15, 5))

        self.tabel = ttk.Treeview(frame_kanan, show="headings",
                                  columns=("id", "judul", "penulis", "tahun"))

        self.tabel.heading("id", text="ID")
        self.tabel.heading("judul", text="Judul")
        self.tabel.heading("penulis", text="Penulis")
        self.tabel.heading("tahun", text="Tahun Terbit")

        self.tabel.column("id", width=50, anchor="center")
        self.tabel.column("judul", width=260)
        self.tabel.column("penulis", width=180)
        self.tabel.column("tahun", width=100, anchor="center")

        scrollbar = ttk.Scrollbar(frame_kanan, orient="vertical",
                                  command=self.tabel.yview)
        self.tabel.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y", padx=(0, 10), pady=(0, 10))
        self.tabel.pack(side="left", fill="both", expand=True,
                        padx=(10, 0), pady=(0, 10))


if __name__ == "__main__":
    app = BukuView()
    app.mainloop()