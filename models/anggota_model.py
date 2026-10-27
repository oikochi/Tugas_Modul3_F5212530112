import mysql.connector
from config.database import get_connection


class AnggotaModel:
    def __init__(self):
        self.conn = get_connection()

    def create_anggota(self, nama, alamat):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO anggota (nama, alamat) VALUES (%s, %s)", (nama, alamat))
            self.conn.commit()
            return True
        except mysql.connector.Error as e:
            print("Error create:", e)
            self.conn.rollback()
            return False

    def get_all_anggota(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM anggota")
        return cursor.fetchall()

    def update_anggota(self, id_anggota, nama, alamat):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "UPDATE anggota SET nama=%s, alamat=%s WHERE id_anggota=%s",
                (nama, alamat, id_anggota))
            self.conn.commit()
            return True
        except mysql.connector.Error as e:
            print("Error update:", e)
            self.conn.rollback()
            return False

    def delete_anggota(self, id_anggota):
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM anggota WHERE id_anggota=%s", (id_anggota,))
            self.conn.commit()
            return True
        except mysql.connector.Error as e:
            print("Error delete:", e)
            self.conn.rollback()
            return False