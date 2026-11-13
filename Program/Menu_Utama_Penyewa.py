import os
import inquirer

import Fitur_Unit
import Fitur_Penitipan_Paket
import Fitur_Pembayaran_Sewa
import Fitur_Kelola_Akun

def Menu_Utama_Penyewa():
    Go_Back_Menu_Utama_Penyewa = False
    while not Go_Back_Menu_Utama_Penyewa:
        os.system("cls")
        opsi = [
            inquirer.List("Opsi Pilih Menu Utama Penyewa", message="Pilih Opsi", choices=["Daftar Unit", "Penitipan Paket", "Pembayaran Sewa", "Kelola Akun", "Log Out"])
        ]
        jawaban = inquirer.prompt(opsi)
        Hasil_Opsi = jawaban["Opsi Pilih Menu Utama Penyewa"]
        if Hasil_Opsi == "Daftar Unit":
            Fitur_Unit.Fitur_Unit()
        elif Hasil_Opsi == "Penitipan Paket":
            Fitur_Penitipan_Paket.Fitur_Penitipan_Paket()
        elif Hasil_Opsi == "Pembayaran Sewa":
            Fitur_Pembayaran_Sewa.Fitur_Pembayaran_Sewa()
        elif Hasil_Opsi == "Kelola Akun":
            Fitur_Kelola_Akun.Fitur_Kelola_Akun()
        elif Hasil_Opsi == "Log Out":
            Go_Back_Menu_Utama_Penyewa = True