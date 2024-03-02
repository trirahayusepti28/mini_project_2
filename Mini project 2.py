import os
from prettytable import PrettyTable

os.system("cls")

print('''
+==================================================================================================+
|                                   SISTEM PEMINJAMAN BARANG                                       |
+==================================================================================================+
''')

# Definisi kelas Node untuk menyimpan data barang
class Node:
    def __init__(self, id_barang, nama_barang, jumlah, kondisi, lokasi, nama_pemilik):
        self.id_barang = id_barang
        self.nama_barang = nama_barang
        self.jumlah = jumlah
        self.kondisi = kondisi
        self.lokasi = lokasi
        self.nama_pemilik = nama_pemilik
        self.next = None

# Definisi kelas LinkedList untuk mengelola data barang
class LinkedList:
    def __init__(self):
        self.head = None

    '''=========================================================================================================='''
    '''                                       CREATE (Menambahkan Barang)                                        '''
    '''=========================================================================================================='''

    # Fungsi untuk menambah barang baru ke inventaris
    def tambah_barang(self, id_barang, nama_barang, jumlah, kondisi, lokasi, nama_pemilik, posisi="akhir"):
        new_node = Node(id_barang, nama_barang, jumlah, kondisi, lokasi, nama_pemilik)
        if not self.head:
            self.head = new_node
        else:
            if posisi == "awal":
                new_node.next = self.head
                self.head = new_node
            elif posisi == "tengah":
                current = self.head
                count = 0
                while current:
                    count += 1
                    current = current.next
                middle = count // 2

                current = self.head
                for _ in range(middle - 1):
                    current = current.next

                new_node.next = current.next
                current.next = new_node
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = new_node

    '''=========================================================================================================='''
    '''                                       READ (Menampilkan Barang)                                          '''
    '''=========================================================================================================='''
    # Fungsi untuk menampilkan semua barang dalam inventaris
    def tampilkan_semua_barang(self):
        if not self.head:
            print("-- Inventaris barang kosong --")
        else:
            table = PrettyTable()
            table.field_names = ["ID", "Nama Barang", "Jumlah", "Kondisi", "Lokasi", "Nama Pemilik"]
            current = self.head
            while current:
                table.add_row([current.id_barang, current.nama_barang, current.jumlah, current.kondisi, current.lokasi, current.nama_pemilik])
                current = current.next
            print(table)

    # Fungsi untuk mencari barang berdasarkan ID
    def cari_barang(self, id_barang):
        if not self.head:
            print("-- Inventaris barang kosong --")
            return None

        current = self.head
        while current:
            if current.id_barang == id_barang:
                print(f"\nBarang dengan ID {id_barang} ditemukan:")
                print(f"ID Barang: {current.id_barang}, Nama Barang: {current.nama_barang}, Jumlah: {current.jumlah}, Kondisi: {current.kondisi}, Lokasi: {current.lokasi}, Nama Pemilik: {current.nama_pemilik}")
                return current
            current = current.next

        print(f"Barang dengan ID {id_barang} tidak ditemukan.")
        return None

    # Fungsi untuk memperbarui informasi barang
    def update_barang(self, id_barang, field, value):
        node = self.cari_barang(id_barang)
        if node:
            if hasattr(node, field):
                setattr(node, field, value)
                print("-- Data barang berhasil diperbarui --")
            else:
                print("-- Field yang dimasukkan tidak valid --")

    # Fungsi untuk menghapus barang dari inventaris
    def hapus_barang(self, id_barang):
        if not self.head:
            print("-- Inventaris barang kosong --")
            return

        if self.head.id_barang == id_barang:
            self.head = self.head.next
            print("-- Barang berhasil dihapus dari inventaris --")
            return

        current = self.head
        while current.next:
            if current.next.id_barang == id_barang:
                current.next = current.next.next
                print("-- Barang berhasil dihapus dari inventaris --")
                return
            current = current.next

        print(f"Tidak ada barang dengan ID {id_barang}.")

# Definisi kelas CustomerNode untuk menyimpan data customer
class CustomerNode:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.nama = ""
        self.alamat = ""
        self.nomor_hp = ""
        self.riwayat_pinjam = []
        self.next = None

    def tambah_riwayat_pinjam(self, barang, jumlah_pinjam):
        self.riwayat_pinjam.append((barang, self.nama, self.alamat, self.nomor_hp, jumlah_pinjam))

