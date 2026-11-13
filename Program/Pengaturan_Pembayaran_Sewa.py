import os
import inquirer

def Pengaturan_Pembayaran_Sewa():
    Go_Back_Pengaturan_Pembayaran_Sewa = False
    while not Go_Back_Pengaturan_Pembayaran_Sewa:
            os.system("cls")
#       # di sini tampilkan daftar penyewa dengan status bayar sewanya
#       # di sini program memilih nama penyewa
#       # di sini tampilkan informasi penyewa yang telah dipilih dari Data_Penyewa
#       # if penyewa yang ditampilkan sudah bayar:
            print("Pembayaran sewa telah lunas")
            print('=' * 40)
            kembali = input('Tekan Enter Untuk Kembali')  
#       # else:
            opsi = [
                inquirer.List("Opsi Pilih Pesan Pengingat", message="Pilih Opsi", choices=["Kirim Pesan Pengingat", "Kembali"])
            ]
            jawaban = inquirer.prompt(opsi)
            Hasil_Opsi = jawaban["Opsi Pilih Pesan Pengingat"]
            if Hasil_Opsi == "Kirim Pesan Pengingat":
#               # di sini program input pesan
                opsi = [
                    inquirer.List("Opsi Pilih Konfirmasi", message="Kirim pesan pengingat ke penyewa?", choices=["Ya", "Tidak"])
                ]
                jawaban = inquirer.prompt(opsi)
                Hasil_Opsi = jawaban["Opsi Pilih Kirim Pengingat"]
                if Hasil_Opsi == "Ya":
#                   # di sini program mengirim pesan ke penyewa
                    print("Pesan berhasil terkirim")
                    print('=' * 40)
                    kembali = input('Tekan Enter Untuk Kembali')
                    Go_Back_Pengaturan_Pembayaran_Sewa = True
                elif Hasil_Opsi == "Tidak":
                     Go_Back_Pengaturan_Pembayaran_Sewa = True
            elif Hasil_Opsi == "Kembali":
                 Go_Back_Pengaturan_Pembayaran_Sewa = True