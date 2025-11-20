import csv
import os
import pandas as pd
from tabulate import tabulate

# ------------------------ FUNGSI REGISTER ADMIN (INTERNAL) ------------------------
def regadmin():
    username = input("Masukkan username admin: ").strip() #strip buat ngehapus spasi berlebih
    password = input("Masukkan password admin: ").strip()

    if not username or not password:
        print("Username atau password tidak boleh kosong!")
        input("Tekan Enter untuk kembali...")
        return

    # Pastikan user.csv ada
    if not os.path.exists('user.csv'):
        with open('user.csv', 'w', newline='') as file:
            csv.writer(file).writerow(['username', 'password', 'role'])

    # Cek duplikat username
    with open('user.csv', 'r', newline='') as file: #newline supaya tidak ada bari kosonng
        reader = csv.reader(file) #reader datanya di jadiin satu baris tapi dipisah dengan koma
        next(reader, None)  # melewati header seperti : ['username', 'paswoard', 'role'] biar yg diproses itu data user bukan header
        for row in reader: #ngecek tiap user udah ada
            if row and row[0] == username: #buat data pertama username sudah ditersimpan
                print("Username admin sudah digunakan!")
                input("Tekan Enter untuk kembali...")
                return

    # Simpan sebagai admin
    with open('user.csv', 'a', newline='') as file:
        csv.writer(file).writerow([username, password, 'admin'])

    print("Admin berhasil didaftarkan!")
    input("Tekan Enter untuk kembali...")

# ------------------------ FUNGSI REGISTER USER ------------------------
def register():
    os.system('cls')
    print("============================[ REGISTER AKUN ]============================")
    
    while True:
        print("\n1. Daftar sebagai admin")
        print("2. Daftar sebagai user")
        print("0. Kembali ke menu utama")
        p = input("Pilih: ").strip() 

        if p == '1':
            regadmin() #manggil fungsi sbg admin
            return  # kembali ke menu utama
        elif p == '2':
            username = input("\nMasukkan username: ").strip().lower() #.lower biar semua huruf jd kecil
            password = input("Masukkan password: ").strip().lower()

            if not username or not password:
                print("\nUsername dan password tidak boleh kosong!")
                input("Tekan Enter untuk ulangi...")
                continue #klo true bisa lanjut ke kondisi selanjutnya

            # Pastikan file user.csv ada
            if not os.path.exists('user.csv'):
                with open('user.csv', 'w', newline='') as file:
                    csv.writer(file).writerow(['username', 'password', 'role'])

            # Cek apakah username sudah ada
            with open('user.csv', 'r', newline='') as file:
                reader = csv.reader(file)
                next(reader, None)  # Lewati header
                for row in reader: #dibaca baris satu persatu
                    if row and row[0] == username:
                        print("\nUsername sudah digunakan!")
                        input("Tekan Enter untuk kembali...")
                        return

            # Simpan user baru
            with open('user.csv', 'a', newline='') as file: #pake append 'a' biar baris baru ditambahin di akhr file
                csv.writer(file).writerow([username, password, 'user']) #pasworadnya disimpan plain text artinya disimpan apa adany tanpa dan bisa dibaca sp aja yg buka file csvnya

            print(f"\nRegistrasi berhasil! Selamat datang, {username}!")
            input("Tekan Enter untuk kembali ke menu utama...")
            return

        elif p == '0': #jika ngetik 0 maka balik ke menu utama / keluar dr register
            return  # kembali ke menu utama
        else:
            print("\nPilihan tidak valid! Masukkan 1, 2, atau 0.")
            input("Tekan Enter untuk ulangi...")

