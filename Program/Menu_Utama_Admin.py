import os
import inquirer

import Pengaturan_Unit
import Pengaturan_Penitipan_Paket
import Pengaturan_Pembayaran_Sewa
import Pengaturan_Kelola_Akun

def Menu_Utama_Admin():
    Go_Back_Menu_Utama_Admin = False
    while not Go_Back_Menu_Utama_Admin:
        os.system("cls")
        opsi = [
            inquirer.List("Opsi Pilih Menu Utama Admin", message="Pilih Opsi", choices=["Pengaturan Unit", "Penitipan Paket", "Pembayaran Sewa", "Kelola Akun", "Log Out"])
        ]
        jawaban = inquirer.prompt(opsi)
        Hasil_Opsi = jawaban["Opsi Pilih Menu Utama Admin"]
        if Hasil_Opsi == "Pengaturan Unit":
            Pengaturan_Unit.Pengaturan_Unit()
        elif Hasil_Opsi == "Penitipan Paket":
            Pengaturan_Penitipan_Paket.Pengaturan_Penitipan_Paket()
        elif Hasil_Opsi == "Pembayaran Sewa":
            Pengaturan_Pembayaran_Sewa.Pengaturan_Pembayaran_Sewa()
        elif Hasil_Opsi == "Kelola Akun":
            Pengaturan_Kelola_Akun.Pengaturan_Kelola_Akun()
        elif Hasil_Opsi == "Log Out":
            Go_Back_Menu_Utama_Admin = True