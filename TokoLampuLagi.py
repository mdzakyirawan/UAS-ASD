import os
import datetime
from prettytable import PrettyTable
import getpass

class NodeLampu:
    def __init__(self, id_lampu, nama_lampu, harga, stok, next=None):
        self.id_lampu = id_lampu
        self.nama_lampu = nama_lampu
        self.harga = harga
        self.stok = stok
        self.next = next

class LinkedListLampu:
    def __init__(self):
        self.head = None

    def tambah_lampu(self, id_lampu, nama_lampu, harga, stok):
        new_node = NodeLampu(id_lampu, nama_lampu, harga, stok)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def hapus_lampu(self, id_lampu):
        temp = self.head
        if temp is not None:
            if temp.id_lampu == id_lampu:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.id_lampu == id_lampu:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return
        prev.next = temp.next
        temp = None

    def edit_lampu(self, id_lampu, nama_lampu, harga, stok):
        temp = self.head
        while temp is not None:
            if temp.id_lampu == id_lampu:
                temp.nama_lampu = nama_lampu
                temp.harga = harga
                temp.stok = stok
                break
            temp = temp.next

    def tampilkan_lampu(self):
        temp = self.head
        x = PrettyTable()
        x.field_names = ["ID Lampu", "Nama Lampu", "Harga", "Stok"]
        while temp is not None:
            x.add_row([temp.id_lampu, temp.nama_lampu, format(temp.harga, ','), temp.stok])
            temp = temp.next
        print(x)

class Pelanggan:
    def __init__(self, nama, gender, usia):
        self.nama = nama
        self.gender = gender
        self.usia = usia
        self.saldo = 300000
        self.nota = []

    def sapaan(self):
        if self.gender == "L":
            if 18 <= self.usia <= 30:
                return f"Selamat datang, Mas {self.nama}!"
            else:
                return f"Selamat datang, Bapak {self.nama}!"
        elif self.gender == "P":
            if 18 <= self.usia <= 30:
                return f"Selamat datang, Mbak {self.nama}!"
            else:
                return f"Selamat datang, Ibu {self.nama}!"
        else:
            return f"Selamat datang, {self.nama}!"

    def beli_lampu(self, id_lampu, jumlah):
        temp = lampu.head
        while temp is not None:
            if temp.id_lampu == id_lampu:
                if temp.stok >= jumlah:
                    total = temp.harga * jumlah
                    diskon = 0
                    if total >= 250000:
                        diskon = 0.15
                    elif total >= 100000:
                        diskon = 0.10
                    if diskon > 0:
                        total -= total * diskon
                        total = int(total)
                        print(f"Anda dapat diskon {int(diskon * 100)}%")
                    print("Total Harga: Rp", format(total, ','))
                    if self.saldo >= total:
                        konfirmasi = input("Apakah Anda Yakin Ingin Membeli Lampu Ini? (y/n): ")
                        if konfirmasi == "y":
                            temp.stok -= jumlah
                            self.saldo -= total
                            self.nota.append((temp.nama_lampu, jumlah, temp.harga, total))
                            print("Lampu Berhasil Dibeli")
                            print("Saldo Anda Sekarang: Rp", format(self.saldo, ','))
                            input("Tekan Enter Untuk Melanjutkan")
                            os.system("cls")
                        else:
                            print("Transaksi Dibatalkan")
                            input("Tekan Enter Untuk Kembali")
                            os.system("cls")
                    else:
                        print("Saldo Anda Tidak Cukup")
                        print("Silahkan Tambahkan Saldo Terlebih Dahulu")
                        pilihan = input("Apakah Anda Ingin Mengisi Saldo? (y/n): ")
                        if pilihan == "y":
                            saldo = int(input("Jumlah Saldo: "))
                            self.isi_saldo(saldo)
                            self.beli_lampu(id_lampu, jumlah)  # Lakukan transaksi kembali
                        else:
                            print("Transaksi Dibatalkan")
                            input("Tekan Enter Untuk Kembali")
                            os.system("cls")
                else:
                    print("Stok Lampu Tidak Cukup")
                break
            temp = temp.next

    def isi_saldo(self, saldo):
        self.saldo += saldo
        print("Saldo Berhasil Ditambahkan")
        print("Saldo Anda Sekarang: Rp", format(self.saldo, ','))
        input("Tekan Enter Untuk Kembali")
        os.system("cls")

    def cek_saldo(self):
        print("| Saldo Anda: Rp", format(self.saldo, ',') )

    def cetak_nota(self):
        print("-------------------------------------------------")
        print("|                   Nota Belanja                |")
        print("-------------------------------------------------")
        x = PrettyTable()
        x.field_names = ["Nama Lampu", "Jumlah", "Harga Satuan", "Total Harga"]
        total_belanja = 0
        for item in self.nota:
            x.add_row([item[0], item[1], format(item[2], ','), format(item[3], ',')])
            total_belanja += item[3]
        print(x)
        print(f"Total Belanja: Rp {format(total_belanja, ',')}")
        print("-------------------------------------------------")