# ------------------------ FUNGSI LOGIN ------------------------
def login():
    os.system('cls')
    print("============================[ LOGIN ]============================")
    username = input("Masukkan username: ").strip().lower()
    password = input("Masukkan password: ").strip().lower()

    if not os.path.exists('user.csv'): #cek apakah file csv uda ada apa blm
        print("\nBelum ada akun! Silakan daftar terlebih dahulu.")
        input("Tekan Enter untuk kembali...")
        return

    with open('user.csv', 'r', newline='') as file: #mbaca file csv
        reader = csv.DictReader(file) #membaca csv trus ngubah tiap baris jd dictionary
        for row in reader:
            if row['username'] == username and row['password'] == password:
                role = row['role']
                print(f"\nLogin berhasil! Selamat datang, {username} ({role})")
                input("Tekan Enter untuk melanjutkan...")
                if role == 'admin':
                    menu_admin(username)
                else: 
                    menu_user(username)
                return

    print("\nUsername atau password salah!")
    input("Tekan Enter untuk mencoba lagi...")

# ------------------------ MENU ADMIN ------------------------
def menu_admin(username):
    while True:
        os.system('cls')
        print(f"=== MENU ADMIN ===\nHalo Admin {username}")
        print("1. Manajemen Pengguna")
        print("2. Manajemen Produk")
        print("3. Manajemen Transaksi")
        print("4. Laporan")
        print("5. Logout")

        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            manajemen_pengguna()
        elif pilihan == '2':
            manajemen_produk()
        elif pilihan == '3':
            manajemen_transaksi()
        elif pilihan == '4':
            laporan()
        elif pilihan == '5':
            return
        else:
            print("Pilihan tidak valid!")
            input("Tekan Enter...")

# ------------------------ BERANDA ADMIN --  ADMIN ------------------------
# def beranda_admin():
#     os.system('cls')
#     print("===== BERANDA ADMIN =====")

#     if not os.path.exists('product.csv'):
#         print("Belum ada data produk.")
#         input("\nTekan Enter untuk kembali...")
#         return

#     df = pd.read_csv('product.csv') #utk membaca file csv
#     total_produk = len(df) #menghitung jmlh baris pada dataframe
#     total_harga = df['harga'].sum() #.sum itu buat ngitung jumlah semua harga
#     total_terjual = df['terjual'].sum()  # .sum buat ngitung semua baris di kolon terjual

#     print(f"Jumlah Produk: {total_produk}")
#     print(f"Total Harga Semua Produk: Rp {total_harga:,}")
#     print(f"Total Produk Terjual: {total_terjual}")

#     input("\nTekan Enter untuk kembali...")



# ------------------------ MANAJEMEN PENGGUNA -- ADMIN------------------------
def manajemen_pengguna():
    os.system('cls')
    print("===== DAFTAR SEMUA USER =====")

    if not os.path.exists('user.csv'):
        print("Belum ada pengguna.")
        input("\nTekan Enter...")
        return
    
    while True: 
        os.system('cls')
        print(f"=== MANAJEMEN Pengguna ===")
        print("1. Lihat Pengguna")
        print("2. Delete Pengguna")
        print("3. Metode Transaksi")
        print("4. logout")

        p = input("Pilih menu: ")
        if p == '1':
            lihat_pengguna()
        elif p == '2':   
            hapus_pengguna()
        elif p == '3':   
            # metodePembayaran()
            return
        elif p == '4':   
            return main_menu()
        else:
            print("Pilihan tidak valid!")
            input("Enter...")


    # ------------------------ HAPUS DATA -- ADMIN -- MANAJEMEN PRODUK -----------------------
def hapus_pengguna():
    os.system('cls')
    file_user = 'user.csv'
    if not os.path.exists(file_user):
        print("Belum ada produk.")
        input("\nTekan Enter...")
        return

    df = pd.read_csv(file_user)
    print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))

    try:
        user = input("\nUsername pengguna yang ingin dihapus : ")
    except ValueError:
        print("user tidak boleh kosong")
        input("Enter...")
        return

    if user not in df['username'].values:
        print("ID tidak ditemukan!")
        input("Enter...")
        return

    df = df[df['username'] != user] 
    df.to_csv(file_user, index=False) #menyimpan perubahan ke file csv tanpa menyertakan index

    print("Produk berhasil dihapus!")
    input("\nTekan Enter...")
    return manajemen_pengguna() 

