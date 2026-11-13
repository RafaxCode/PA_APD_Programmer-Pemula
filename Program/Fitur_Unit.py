import os
import inquirer

def Fitur_Unit():
    os.system("cls")
    Go_Back_Fitur_Daftar_Unit = False
    while not Go_Back_Fitur_Daftar_Unit:
#       # tampilan menu
        opsi = [
            inquirer.List("Opsi Pilih Fitur Unit", message="Pilih Opsi", choices=["Daftar Unit", "Unit Sewa Anda"])
        ]
        jawaban = inquirer.prompt(opsi)
        Hasil_Opsi = jawaban["Opsi Pilih Fitur Unit"]
        if Hasil_Opsi == "Daftar Unit":
            Daftar_Unit()
        elif Hasil_Opsi == "Unit Sewa Anda":
            Unit_Sewa()
        elif Hasil_Opsi == "Kembali":
            Go_Back_Fitur_Daftar_Unit = True

def Daftar_Unit():
    os.system("cls")
#   # di sini tampilkan daftar unit
    opsi = [
        inquirer.List("Opsi Pilih Sewa Unit", message="Apakah Anda ingin menyewa unit?", choices=["Ya", "Tidak"])
    ]
    jawaban = inquirer.prompt(opsi)
    Hasil_Opsi = jawaban["Opsi Pilih Sewa Unit"]
    if Hasil_Opsi == "Ya":
#           # di sini penyewa memilih unit
#           # di sini program menampilkan informasi dari Data_Unit berdasarkan unit yang telah dipilih
        opsi = [
            inquirer.List("Opsi Pilih Konfirmasi", message="Apakah Anda ingin menyewa unit ini?", choices=["Ya", "Tidak"])
        ]
        jawaban = inquirer.prompt(opsi)
        Hasil_Opsi = jawaban["Opsi Pilih Konfirmasi"]
        if Hasil_Opsi == "Ya":
#               # di sini program input data penyewa yang akan di simpan di Data_Penyewa
#               # di sini program bayar sewa awal bagi penyewa
            print("Unit berhasil disewa")
            print('=' * 40)
            kembali = input("Tekan Enter Untuk Kembali")
        elif Hasil_Opsi == "Tidak":
            pass
    elif Hasil_Opsi == "Tidak":
        pass

def Unit_Sewa():
    os.system("cls")
    # di sini tampilkan daftar unit yang telah disewa
    # di sini penyewa memilih unit
#   # di sini program menampilkan informasi dari Data_Unit berdasarkan unit yang telah dipilih
    opsi = [
        inquirer.List("Opsi Pilih Unit Sewa", message="Pilih Opsi", choices=["Batalkan Sewa", "Kembali"])
    ]
    jawaban = inquirer.prompt(opsi)
    Hasil_Opsi = jawaban["Opsi Pilih Unit Sewa"]
    if Hasil_Opsi == "Batalkan Sewa":
        opsi = [
            inquirer.List("Opsi Pilih Unit Sewa", message="Pilih Opsi", choices=["Batalkan Sewa", "Kembali"])
        ]
        jawaban = inquirer.prompt(opsi)
        Hasil_Opsi = jawaban["Opsi Pilih Unit Sewa"]
        if Hasil_Opsi == "Batalkan Sewa"
            opsi = [
                inquirer.List("Opsi Pilih Batalkan Sewa", message="Apakah Anda ingin membatalkan sewa unit ini?", choices=["Ya", "Tidak"])
            ]
            jawaban = inquirer.prompt(opsi)
            Hasil_Opsi = jawaban["Opsi Pilih Batalkan Sewa"]
            if Hasil_Opsi == "Ya":
#               # di sini program membatalkan sewa (menghapus unit dari daftar unit sewa anda, mengubah informasi unit pada Data_Unit dari statusnya penuh menjadi tersedia)
                print("Sewa Unit berhasil dibatalkan")
                print('=' * 40)
                kembali = input("Tekan Enter Untuk Kembali")
            elif Hasil_Opsi == "Tidak":
                pass