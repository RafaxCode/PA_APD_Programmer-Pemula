import os
import inquirer

def Pengaturan_Penitipan_Paket():
    Go_Back_Pengaturan_Penitipan_Paket = False
    while not Go_Back_Pengaturan_Penitipan_Paket:
        os.system("cls")
#       # if ada paket
#           # tampilkan daftar paket
            opsi = [
                inquirer.List("Opsi Pilih Pengaturan Penitipan Paket", message="Pilih Opsi", choices=["Pilih Paket", "Kembali"])
            ]
            jawaban = inquirer.prompt(opsi)
            Hasil_Opsi = jawaban["Opsi Pilih Pengaturan Penitipan Paket"]
            if Hasil_Opsi == "Pilih Paket":
#               # di sini program memilih paket dari daftar paket
                opsi = [
                    inquirer.List("Opsi Pilih Paket Sampai", message="Apakah paket sudah sampai?", choices=["Ya", "Tidak"])
                ]
                jawaban = inquirer.prompt(opsi)
                Hasil_Opsi = jawaban["Opsi Pilih Paket Sampai"]
                if Hasil_Opsi == "Ya":
#                   # di sini program mengubah status paket ke "Paket Sudah Sampai"
                    opsi = [
                        inquirer.List("Opsi Pilih Paket Diterima", message="Apakah paket sudah diterima?", choices=["Ya", "Tidak"])
                    ]
                    jawaban = inquirer.prompt(opsi)
                    Hasil_Opsi = jawaban["Opsi Pilih Paket Diterima"]
                    if Hasil_Opsi == "Ya":
#                       # di sini program menghapus form penitipan paket
                        print("Form telah dihapus")
                        print('=' * 40)
                        kembali = input('Tekan Enter Untuk Kembali')  
                        Go_Back_Pengaturan_Penitipan_Paket = True
                    elif Hasil_Opsi == "Tidak":
                        Go_Back_Pengaturan_Penitipan_Paket = True
                elif Hasil_Opsi == "Tidak":
                    Go_Back_Pengaturan_Penitipan_Paket = True
            elif Hasil_Opsi == "Kembali":
                Go_Back_Pengaturan_Penitipan_Paket = True
#       # else tidak ada paket
            print("Unit berhasil ditambahkan")
            print('=' * 40)
            kembali = input('Tekan Enter Untuk Kembali')        