def lihat_pengguna():
    os.system('cls')

    while True:
        file_product = 'user.csv'
        namaColumn = 'user', 'password', 'role'
        if not os.path.exists(file_product):
            print("Belum ada produk.")
            df = pd.DataFrame(columns=namaColumn) #buat buka dataframe kolomnya dr variabl kolum
            df.to_csv(file_product)
            print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))
            input("Enter untuk kembali...")
            return 

        
        else:
            df = pd.read_csv(file_product)
            # df = pd.DataFrame(columns=['id', 'NamaProduk', 'Kategori', 'Harga', 'Stok', 'Subsidi', 'Terjual'])
            print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))
            input("Enter untuk kembali...")
            return


# ------------------------ MANAJEMEN PRODUK -- ADMIN ------------------------
def manajemen_produk():
    while True:
        os.system('cls')
        print("===== MANAJEMEN PRODUK =====")
        print("1. Lihat Semua Produk")
        print("2. Tambah Produk")
        print("3. Ubah Produk")
        print("4. Hapus Produk")
        print("5. Kembali")

        p = input("Pilih: ")

        if p == '1':
            lihat_produk()
        elif p == '2':
            tambah_produk()
        elif p == '3':
            ubah_produk()
        elif p == '4':
            hapus_produk()
        elif p == '5':
            return
        else:
            print("Pilihan tidak valid!")
            input("Enter...")

# ------------------------ LIHAT PRODUK -- OPERATOR DAN ADMIN -- MANAJEMEN PRODUK ------------------------
def lihat_produk():
    os.system('cls')

    while True:
        file_product = 'product.csv'
        namaColumn = 'id', 'NamaProduk', 'Kategori', 'Harga', 'Stok', 'Subsidi', 'Terjual'
        if not os.path.exists(file_product):
            print("Belum ada produk.")
            df = pd.DataFrame(columns=namaColumn) #buat buka dataframe kolomnya dr variabl kolum
            df.to_csv(file_product)
            print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))
            input("Enter untuk kembali...")
            return

        
        else:
            df = pd.read_csv(file_product)
            # df = pd.DataFrame(columns=['id', 'NamaProduk', 'Kategori', 'Harga', 'Stok', 'Subsidi', 'Terjual'])
            print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))
            input("Enter untuk kembali...")
            return
# ------------------------ TAMBAH PRODUK -- ADMIN -- MANAJEMEN PRODUK -----------------------

def tambah_produk():
    os.system('cls')
    print("===== TAMBAH PRODUK =====")
    file_product = 'product.csv'
    if not os.path.exists(file_product):
        # Buat file dengan header
        with open(file_product, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['id', 'NamaProduk', 'Kategori', 'Harga', 'Stok', 'Subsidi', 'Terjual'])
    # baca file
    df = pd.read_csv(file_product)
# tentukan id baru
    id_new = df['id'].max() + 1 if not df.empty else 1 #klo df ga kosong id baru itu id max + 1 klo kosong id nya 1
# input data baru
    nama = input("Nama produk: ").strip().title()
    kategori = input("Kategori: ").strip().title()
    try:
        harga = int(input("Harga: "))
        stok = int(input("Stok: "))
        subsidi = input("Subsidi (ya/tidak): ").strip().title() #strip buat ngilangin spasi title buat bikin huruf awal jd kapital

        with open('product.csv', 'a', newline='') as f:
            csv.writer(f).writerow([id_new, nama, kategori, harga, stok, subsidi])

        print("Produk berhasil ditambahkan!")
        input("\nTekan Enter...")
    except ValueError:
        print("Harga dan stok harus berupa angka!")
        input("\n Tekan Enter untuk kembali...")
        return 

# ------------------------ UBAH DATA -- ADMIN -- MANAJEMEN PRODUK -----------------------

