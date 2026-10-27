class AnggotaView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Manajemen Data Anggota")
        self.geometry("850x420")

        frame_kiri = ctk.CTkFrame(self, width=280)
        frame_kiri.pack(side="left", fill="y", padx=10, pady=10)
        frame_kanan = ctk.CTkFrame(self)
        frame_kanan.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        ctk.CTkLabel(frame_kiri, text="Form Data Anggota",
                     font=("Arial", 16, "bold")).pack(pady=10)

        ctk.CTkLabel(frame_kiri, text="Nama Anggota").pack(anchor="w", padx=15)
        self.entry_nama = ctk.CTkEntry(frame_kiri, width=240)
        self.entry_nama.pack(padx=15, pady=(0, 8))

        ctk.CTkLabel(frame_kiri, text="Alamat").pack(anchor="w", padx=15)
        self.entry_alamat = ctk.CTkEntry(frame_kiri, width=240)
        self.entry_alamat.pack(padx=15, pady=(0, 12))

        self.btn_simpan = ctk.CTkButton(frame_kiri, text="Simpan Data")
        self.btn_simpan.pack(padx=15, pady=4, fill="x")
        self.btn_perbarui = ctk.CTkButton(frame_kiri, text="Perbarui Data")
        self.btn_perbarui.pack(padx=15, pady=4, fill="x")
        self.btn_hapus = ctk.CTkButton(frame_kiri, text="Hapus Data",
                                       fg_color="#c0392b", hover_color="#962d22")
        self.btn_hapus.pack(padx=15, pady=4, fill="x")

        self.tabel = ttk.Treeview(frame_kanan, show="headings",
                                  columns=("id", "nama", "alamat"))
        for kode, teks, lebar in [("id", "ID", 50), ("nama", "Nama Anggota", 200),
                                  ("alamat", "Alamat", 250)]:
            self.tabel.heading(kode, text=teks)
            self.tabel.column(kode, width=lebar)
        self.tabel.pack(fill="both", expand=True, padx=10, pady=10)


if __name__ == "__main__":
    AnggotaView().mainloop()