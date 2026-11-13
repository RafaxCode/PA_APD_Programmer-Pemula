import os
import inquirer
import time

def Pengaturan_Unit():
    Go_Back_Pengaturan_Unit = False
    while not Go_Back_Pengaturan_Unit:
        os.system("cls")
        opsi = [
            inquirer.List("Opsi Pilih Pengaturan Unit", message="Pilih Opsi", choices=["Daftar Unit", "Tambah Unit", "Status Unit", "Hapus Unit", "Kembali"])
        ]
        jawaban = inquirer.prompt(opsi)
        Hasil_Opsi = jawaban["Opsi Pilih Pengaturan Unit"]
        if Hasil_Opsi == "Daftar Unit":
            Daftar_Unit()
        elif Hasil_Opsi == "Tambah Unit":
            Tambah_Unit()
        elif Hasil_Opsi == "Status Unit":
            Status_Unit()
        elif Hasil_Opsi == "Hapus Unit":
            Hapus_Unit()
        elif Hasil_Opsi == "Kembali":
            Go_Back_Pengaturan_Unit = True

def Daftar_Unit():
    os.system("cls")
    # Tampilkan daftar unit
    print('=' * 40)
    kembali = input('Tekan Enter Untuk Kembali')

def Tambah_Unit():
    os.system("cls")
    # program tambah unit
    opsi = [
        inquirer.List("Opsi Pilih Konfirmasi", message="Apakah Anda ingin menambahkan unit ini?", choices=["Ya", "Tidak"])
    ]
    jawaban = inquirer.prompt(opsi)
    Hasil_Opsi = jawaban["Opsi Pilih Konfirmasi"]
    if Hasil_Opsi == "Ya":
        # di sini program unit ditambahkan ke Data_Unit
        print("Unit berhasil ditambahkan")
        print('=' * 40)
        kembali = input('Tekan Enter Untuk Kembali')
    elif Hasil_Opsi == "Tidak":
        pass

def Status_Unit():
    os.system("cls")
    # di sini program unit mengubah status unit
    opsi = [
        inquirer.List("Opsi Pilih Konfirmasi", message="Apakah Anda ingin mengubah status unit ini?", choices=["Ya", "Tidak"])
    ]
    jawaban = inquirer.prompt(opsi)
    Hasil_Opsi = jawaban["Opsi Pilih Konfirmasi"]
    if Hasil_Opsi == "Ya":
        print("Status berhasil diubah")
        print('=' * 40)
        kembali = input('Tekan Enter Untuk Kembali')
    elif Hasil_Opsi == "Tidak":
        pass

def Hapus_Unit():
    os.system("cls")
    # di sini program hapus unit
    opsi = [
        inquirer.List("Opsi Pilih Konfirmasi", message="Apakah Anda ingin menghapus unit ini?", choices=["Ya", "Tidak"])
    ]
    jawaban = inquirer.prompt(opsi)
    Hasil_Opsi = jawaban["Opsi Pilih Konfirmasi"]
    if Hasil_Opsi == "Ya":
        print("Unit berhasil dihapus")
        print('=' * 40)
        kembali = input('Tekan Enter Untuk Kembali')
    elif Hasil_Opsi == "Tidak":
        pass