def ubah_produk():
    os.system('cls')
    print("===== UBAH PRODUK =====")
    file_product = 'product.csv'

    if not os.path.exists(file_product):
        print("Belum ada produk.")
        input("\nTekan Enter...")
        return

    df = pd.read_csv(file_product)
    print("Daftar Produk:")
    print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))

    try:
        df = pd.read_csv(file_product)
        id_p = int(input("\nMasukkan ID produk yang ingin diubah: "))
    except ValueError:
        print("ID harus berupa angka!")
        input("Enter...")
        return

    if id_p not in df['id'].values: #ngecek id_p itu ada di variabel df di kolom id
        print("ID tidak ditemukan!")
        input("Enter...")
        return
    
    # ambil data based id
    data_produk = df[df['id'] == id_p] #
    # ambil nilai idx 0 dri data_produk
    data = data_produk.iloc[0]

    
    # menampilkan data produk yg akan diubah
    data = data_produk[data_produk['id'] == id_p]

    if not data_produk.empty:
        os.system('cls')
        print("Data produk yang akan diubah:")
        print(tabulate(data, headers='keys', tablefmt='fancy_grid', showindex=False))

        
    try:
        nama = input("/nNama baru: ").strip().title()
        kategori = input("Kategori baru: ").strip().title()
        harga = int(input("Harga: "))
        stok = int(input("Stok: "))
        subsidi = input("Subsidi (ya/tidak): ").strip().title()

        if nama :
            df.loc[df['id'] == id_p, 'NamaProduk'] = nama
        if kategori :   
            df.loc[df['id'] == id_p, 'Kategori'] = kategori                 
        if harga :
            df.loc[df['id'] == id_p, 'Harga'] = harga
        if stok :
            df.loc[df['id'] == id_p, 'Stok'] = stok

        # with open('product.csv', 'a', newline='') as f:
        #     csv.writer(f).writerow([id_p, nama, kategori, harga, stok, subsidi]).
        print("Produk berhasil ditambahkan!")
        input("\nTekan Enter...")
    except ValueError:
        print("Harga dan stok harus berupa angka!")
        input("\n Tekan Enter...")
        return
    


    df.to_csv(file_product, index=False)
    print("Produk berhasil diubah!")
    input("\nTekan Enter...")
    return

# ------------------------ HAPUS DATA -- ADMIN -- MANAJEMEN PRODUK -----------------------
def hapus_produk():
    os.system('cls')
    if not os.path.exists('product.csv'):
        print("Belum ada produk.")
        input("\nTekan Enter...")
        return

    df = pd.read_csv('product.csv')
    print(tabulate(df, headers='keys', tablefmt='grid'))

    try:
        id_p = int(input("\nID produk yang ingin dihapus: "))
    except ValueError:
        print("ID harus berupa angka!")
        input("Enter...")
        return

    if id_p not in df['id'].values:
        print("ID tidak ditemukan!")
        input("Enter...")
        return

    df = df[df['id'] != id_p]
    df.to_csv('product.csv', index=False)

    print("Produk berhasil dihapus!")
    input("\nTekan Enter...")
    return manajemen_produk()





# ------------------------ MANAJEMEN PRODUK -- ADMIN ------------------------
# ISI

# ------------------------ LAPORAN -- ADMIN ------------------------
def laporan():
    os.system('cls')
    print("===== LAPORAN TRANSAKSI =====")

    if not os.path.exists('transaksi.csv'):
        print("Belum ada transaksi!")
        input("\nTekan Enter...")
        return

    df = pd.read_csv('transaksi.csv')

    if df.empty:
        print("Belum ada transaksi!")
        input("\nTekan Enter...")
        return

    df['tanggal'] = pd.to_datetime(df['tanggal'])
    total_pendapatan = df['total_harga'].sum()

    print(f"Total Pendapatan: Rp {total_pendapatan:,}")
    print("\nTransaksi Harian:")
    harian = df.groupby(df['tanggal'].dt.date)['total_harga'].sum().reset_index()
    print(tabulate(harian, headers="keys", tablefmt="grid"))

    input("\nTekan Enter...")

