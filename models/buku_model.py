import mysql.connector
from config.database import get_connection


class BukuModel:
    def __init__(self):
        self.conn = get_connection()

    def create_buku(self, judul, penulis, tahun):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO buku (judul, penulis, tahun_terbit) VALUES (%s, %s, %s)",
                (judul, penulis, tahun))
            self.conn.commit()
            return True
        except mysql.connector.Error as e:
            print("Error create:", e)
            self.conn.rollback()
            return False

    def get_all_buku(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM buku")
        return cursor.fetchall()

    def update_buku(self, id_buku, judul, penulis, tahun):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "UPDATE buku SET judul=%s, penulis=%s, tahun_terbit=%s WHERE id_buku=%s",
                (judul, penulis, tahun, id_buku))
            self.conn.commit()
            return True
        except mysql.connector.Error as e:
            print("Error update:", e)
            self.conn.rollback()
            return False

    def delete_buku(self, id_buku):
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM buku WHERE id_buku=%s", (id_buku,))
            self.conn.commit()
            return True
        except mysql.connector.Error as e:
            print("Error delete:", e)
            self.conn.rollback()
            return False