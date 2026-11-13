import os
import inquirer

def Fitur_Pembayaran_Sewa():
    # di sini tampilkan tagihan sewa
    opsi = [
        inquirer.List("Opsi Pilih Bayar Sewa", message="Pilih Opsi", choices=["Bayar Sewa", "Kembali"])
    ]
    jawaban = inquirer.prompt(opsi)
    Hasil_Opsi = jawaban["Opsi Pilih Bayar Sewa"]
    if Hasil_Opsi == "Bayar Sewa":
        # di sini program untuk penyewa membayar sewa (uang sewa akan dimasukkan ke dalam simpanan uang admin)
        # di sini 
        print("Sewa Unit berhasil dibatalkan")
        print('=' * 40)
        kembali = input("Tekan Enter Untuk Kembali")