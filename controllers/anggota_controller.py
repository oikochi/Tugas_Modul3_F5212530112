import tkinter.messagebox as messagebox
from models.anggota_model import AnggotaModel
from views.anggota_view import AnggotaView


class AnggotaController:
    def __init__(self):
        self.model = AnggotaModel()
        self.view = AnggotaView()

        # Binding tombol dan klik baris tabel
        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_perbarui.configure(command=self.perbarui_data)
        self.view.btn_hapus.configure(command=self.hapus_data)
        self.view.tabel.bind("<<TreeviewSelect>>", self.pilih_baris)

        self.muat_data_tabel()

    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)
        for no, a in enumerate(self.model.get_all_anggota(), start=1):
            # iid menyimpan id_anggota asli, kolom pertama hanya nomor urut
            self.view.tabel.insert("", "end", iid=str(a['id_anggota']),
                                   values=(no, a['nama'], a['alamat']))

    def bersihkan_form(self):
        self.view.entry_nama.delete(0, 'end')
        self.view.entry_alamat.delete(0, 'end')

    def ambil_id_terpilih(self):
        terpilih = self.view.tabel.selection()
        if not terpilih:
            return None
        return int(terpilih[0])

    def pilih_baris(self, event=None):
        terpilih = self.view.tabel.selection()
        if not terpilih:
            return
        _, nama, alamat = self.view.tabel.item(terpilih[0])["values"]
        self.bersihkan_form()
        self.view.entry_nama.insert(0, nama)
        self.view.entry_alamat.insert(0, alamat)

    def simpan_data(self):
        nama = self.view.entry_nama.get()
        alamat = self.view.entry_alamat.get()

        if not nama or not alamat:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        if self.model.create_anggota(nama, alamat):
            messagebox.showinfo("Sukses", "Data anggota berhasil disimpan!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat menyimpan data.")

    def perbarui_data(self):
        id_anggota = self.ambil_id_terpilih()
        if id_anggota is None:
            messagebox.showwarning("Peringatan", "Pilih data di tabel terlebih dahulu!")
            return

        nama = self.view.entry_nama.get()
        alamat = self.view.entry_alamat.get()
        if not nama or not alamat:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        if self.model.update_anggota(id_anggota, nama, alamat):
            messagebox.showinfo("Sukses", "Data anggota berhasil diperbarui!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat memperbarui data.")

    def hapus_data(self):
        id_anggota = self.ambil_id_terpilih()
        if id_anggota is None:
            messagebox.showwarning("Peringatan", "Pilih data di tabel terlebih dahulu!")
            return
        if not messagebox.askyesno("Konfirmasi", "Yakin ingin menghapus data ini?"):
            return

        if self.model.delete_anggota(id_anggota):
            messagebox.showinfo("Sukses", "Data anggota berhasil dihapus!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error", "Gagal menghapus. Data mungkin dipakai di tabel peminjaman.")

    def run(self):
        self.view.mainloop()

if __name__ == "__main__":
    AnggotaController().run()