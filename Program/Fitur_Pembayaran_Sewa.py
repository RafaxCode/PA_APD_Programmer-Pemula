import os
import inquirer

def Fitur_Pembayaran_Sewa():
    Go_Back_Fitur_Pembayaran_Sewa = False
    while Go_Back_Fitur_Pembayaran_Sewa:
        # di sini tampilkan tagihan sewa
        opsi = [
            inquirer.List("Opsi Pilih Bayar Sewa", message="Pilih Opsi", choices=["Bayar Sewa", "Kembali"])
        ]
        jawaban = inquirer.prompt(opsi)
        Hasil_Opsi = jawaban["Opsi Pilih Bayar Sewa"]
        if Hasil_Opsi == "Bayar Sewa":
            # di sini program untuk penyewa membayar sewa (uang sewa akan dimasukkan ke dalam simpanan uang admin)
            # if uang bayar > tagihan sewa
                print("Pembayaran berhasil")
                print('=' * 40)
                kembali = input("Tekan Enter Untuk Kembali")
            # else
                print("Pembayaran gagal")
                print('=' * 40)
                kembali = input("Tekan Enter Untuk Kembali")
        elif Hasil_Opsi == "Kembali":
            Go_Back_Fitur_Pembayaran_Sewa = True