# Definisi kelas CustomerLinkedList untuk mengelola data customer
class CustomerLinkedList:
    def __init__(self):
        self.head = None

    def add_customer(self, username, password):
        new_customer = CustomerNode(username, password)
        if not self.head:
            self.head = new_customer
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_customer

    def find_customer(self, username):
        current = self.head
        while current:
            if current.username == username:
                return current
            current = current.next
        return None

# Membuat objek LinkedList untuk inventaris dan CustomerLinkedList untuk daftar customer
customer_list = CustomerLinkedList()
inventaris = LinkedList()

# Inisialisasi inventaris barang
inventaris.tambah_barang("B001", "Laptop", 5, "Baik", "Gudang A", "Anni")
inventaris.tambah_barang("B002", "Printer", 3, "Rusak", "Gudang B", "Budi")
inventaris.tambah_barang("B003", "Monitor", 8, "Baik", "Gudang C", "Cici")
inventaris.tambah_barang("B004", "Keyboard", 10, "Baik", "Gudang D", "Dini")
inventaris.tambah_barang("B005", "Mouse", 15, "Baik", "Gudang E", "Eva")


'''=========================================================================================================='''
'''                                                 MENU ADMIN                                               '''
'''=========================================================================================================='''
# Fungsi untuk menampilkan menu admin
def admin_menu():
    # Username dan password admin
    username = "anni"
    password = "2809"

    input_username = input("Username: ")
    input_password = input("Password: ")

    # Memeriksa apakah username dan password sesuai
    if input_username == username and input_password == password:
        print("Login berhasil.")
        while True:
            print("\n=== Menu Admin ===")
            print("1. Tambah Barang")
            print("2. Tampilkan Semua Barang")
            print("3. Cari Barang")
            print("4. Update Barang")
            print("5. Hapus Barang")
            print("6. Keluar")

            pilihan = input("Masukkan pilihan (1/2/3/4/5/6): ")

            if pilihan == "1":
                tambah_barang()
            elif pilihan == "2":
                inventaris.tampilkan_semua_barang()
            elif pilihan == "3":
                cari_barang()
            elif pilihan == "4":
                update_barang()
            elif pilihan == "5":
                hapus_barang()
            elif pilihan == "6":
                print("Anda telah keluar dari Menu Admin.")
                break
            else:
                print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")
    else:
        print("Username atau password salah. Silakan coba lagi.")

# Fungsi untuk menambah barang oleh admin
def tambah_barang():
    id_barang = input("Masukkan ID Barang: ")
    nama_barang = input("Masukkan Nama Barang: ")

    while True:
        jumlah = input("Masukkan Jumlah: ")
        if not jumlah.isdigit():
            print("Jumlah barang harus berupa angka.")
        else:
            jumlah = int(jumlah)
            break

    kondisi = input("Masukkan Kondisi: ")
    lokasi = input("Masukkan Lokasi: ")
    nama_pemilik = input("Masukkan Nama Pemilik: ")
    
    while True:
        posisi = input("Masukkan Posisi untuk Menaruh Barang (awal/tengah/akhir): ")
        if posisi in ["awal", "tengah", "akhir"]:
            break
        else:
            print("--Posisi tidak valid. Pilihan yang valid adalah 'awal', 'tengah', atau 'akhir'.--")

    inventaris.tambah_barang(id_barang, nama_barang, jumlah, kondisi, lokasi, nama_pemilik, posisi)
    print("Barang berhasil ditambahkan.")

# Fungsi untuk mencari barang oleh admin
def cari_barang():
    id_barang = input("Masukkan ID Barang yang ingin dicari: ")
    inventaris.cari_barang(id_barang)

# Fungsi untuk memperbarui informasi barang oleh admin
def update_barang():
    id_barang = input("Masukkan ID Barang yang ingin diperbarui: ")
    field = input("Masukkan Field yang ingin diperbarui: ")
    value = input("Masukkan Nilai baru: ")
    inventaris.update_barang(id_barang, field, value)

# Fungsi untuk menghapus barang oleh admin
def hapus_barang():
    id_barang = input("Masukkan ID Barang yang ingin dihapus: ")
    inventaris.hapus_barang(id_barang)


'''=========================================================================================================='''
'''                                                  LOGIN CUSTOMER                                          '''
'''=========================================================================================================='''
# Fungsi untuk login customer
def customer_login():
    print("\n=== Login Customer ===")
    input_username = input("Username: ")
    input_password = input("Password: ")

    customer = customer_list.find_customer(input_username)
    if customer and customer.password == input_password:
        print("Login berhasil.")
        customer_menu(customer)
    else:
        print("Username atau password salah. Silakan coba lagi.")


