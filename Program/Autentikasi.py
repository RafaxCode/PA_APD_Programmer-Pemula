import os
import inquirer

import Menu_Utama_Admin
import Menu_Utama_Penyewa


def Menu_Autentikasi():
    Go_Back_Autentikasi = False
    while not Go_Back_Autentikasi:
        os.system("cls")
        opsi = [
            inquirer.List("Opsi Pilih Menu Autentikasi", message="Pilih Opsi", choices=["Log In", "Sign In", "Keluar"])
        ]
        jawaban = inquirer.prompt(opsi)
        Hasil_Opsi = jawaban["Opsi Pilih Menu Autentikasi"]
        if Hasil_Opsi == "Log In":
            Menu_Log_In()
        elif Hasil_Opsi == "Sign In":
            Menu_Sign_In()
        elif Hasil_Opsi == "Keluar":
            Go_Back_Autentikasi = True

def Menu_Log_In():
    os.system("cls")
    # Periksa Data_Akun
    # if Username_Log_In == Username and Password_Log_In == Password:
        opsi = [
            inquirer.List("Opsi Pilih Menu Log In", message="Apakah Anda ingin masuk?", choices=["Ya", "Tidak"])
        ]
        jawaban = inquirer.prompt(opsi)
        Hasil_Opsi = jawaban["Opsi Pilih Menu Log In"]
        if Hasil_Opsi == "Ya":
            # if Username_Log_In == Username_Admin:
                Menu_Utama_Admin.Menu_Utama_Admin()
            # else:
                Menu_Utama_Penyewa.Menu_Utama_Penyewa()
        elif Hasil_Opsi == "Tidak":
            pass
    # else:
        # "Login gagal"

def Menu_Sign_In():
    os.system("cls")
    # Periksa Data_Akun
    # if Username_Log_In in Data_Akun and Username_Log_In == Username_Admin:
        # "Username sudah digunakan"
    # elif username admin yang diinput kosong
        print("Username tidak boleh kosong")
        print('=' * 40)
        kembali = input("Tekan Enter Untuk Kembali")
    # else:
        opsi = [
            inquirer.List("Opsi Pilih Menu Sign In", message="Simpan Akun?", choices=["Ya", "Tidak"])
        ]
        jawaban = inquirer.prompt(opsi)
        Hasil_Opsi = jawaban["Opsi Pilih Menu Sign In"]
        if Hasil_Opsi == "Ya":
            # Simpan ke Data_Akun
        elif Hasil_Opsi == "Tidak":
            pass