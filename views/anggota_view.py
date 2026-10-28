import customtkinter as ctk
from tkinter import ttk


class AnggotaView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Manajemen Data Anggota Perpustakaan")
        self.geometry("950x480")

        # ===== Frame kiri: form input =====
        frame_kiri = ctk.CTkFrame(self, width=300)
        frame_kiri.pack(side="left", fill="y", padx=10, pady=10)
        frame_kiri.pack_propagate(False)

        ctk.CTkLabel(frame_kiri, text="Form Data Anggota",
                     font=("Arial", 18, "bold")).pack(pady=15)

        ctk.CTkLabel(frame_kiri, text="Nama Anggota").pack(anchor="w", padx=20)
        self.entry_nama = ctk.CTkEntry(frame_kiri, width=260)
        self.entry_nama.pack(padx=20, pady=(0, 10))

        ctk.CTkLabel(frame_kiri, text="Alamat").pack(anchor="w", padx=20)
        self.entry_alamat = ctk.CTkEntry(frame_kiri, width=260)
        self.entry_alamat.pack(padx=20, pady=(0, 15))

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

        ctk.CTkLabel(frame_kanan, text="Daftar Anggota",
                     font=("Arial", 18, "bold")).pack(pady=(15, 5))
        style = ttk.Style()
        style.configure("Treeview", rowheight=28)

        self.tabel = ttk.Treeview(frame_kanan, show="headings",
                                  columns=("no", "nama", "alamat"))
        

        self.tabel.heading("no", text="No")
        self.tabel.heading("nama", text="Nama Anggota")
        self.tabel.heading("alamat", text="Alamat")

        self.tabel.column("no", width=50, anchor="center")
        self.tabel.column("nama", width=220)
        self.tabel.column("alamat", width=300)

        scrollbar = ttk.Scrollbar(frame_kanan, orient="vertical",
                                  command=self.tabel.yview)
        self.tabel.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y", padx=(0, 10), pady=(0, 10))
        self.tabel.pack(side="left", fill="both", expand=True,
                        padx=(10, 0), pady=(0, 10))


if __name__ == "__main__":
    app = AnggotaView()
    app.mainloop()