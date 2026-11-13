import os
import inquirer

def Pengaturan_Kelola_Akun():
    Go_Back_Pengaturan_Kelola_Akun = False
    while not Go_Back_Pengaturan_Kelola_Akun:
        os.system("cls")
#       # di sini tampilkan judul kelola akun, username admin, password admin, dan jumlah simpanan uang admin
        opsi = [
            inquirer.List("Opsi Pilih Pengaturan Kelola Akun", message="Pilih Opsi", choices=["Ubah Username", "Ubah Password", "Kembali"])
        ]
        jawaban = inquirer.prompt(opsi)
        Hasil_Opsi = jawaban["Opsi Pilih Pengaturan Kelola Akun"]

        if Hasil_Opsi == "Ubah Username":
#           # di sini program mengganti username lama dengan username baru
#           # if username admin yang diinput sama dengan yang ada di Data_Penyewa
                print("Username tidak boleh sama dengan penyewa")
                print('=' * 40)
                kembali = input('Tekan Enter Untuk Kembali')
#           # elif username admin yang diinput kosong
                print("Username tidak boleh kosong")
                print('=' * 40)
                kembali = input("Tekan Enter Untuk Kembali")
#           # else:  
                opsi = [
                    inquirer.List("Opsi Pilih Konfirmasi", message="Apakah Anda ingin mengganti dengan username ini?", choices=["Ya", "Tidak"])
                ]
                jawaban = inquirer.prompt(opsi)
                Hasil_Opsi = jawaban["Opsi Pilih Konfirmasi"]
                if Hasil_Opsi == "Ya":
                    # simpan username admin yang baru
                    print("Username telah diganti")
                    print('=' * 40)
                    kembali = input("Tekan Enter Untuk Kembali")
                elif Hasil_Opsi == "Tidak":
                    pass

        elif Hasil_Opsi == "Ubah Password":
#           # di sini program mengganti password lama dengan password baru
            opsi = [
                inquirer.List("Opsi Pilih Konfirmasi", message="Apakah Anda ingin mengganti dengan password ini?", choices=["Ya", "Tidak"])
            ]
            jawaban = inquirer.prompt(opsi)
            Hasil_Opsi = jawaban["Opsi Pilih Konfirmasi"]
            if Hasil_Opsi == "Ya":
                # simpan password admin yang baru
                print("Password telah diganti")
                print('=' * 40)
                kembali = input("Tekan Enter Untuk Kembali")
            elif Hasil_Opsi == "Tidak":
                pass

        elif Hasil_Opsi == "Kembali":
            Go_Back_Pengaturan_Kelola_Akun = True