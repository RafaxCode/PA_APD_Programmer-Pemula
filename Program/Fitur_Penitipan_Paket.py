import os
import inquirer

def Fitur_Penitipan_Paket():
    Go_Back_Fitur_Penitipan_Paket = False
    while not Go_Back_Fitur_Penitipan_Paket:
        os.system("cls")
#       # di sini tampilkan judul
#       # di sini program menampilkan daftar form dari semua form paket yang telah dibuat
        opsi = [
            inquirer.List("Opsi Pilih Fitur Penitipan Paket", message="Pilih Opsi", choices=["Buat Form", "Status Paket", "Hapus Form", "Kembali"])
        ]
        jawaban = inquirer.prompt(opsi)
        Hasil_Opsi = jawaban["Opsi Pilih Fitur Penitipan Paket"]
        if Hasil_Opsi == "Buat Form":
            Buat_Form()
        elif Hasil_Opsi == "Status Paket":
            Status_Paket()
        elif Hasil_Opsi == "Hapus Form":
            Hapus_Form()
        elif Hasil_Opsi == "Kembali":
            Go_Back_Fitur_Penitipan_Paket

def Buat_Form():
    # di sini program input form
    opsi = [
        inquirer.List("Opsi Pilih Konfirmasi", message="Apakah Anda ingin membuat form ini?", choices=["Ya", "Tidak"])
    ]
    jawaban = inquirer.prompt(opsi)
    Hasil_Opsi = jawaban["Opsi Pilih Konfirmasi"]
    if Hasil_Opsi == "Ya":
#       # di sini program simpan form ke Data_Paket
        print("Form telah dibuat")
        print('=' * 40)
        kembali = input('Tekan Enter Untuk Kembali')  
    elif Hasil_Opsi == "Tidak":
        pass

def Status_Paket():
    # if ada form:
        # di sini program menampilkan form paket beserta statusnya
        print('=' * 40)
        kembali = input('Tekan Enter Untuk Kembali')
    # else (tidak ada form)
        print("Belum ada form yang dibuat")
        print('=' * 40)
        kembali = input('Tekan Enter Untuk Kembali')  

def Hapus_Form():
    # if ada form:
        # di sini program penyewa memilih salah satu paket
        opsi = [
            inquirer.List("Opsi Pilih Konfirmasi", message="Apakah Anda ingin menghapus form ini?", choices=["Ya", "Tidak"])
        ]
        jawaban = inquirer.prompt(opsi)
        Hasil_Opsi = jawaban["Opsi Pilih Konfirmasi"]
        if Hasil_Opsi == "Ya":
    #       # simpan form ke Data_Paket
            print("Form berhasil dibuat")
            print('=' * 40)
            kembali = input('Tekan Enter Untuk Kembali')
        elif Hasil_Opsi == "Ya":
    #       # di sini program simpan form ke Data_Paket
            print("Form telah dibuat")
            print('=' * 40)
            kembali = input('Tekan Enter Untuk Kembali')  
        elif Hasil_Opsi == "Tidak":
            pass
    # else (tidak ada form)        
        print("Belum ada form yang dibuat")
        print('=' * 40)
        kembali = input('Tekan Enter Untuk Kembali')