lampu = LinkedListLampu()
lampu.tambah_lampu(1, "Lampu LED", 20000, 10)
lampu.tambah_lampu(2, "Lampu Neon", 50000, 5)
lampu.tambah_lampu(3, "Lampu Bohlam", 15000, 20)
lampu.tambah_lampu(4, "Lampu Tidur", 50000, 15)

pelanggan_data = {
    "putra": Pelanggan("Putra", "L", 25),
    "putri": Pelanggan("Putri", "P", 26),
    "adimas": Pelanggan("Adimas", "L", 35),
    "adelia": Pelanggan("Adelia", "P", 36)
}

def menu_admin(lampu):
    os.system("cls")
    while True:
        print("----------------------------------------------------")
        print("|                  Menu Admin                      |")
        print("----------------------------------------------------")
        print("| 1. Tambah Lampu                                  |")
        print("| 2. Hapus Lampu                                   |")
        print("| 3. Edit Lampu                                    |")
        print("| 4. Tampilkan Lampu                               |")
        print("| 5. Logout                                        |")
        print("----------------------------------------------------")
        pilihan = input("Pilih Menu: ")
        if pilihan == "1":
            id_lampu = int(input("ID Lampu: "))
            nama_lampu = input("Nama Lampu: ")
            harga = int(input("Harga: "))
            stok = int(input("Stok: "))
            lampu.tambah_lampu(id_lampu, nama_lampu, harga, stok)
        elif pilihan == "2":
            id_lampu = int(input("ID Lampu: "))
            lampu.hapus_lampu(id_lampu)
        elif pilihan == "3":
            id_lampu = int(input("ID Lampu: "))
            nama_lampu = input("Nama Lampu: ")
            harga = int(input("Harga: "))
            stok = int(input("Stok: "))
            lampu.edit_lampu(id_lampu, nama_lampu, harga, stok)
        elif pilihan == "4":
            lampu.tampilkan_lampu()
        elif pilihan == "5":
            login()

def menu_pelanggan(lampu, pelanggan): 
    os.system("cls")
    print(pelanggan.sapaan())
    while True:
        print("-------------------------------------------------")
        print("|                   Toko Lampu                  |")
        print("-------------------------------------------------")
        pelanggan.cek_saldo()  
        print("| 1. Beli Lampu                                 |")
        print("| 2. Isi Saldo                                  |")
        print("| 3. Lihat Nota                                 |")
        print("| 4. Logout                                     |")
        print("-------------------------------------------------")
        pilihan = input("Pilih Menu: ")
        if pilihan == "1":
            os.system("cls")
            while True:
                lampu.tampilkan_lampu()
                id_lampu = int(input("Pilih ID Lampu (0 untuk selesai): "))
                if id_lampu == 0:
                    os.system("cls")
                    break
                else:
                    jumlah = int(input("Jumlah: "))
                    pelanggan.beli_lampu(id_lampu, jumlah)
        elif pilihan == "2":
            saldo = int(input("Jumlah Saldo: "))
            pelanggan.isi_saldo(saldo)
        elif pilihan == "3":
            os.system("cls")
            pelanggan.cetak_nota()
            input("Tekan Enter Untuk Kembali")
            os.system("cls")
        elif pilihan == "4":
            login()

def jam_operasional():
    sekarang = datetime.datetime.now().time()
    buka = datetime.time(9, 0, 0)
    tutup = datetime.time(17, 0, 0)
    return buka <= sekarang <= tutup

def login():
    os.system("cls")
    if not jam_operasional():
        print("----------------------------------------------------")
        print("|        Maaf, Toko Lampu Dzaky sedang tutup       |")
        print("|  Silahkan datang kembali pada jam 09.00 - 17.00  |")
        print("----------------------------------------------------")
        return
    while True:
        print("O----------------------------------------O")
        print("O - Selamat Datang di Toko Lampu Dzaky - O")
        print("O             TERANGNYA OOYY             O")
        print("------------------------------------------")
        print("|  Silahkan Login Terlebih Dahulu")
        username = input("|  Masukkan Username: ")
        password = getpass.getpass("|  Masukkan Password: ")
        if username == "admin" and password == "123":
            menu_admin(lampu)
        elif username in pelanggan_data and password == "123":
            pelanggan = pelanggan_data[username]
            menu_pelanggan(lampu, pelanggan)
        else:
            print("Username atau Password Salah")
            login()

if __name__ == "__main__":
    login()