# ------------------------ MANAJEMEN TRANSAKSI ------------------------
def manajemen_transaksi():
    os.system('cls')
    print("===== SEMUA TRANSAKSI =====")

    if not os.path.exists('transaksi.csv'):
        print("Belum ada transaksi.")
        input("\nTekan Enter...")
        return

    df = pd.read_csv('transaksi.csv')
    print(tabulate(df, headers='keys', tablefmt='grid'))
    input("\nTekan Enter...")
    


# ------------------------ MENU USER ------------------------
def menu_user(username):
    while True:
        os.system('cls')
        print(f"=== MENU USER ===\nHalo {username}")
        print("1. Lihat Produk")
        print("2. Searching")
        print("3. Keranjang Belanja")
        print("4. Pembayaran")
        print("5. logout")

        p = input("Pilih menu: ")

        if p == '1':
            lihat_produk()
        elif p == '2':   
            cariProduct()
        elif p == '3':   
            # keranjang()
            return
        
        elif p == '4':   
            # metodePembayaran()
            return
        elif p == '5':   
            return main_menu()
        
        else:
            print("Pilihan tidak valid!")
            input("Enter...")

    
def cariProduct():
    os.system('cls')
    print("===== CARI Produk =====")
    while True:
        data_product = 'product.csv'
        namaColumn = 'id', 'NamaProduk', 'Kategori', 'Harga', 'Stok', 'Subsidi', 'Terjual'
        if not os.path.exists(data_product):
            print("Belum ada pengguna.")
            df = pd.DataFrame(columns=namaColumn)
            df.to_csv(data_product)
            print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))
            input("\nTekan Enter...")
            return
        else:
            df = pd.read_csv(data_product)
            # df = pd.DataFrame(columns=['id', 'NamaProduk', 'Kategori', 'Harga', 'Stok', 'Subsidi', 'Terjual'])
            print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))

        try:
            id = int(input("\n Cari product berdasarkan id: "))
        except:
            print("Masukan id dengan angka")
            input("Tekan Enter untuk kembali...")
            return
        
        # mencari value var id dari data =_product
        filter =  df[df['id'] == id]
        
        if not filter.empty:
            os.system('cls')
            print("Data ditemukan \n")
            print(tabulate(filter, headers='keys', tablefmt='fancy_grid', showindex=False))
            input("Tekan Enter untuk kembaLi...")
            return

        else:
            print("\nData tidak ditemukan")
            input("Tekan Enter untuk kembaLi...")
            return

# def keranjang():


# def metodePembayaran():




#  SAMA DENGAN YG ATAS
# def hapus_produk():
#     os.system('cls')
#     if not os.path.exists('product.csv'):
#         print("Belum ada produk.")
#         input("\nTekan Enter...")
#         return

#     df = pd.read_csv('product.csv')
#     print(tabulate(df, headers='keys', tablefmt='grid'))

#     try:
#         id_p = int(input("\nID produk yang ingin dihapus: "))
#     except ValueError:
#         print("ID harus berupa angka!")
#         input("Enter...")
#         return

#     if id_p not in df['id'].values:
#         print("ID tidak ditemukan!")
#         input("Enter...")
#         return

#     df = df[df['id'] != id_p]
#     df.to_csv('product.csv', index=False)

#     print("Produk berhasil dihapus!")
#     input("\nTekan Enter...")




# ------------------------ MENU UTAMA ------------------------
def main_menu():
    while True:
        os.system('cls')
        print("===================================================================")
        print("    MARKETPLACE BIBIT & PUPUK    ")
        print("===================================================================")
        print("1. Register (Daftar Akun Baru)")
        print("2. Login")
        print("3. Keluar")
        print("===================================================================")
        pilihan = input("Pilih menu (1/2/3): ").strip()

        if pilihan == '1':
            register()
        elif pilihan == '2':
            login()
        elif pilihan == '3':
            print("Terima kasih telah menggunakan sistem marketplace ini!")
            exit()
        else:
            input("Pilihan tidak valid! Tekan Enter untuk mencoba lagi...")

# ------------------------ JALANKAN PROGRAM ------------------------

main_menu()