'''=========================================================================================================='''
'''                                       REGISTRASI CUSTOMER                                                '''
'''=========================================================================================================='''
# Fungsi untuk registrasi customer
def customer_register():
    print("\n=== Registrasi Customer ===")
    new_username = input("Masukkan username baru: ")
    new_password = input("Masukkan password baru: ")

    existing_customer = customer_list.find_customer(new_username)
    if existing_customer:
        print("Username sudah digunakan. Silakan gunakan username lain.")
    else:
        customer_list.add_customer(new_username, new_password)
        print("Registrasi berhasil.")

        pilihan = input("Apakah Anda ingin login sekarang? (ya/tidak): ")
        if pilihan.lower() == "ya":
            customer_login()
        else:
            return

# Fungsi untuk meminjam barang oleh customer
def pinjam_barang(customer):
    id_barang = input("Masukkan ID Barang yang ingin dipinjam: ")
    barang = inventaris.cari_barang(id_barang)
    if barang:
        if barang.jumlah > 0:
            customer.nama = input("Masukkan Nama Anda: ")
            customer.alamat = input("Masukkan Alamat Anda: ")
            while True:
                nomor_hp = input("Masukkan Nomor HP Anda: ")
                if not nomor_hp.isdigit():
                    print("Nomor HP harus berupa angka. Silakan masukkan kembali.")
                else:
                    customer.nomor_hp = nomor_hp
                    break
            
            while True:
                jumlah_pinjam = input("Masukkan Jumlah Barang yang Ingin Dipinjam: ")
                if not jumlah_pinjam.isdigit():
                    print("Jumlah barang harus berupa angka. Silakan masukkan kembali.")
                else:
                    jumlah_pinjam = int(jumlah_pinjam)
                    if jumlah_pinjam > barang.jumlah:
                        print("Maaf, stok barang tidak mencukupi.")
                    else:
                        break

            customer.tambah_riwayat_pinjam(barang, jumlah_pinjam)
            barang.jumlah -= jumlah_pinjam
            print("Barang berhasil dipinjam.")
        else:
            print("Maaf, stok barang tidak mencukupi.")
    else:
        print("Barang tidak ditemukan.")
        

# Fungsi untuk melihat riwayat pinjaman oleh customer
def lihat_riwayat_pinjam(customer):
    if customer.riwayat_pinjam:
        print("Riwayat Pinjaman:")
        for riwayat in customer.riwayat_pinjam:
            barang, nama_peminjam, alamat_peminjam, nomor_hp_peminjam, jumlah_pinjam = riwayat
            print(f"ID Barang: {barang.id_barang}, Nama Barang: {barang.nama_barang}, Jumlah: {jumlah_pinjam}, Nama Peminjam: {nama_peminjam}, Alamat: {alamat_peminjam}, Nomor HP: {nomor_hp_peminjam}")
    else:
        print("Anda belum pernah meminjam barang.")

'''=========================================================================================================='''
'''                                               MENU CUSTOMER                                              '''
'''=========================================================================================================='''
# Fungsi untuk menampilkan menu customer
def customer_menu(customer):
    while True:
        print("\n=== Menu Customer ===")
        print("1. Lihat Barang Tersedia")
        print("2. Pinjam Barang")
        print("3. Lihat Riwayat Pinjaman")
        print("4. Keluar")

        pilihan = input("Masukkan pilihan (1/2/3/4): ")

        if pilihan == "1":
            inventaris.tampilkan_semua_barang()
        elif pilihan == "2":
            pinjam_barang(customer)
        elif pilihan == "3":
            lihat_riwayat_pinjam(customer)
        elif pilihan == "4":
            print("Anda telah keluar dari Menu Customer.")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")


'''=========================================================================================================='''
'''                                                    MAIN                                                  '''
'''=========================================================================================================='''
# Fungsi utama
def main():
    while True:
        print("\n=== Selamat datang di Sistem Peminjaman Barang ===")
        print("1. Admin")
        print("2. Customer")
        print("3. Keluar")

        pilihan_user = input("Silakan pilih peran Anda (1/2/3): ")

        if pilihan_user == "1":
            admin_menu()
        elif pilihan_user == "2":
            print("\n=== Sign In or Register Customer ===")
            print("1. Login")
            print("2. Registrasi")
            print("3. Keluar")

            pilihan = input("Silakan pilih opsi Anda (1/2/3): ")

            if pilihan == "1":
                customer_login()
            elif pilihan == "2":
                customer_register()
            elif pilihan == "3":
                print("Terima kasih telah menggunakan program ini.")
                break
            else:
                print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")
        elif pilihan_user == "3":
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")

# memanggil main
if __name__ == "__main__":
    main()
