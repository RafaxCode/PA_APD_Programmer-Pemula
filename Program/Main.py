import os
import inquirer

import Autentikasi

Go_Out = False
while not Go_Out:
    Autentikasi.Menu_Autentikasi()
    os.system("cls")
    opsi = [
        inquirer.List("Opsi Pilih Keluar", message="Apakah Anda ingin keluar?", choices=["Ya", "Tidak"])
    ]
    jawaban = inquirer.prompt(opsi)
    Hasil_Opsi = jawaban["Opsi Pilih Keluar"]
    if Hasil_Opsi == "Ya":
        go_out = True
    elif Hasil_Opsi == "Tidak":
        pass