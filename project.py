import csv
import os
import pandas as pd
from tabulate import tabulate
from datetime import datetime

# ------------------------ MENU UTAMA ------------------------

def main_menu():
    while True:
        os.system('cls')
        teks = """
    
        ██████╗░██╗░░░██╗██████╗░██╗░░░██╗░██████╗░██╗░░░██╗███████╗███████╗███╗░░██╗░██████╗
        ██╔══██╗██║░░░██║██╔══██╗██║░░░██║██╔═══██╗██║░░░██║██╔════╝██╔════╝████╗░██║██╔════╝
        ██████╔╝██║░░░██║██████╔╝██║░░░██║██║██╗██║██║░░░██║█████╗░░█████╗░░██╔██╗██║╚█████╗░
        ██╔═══╝░██║░░░██║██╔═══╝░██║░░░██║╚██████╔╝██║░░░██║██╔══╝░░██╔══╝░░██║╚████║░╚═══██╗
        ██║░░░░░╚██████╔╝██║░░░░░╚██████╔╝░╚═██╔═╝░╚██████╔╝███████╗███████╗██║░╚███║██████╔╝
        ╚═╝░░░░░░╚═════╝░╚═╝░░░░░░╚═════╝░░░░╚═╝░░░░╚═════╝░╚══════╝╚══════╝╚═╝░░╚══╝╚═════╝░
        """
        print(teks)

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
            os.system('cls')
            print("===============================================================")
            print("===*                                                       *===")
            print("=== Terima kasih telah menggunakan sistem marketplace ini! ====")
            print("===*                                                       *===")
            print("===============================================================")
            exit()
        else:
            input("Pilihan tidak valid! Tekan Enter untuk mencoba lagi...")

# ------------------------ FUNGSI REGISTER USER ------------------------
def register():
    os.system('cls')
    print("============================[ REGISTER AKUN ]============================")
    
    while True:
        print("\n1. Daftar sebagai user")
        print("0. Kembali ke menu utama")
        p = input("Pilih: ").strip() 

        if p == '1':
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
                        break

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
                

    print("\nUsername atau password salah!")
    input("Tekan Enter untuk mencoba lagi...")



# ------------------------ MENU ADMIN ------------------------
def menu_admin(username):
    while True:
        os.system('cls')
        print(f"=== MENU ADMIN ===\nHalo Admin {username}")
        print("1. Manajemen Pengguna")
        print("2. Manajemen Produk")
        print("3. Laporan")
        print("4. Logout")

        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            manajemen_pengguna()
        elif pilihan == '2':
            manajemen_produk()
        elif pilihan == '3':
            laporanadmin()
        elif pilihan == '4':
            return main_menu()
        else:
            print("Pilihan tidak valid!")
            input("Tekan Enter...")

# ------------------------ MANAJEMEN PENGGUNA -- ADMIN------------------------
def manajemen_pengguna():
    while True: 
        os.system('cls')
        print("===== DAFTAR SEMUA USER =====")

        if not os.path.exists('user.csv'):
            print("Belum ada pengguna.")
            input("\nTekan Enter...")
            break
        
        os.system('cls')
        print(f"=== MANAJEMEN Pengguna ===")
        print("1. Lihat Pengguna")
        print("2. Delete Pengguna")
        print("3. Keluar")

        p = input("Pilih menu: ")
        if p == '1':
            lihat_pengguna()
        elif p == '2':   
            hapus_pengguna()
        elif p == '3':   
            break
        else:
            print("Pilihan tidak valid!")
            input("Enter...")



    # ------------------------ HAPUS DATA -- ADMIN -- MANAJEMEN PRODUK -----------------------
def hapus_pengguna():
    while True:
        os.system('cls')
        file_user = 'user.csv'
        if not os.path.exists(file_user):
            print("Belum ada data.")
            input("\nTekan Enter...")
            break

        df = pd.read_csv(file_user)
        print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))

        try:
            user = input("\nUsername pengguna yang ingin dihapus : ")
        except ValueError:
            print("user tidak boleh kosong")
            input("Enter...")
            break


        if user not in df['username'].values:
            print("ID tidak ditemukan!")
            input("Enter...")
            break

        df = df[df['username'] != user] #ngefilter apa di variabel df kolom username ini ada user apa ngga, klo ada dihapus
        df.to_csv(file_user, index=False) #menyimpan perubahan ke file csv tanpa menyertakan index

        print("Data berhasil dihapus!")
        input("\nTekan Enter...")
        break

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
            break

        
        else:
            df = pd.read_csv(file_product)
            # df = pd.DataFrame(columns=['id', 'NamaProduk', 'Kategori', 'Harga', 'Stok', 'Subsidi', 'Terjual'])
            print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))
            input("Enter untuk kembali...")
            break


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
            break
        else:
            print("Pilihan tidak valid!")
            input("Enter...")

# ------------------------ LIHAT PRODUK -- OPERATOR DAN ADMIN -- MANAJEMEN PRODUK ------------------------
def lihat_produk():
    os.system('cls')

    while True:
        file_product = 'product.csv'
        namaColumn = 'id', 'NamaProduk', 'Kategori', 'Harga', 'Stok', 'Subsidi'
        if not os.path.exists(file_product):
            print("Belum ada produk.")
            df = pd.DataFrame(columns=namaColumn) #buat buka dataframe kolomnya dr variabl kolum
            df = df.reset_index(drop=True) #untuk mengurutkan indeks 
            df.to_csv(file_product)
            print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))
            input("Enter untuk kembali...")
            break

        
        else:
            df = pd.read_csv(file_product)
            # df = pd.DataFrame(columns=['id', 'NamaProduk', 'Kategori', 'Harga', 'Stok', 'Subsidi'])
            print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))
            input("Enter untuk kembali...")
            break
# ------------------------ TAMBAH PRODUK -- ADMIN -- MANAJEMEN PRODUK -----------------------

def tambah_produk():
    while True:
        os.system('cls')
        print("===== TAMBAH PRODUK =====")
        file_product = 'product.csv'
        if not os.path.exists(file_product):
            # Buat file dengan header
            with open(file_product, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['id', 'NamaProduk', 'Kategori', 'Harga', 'Stok', 'Subsidi'])
            
        df = pd.read_csv(file_product)
            
        id_new = 1
        try:
            with open(file_product, 'r', newline='') as f:
                reader = csv.reader(f)
                f = list(reader)
            if len(f) > 1: #ngecek panjang item di variabel f
                    id_terakhir = int(f[-1][0]) #-1 baris paling akhir tapi ngambil dr kolom ke 0 atau pertama
                    id_new = id_terakhir + 1 #ditambah di indeks akhir
            else:
                id_new = 1 

        except ValueError:
            print("File kosong, memulai dari ID 1.")
                
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
            break
        except ValueError:
            print("Harga dan stok harus berupa angka!")
            input("\n Tekan Enter untuk kembali...")
            break

# ------------------------ UBAH DATA -- ADMIN -- MANAJEMEN PRODUK -----------------------

def ubah_produk():
    while True:
        os.system('cls')
        print("===== UBAH PRODUK =====")
        file_product = 'product.csv'

        if not os.path.exists(file_product):
            with open('product.csv', 'a', newline='') as f:
                csv.writer(f).writerow([id_p, nama, kategori, harga, stok, subsidi])
            print("Belum ada produk.")
            input("\nTekan Enter...")
            break

        df = pd.read_csv(file_product)
        print("Daftar Produk:") 
        print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))

        try:
            df = pd.read_csv(file_product)
            id_p = int(input("\nMasukkan ID produk yang ingin diubah: "))
        except ValueError:
            print("ID harus berupa angka!")
            input("Enter...")
            break

        if id_p not in df['id'].values: #ngecek id_p itu ada di variabel df di kolom id
            print("ID tidak ditemukan!")
            input("Enter...")
            break

        # ambil data based id
        data_produk = df[df['id'] == id_p] #klo sama dengan df nanti bakal masuk ke variabel dataproduk 
        # ambil nilai idx 0 dri data_produk
        data = data_produk.iloc[0] #ini buat ngambil satu barisnya 


        # menampilkan data produk yg akan diubah
        data = data_produk[data_produk['id'] == id_p]

        if not data_produk.empty:
            os.system('cls')
            print("Data produk yang akan diubah:")
            print(tabulate(data, headers='keys', tablefmt='fancy_grid', showindex=False))


        try:
            nama = input("\nNama baru: ").strip().title()
            kategori = input("Kategori baru: ").strip().title()
            harga = int(input("Harga: "))
            stok = int(input("Stok: "))
            subsidi = input("Subsidi (ya/tidak): ").strip().title()

            if nama :
                df.loc[df['id'] == id_p, 'NamaProduk'] = nama #buat gnti produk barunya .loc itu buat ngambil lbh spesifik
            if kategori :   
                df.loc[df['id'] == id_p, 'Kategori'] = kategori                 
            if harga :
                df.loc[df['id'] == id_p, 'Harga'] = harga
            if stok :
                df.loc[df['id'] == id_p, 'Stok'] = stok
        except ValueError:
            print("Harga dan stok harus berupa angka!")
            input("\n Tekan Enter...")
            break


        df.to_csv(file_product, index=False)
        print("Produk berhasil diubah!")
        input("\nTekan Enter...")
        break

# ------------------------ HAPUS DATA -- ADMIN -- MANAJEMEN PRODUK -----------------------
def hapus_produk():
    while True:
        os.system('cls')
        file_produk = 'product.csv'
        if not os.path.exists(file_produk):
            print("Belum ada produk.")
            input("\nTekan Enter...")
            break

        df = pd.read_csv(file_produk)
        print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))
        
        try:
            id_p = int(input("\nID produk yang ingin dihapus: "))
        except ValueError:
            print("ID harus berupa angka!")
            input("Enter...")
            break

        if id_p not in df['id'].values:
            print("ID tidak ditemukan!")
            input("Enter...")
            break

        df = df[df['id'] != id_p]
        df = df.reset_index(drop=True)
        df.to_csv(file_produk, index=False)

        print("Produk berhasil dihapus!")
        input("\nTekan Enter...")
        break


# ------------------------ LAPORAN -- ADMIN ------------------------
def laporanadmin():
        while True:
            os.system('cls')
            print("===== LAPORAN TRANSAKSI =====")

            if not os.path.exists('riwayat.csv'):
                print("Belum ada transaksi!")
                input("\nTekan Enter...")
                break

            df = pd.read_csv('riwayat.csv')

            if df.empty:
                print("Belum ada transaksi!")
                input("\nTekan Enter...")
                break
            df['TanggalBeli'] = pd.to_datetime(df['TanggalBeli'], format= '%d-%m-%Y')
            total_pendapatan = df['HargaTotal'].sum()
            df['TanggalBeli'] = pd.to_datetime(df['TanggalBeli']).dt.strftime('%d-%m-%Y')

            print("\nTransaksi Harian:".center(50))
            print(tabulate(df, headers="keys", tablefmt="fancy_grid",showindex=False))
            print(f"Total Pendapatan: Rp {total_pendapatan:,}")

            input("\nTekan Enter...")
            return
#BELUM SELESAI

# ------------------------ MENU USER ------------------------
def menu_user(username):
    while True:
        os.system('cls')
        print(f"=== MENU USER ===\nHalo {username}")
        print("1. Lihat Produk")
        print("2. Searching") #berdasarkan id
        print("3. Tambah produk ke keranjang")
        print("4. Hapus produk dari keranjang ")
        print("5. Metode Pembayaran")
        print("6. Riwayat")
        print("7. logout")

        p = input("Pilih menu: ")

        if p == '1':
            lihat_produk()
        elif p == '2':   
            cariProduct()
        elif p == '3':   
            tambah_ke_keranjang(username)
        elif p == '4':   
            hapus_dari_keranjang(username)
        elif p == '5':   
            metode_pembayaran(username)
        elif p == '6':   
            riwayat(username)
        elif p == '7':   
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
            df = pd.DataFrame(columns=namaColumn) #membuat formulir kosong dengan judul kolom yang sudah ditentukan, siap diisi data nanti. 
            df.to_csv(data_product)
            print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))
            input("\nTekan Enter...")
            break
        else:
            df = pd.read_csv(data_product)
            # df = pd.DataFrame(columns=['id', 'NamaProduk', 'Kategori', 'Harga', 'Stok', 'Subsidi', 'Terjual'])
            print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))

        try:
            id = int(input("\n Cari product berdasarkan id: "))
        except:
            print("Masukan id dengan angka")
            input("Tekan Enter untuk kembali...")
            break
        
        # mencari value var id dari data =_product
        filter =  df[df['id'] == id]
        
        if not filter.empty:
            os.system('cls')
            print("Data ditemukan \n")
            print(tabulate(filter, headers='keys', tablefmt='fancy_grid', showindex=False))
            input("Tekan Enter untuk kembaLi...")
            break

        else:
            print("\nData tidak ditemukan")
            input("Tekan Enter untuk kembaLi...")
            break

def tambah_ke_keranjang(username):
    os.system('cls')
    while True:
        print("===== TAMBAH KE KERANJANG =====")
        
        # Cek apakah produk tersedia
        if not os.path.exists('product.csv'):
            print("Belum ada produk! Silakan tambahkan produk terlebih dahulu.")
            input("Tekan Enter untuk kembali...")
            break

        # Tampilkan daftar produk
        df_produk = pd.read_csv('product.csv')
        print(tabulate(df_produk[['id', 'NamaProduk', 'Harga', 'Stok']], headers='keys', tablefmt='fancy_grid', showindex=False))

        try:
            id_produk = int(input("\nMasukkan ID produk yang ingin ditambahkan: "))
        except ValueError:
            print("ID harus berupa angka!")
            input("Tekan Enter...")
            break

        # Cek apakah ID ada
        if id_produk not in df_produk['id'].values:
            print("ID produk tidak ditemukan!")
            input("Tekan Enter...")
            os.system('cls')
            break

        produk = df_produk[df_produk['id'] == id_produk].iloc[0]
        if produk['Stok'] <= 0:
            print("Stok produk ini habis!")
            input("Tekan Enter...")
            return tambah_ke_keranjang(username)
            

        # Input jumlah
        try:
            jumlah = int(input(f"Jumlah (Stok tersedia: {produk['Stok']}): "))
            if jumlah <= 0:
                print("Jumlah minimal 1!")
                input("Tekan Enter...")
                break
            if jumlah > produk['Stok']:
                print("Jumlah melebihi stok tersedia!")
                input("Tekan Enter...")
                break
        except ValueError:
            print("Jumlah harus berupa angka!")
            input("Tekan Enter...")
            break
        
        tanggal = input("Masukkan tanggal (DD-MM-YYYY) atau Enter untuk hari ini: ").strip()
        if not tanggal:
            tanggal = datetime.now().strftime("%d-%m-%Y") #buat formatnya

        harga = df_produk.loc[df_produk['id'] == id_produk ,'Harga'].values[0] #gambil dr ID yg uda dipilih 
        hargaTotal = harga * jumlah

        # Pastikan file keranjang ada
        keranjang_file = 'keranjang.csv'
        if not os.path.exists(keranjang_file):
            with open(keranjang_file, 'w', newline='') as f:
                csv.writer(f).writerow(['username','id', 'NamaProduk', 'Harga', 'Jumlah', 'hargaTotal', 'tanggal'])

        # Baca keranjang
        df_keranjang = pd.read_csv(keranjang_file)
        
        if not os.path.exists(keranjang_file):
            print("Transaksi belum ada")
            input("Enter untuk lanjut...")
            break

        # # Tambah baru
        with open(keranjang_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([username, id_produk, produk['NamaProduk'], int(produk['Harga']), jumlah, hargaTotal, tanggal])
        print(f"Produk '{produk['NamaProduk']}' berhasil ditambahkan ke keranjang!")

        pilih = input('Mau tambah produk ke keranjang lagi? y/n: ').lower()

        if pilih == 'n':
            input("Enter untuk ke menu user...")
            return menu_user(username)
        elif pilih == 'y':
            return tambah_ke_keranjang(username)
        elif pilih != 'y' or pilih != 'n':
            print("Pilih menu Metode Bayar (5) untuk melakukan pembayaran.")
        input("Tekan Enter untuk kembali...")
        return

# ------------------------ HAPUS BARANG DARI KERANJANG ------------------------
def hapus_dari_keranjang(username):
    while True:
        os.system('cls')
        print("===== HAPUS DARI KERANJANG =====")

        keranjang_file = 'keranjang.csv'
        if not os.path.exists(keranjang_file):
            print("Keranjang Anda kosong.")
            input("Tekan Enter...")
            break

        df = pd.read_csv(keranjang_file)
        user_cart = df[df['username'] == username]

        if user_cart.empty: #jika file nya gaada isi 
            print("Keranjang Anda kosong.")
            input("Tekan Enter...")
            break

        print("Isi Keranjang Anda:")
        print(tabulate(user_cart[['NamaProduk', 'Jumlah','hargaTotal' ]], headers='keys', tablefmt='fancy_grid', showindex=False))

        try:
            nama_hapus = input("\nMasukkan Nama produk yang ingin dihapus: ").title()
        except ValueError:
            print("ID harus berupa angka!")
            input("Tekan Enter...")
            break

        if nama_hapus not in user_cart['NamaProduk'].values:
            print("Produk tidak ditemukan di keranjang Anda!")
            input("Tekan Enter...")
            break

        # Hapus baris yang cocok
        df = df.astype(str) #cari perbedaan astype dan dstype #buat ngubah SEMUA data di DataFrame menjadi teks (string). 
        hasil = df[
            df['NamaProduk'].str.contains(nama_hapus, case=False)] #.str.contains = untuk memeriksa apakah ada kata yang mirip 
# tampilkan hasil pencarian
        if not hasil.empty:
            os.system('cls')
            print(tabulate(hasil[['NamaProduk', 'Jumlah','hargaTotal']], headers='keys', tablefmt='fancy_grid', showindex=False))
        try:
            pilih = input("\n Yakin ingin mengahapus? y/n: ").lower()
            if pilih == 'y':
                hasil = hasil[hasil['NamaProduk'].astype(str) != nama_hapus] # klo nama produk ada di kolom namaProduk dalam variabel hasil nanti bakal dihapus
                hasil.reset_index(drop=True, inplace=True)  #data lama lngsung keapus, lngsng disimpan tanpa variabel 
                hasil.to_csv(keranjang_file, index=False) #save 
                print("Produk berhasil dihapus!")
                input("Enter untuk kembali...")
                return
            

            elif pilih == 'n':
                print('Produk batal dihapus')
                return
            else:
                print("Masukkan huruf yang sesuai dengan pilihan yang ada")
                return
        except ValueError:
            print("ERROR DI BAGIAN HAPUS DATA")
        
        print("Produk berhasil dihapus dari keranjang!")
        break 
        # input("Tekan Enter...")
#-----------------------------METODE PEMBAYARAN---------------
#def metodePembayaran():
def metode_pembayaran(username):
    os.system('cls')
    
    while True:
        print("===== METODE PEMBAYARAN =====")
        print("\n1. Transfer \n2. Di tempat \n0.Kembali")
        pilih = input("\nPilih menu: ")

        if pilih == '1':
            pembayaran(username, pilih) 
        elif pilih == '2':
            pembayaran(username, pilih)
        elif pilih == '0':
            return
        else:
            print("Pilih opsi yang ada di menu")
            input("Tekan Enter untuk kembali")
            return

def pembayaran(username, pilih):
    os.system('cls')
    print("===== PEMBAYARAN VIA TRANSFER =====")

    keranjang_file = 'keranjang.csv'
    produk_file = 'product.csv'
    transaksi_file = 'transaksi.csv'
    riwayat_file = 'riwayat.csv'

    # Cek keranjang
    if not os.path.exists(keranjang_file):
        print("Keranjang masih kosong.")
        input("Tekan Enter...")
        return

    df_keranjang = pd.read_csv(keranjang_file)

    # filter keranjang user
    df_user = df_keranjang[df_keranjang['username'] == username].copy() #.copy ini buat ngecopy tnpa merusak df krnjangnya

    if df_user.empty:
        print("Keranjang Anda kosong.")
        input("Tekan Enter...")
        return

    # reset index supaya ada kolom index asli
    df_user = df_user.reset_index()          # kolom "index" ini adalah index asli di df_keranjang
    df_user = df_user.rename(columns={"index": "index_asal"}) #supaya ga salah apus data 

    # tambah kolom "No" untuk ditampilkan ke user (1,2,3,...)
    df_tampil = df_user.copy() #tmpt file yg uda di coppy
    df_tampil["No"] = range(1, len(df_tampil) + 1) #buat ngitung baris trus ditmbh 1

    # tampilkan tabel keranjang user
    print("\nKeranjang Anda:")
    print(
        tabulate(
            df_tampil[["No", "NamaProduk", "Jumlah", "Harga", "hargaTotal", "tanggal"]],
            headers="keys",
            tablefmt="fancy_grid",
            showindex=False
        )
    )

    # pilih produk mana yang mau dibayar
    print("\nPilih produk yang ingin dibayar:")
    print("- Ketik nomor item, misalnya: 1 atau 1,3,4")
    print("- Ketik 'all' untuk bayar semua")
    print("- Ketik 0 untuk batal")
    # print("- Ketik 'e' untuk menghapus produk keranjang")

    pilihan = input("Masukkan pilihan: ").strip().lower()

    if pilihan == '0':
        print("Pembayaran dibatalkan.")
        input("Tekan Enter...")
        return 

    # tentukan baris yang dipilih
    baris_terpilih = []       # list berisi baris yang akan dibayar
    index_asal_terpilih = []  # list index_asal untuk dihapus dari keranjang nanti

    if pilihan == 'all':
        # jika user memilih semua
        for i in range(len(df_user)):
            baris = df_user.iloc[i]
            baris_terpilih.append(baris)
            index_asal_terpilih.append(int(baris["index_asal"]))
    # elif pilihan == 'e':
    #     hapus_dari_keranjang(username)
    #     return
    else:
        # jika user memilih beberapa nomor
        try:
            nomor_list = [int(x.strip()) for x in pilihan.split(",") if x.strip() != ""] #pahami
        except ValueError:
            print("Input tidak valid. Gunakan angka atau 'all'.")
            input("Tekan Enter...")
            return

        # validasi nomor
        for no in nomor_list:
            if no < 1 or no > len(df_user): #ngecek nomer yg dipilih ada di daftar
                print(f"Nomor {no} tidak valid.")
                input("Tekan Enter...")
                return

        # ambil baris sesuai nomor
        for no in nomor_list:
            idx = no - 1  # karena No mulai dari 1, index dataframe mulai dari 0
            baris = df_user.iloc[idx]
            baris_terpilih.append(baris)
            index_asal_terpilih.append(int(baris["index_asal"]))

    # hitung total bayar dari produk terpilih
    total_bayar = 0
    for baris in baris_terpilih:
        total_bayar += int(baris["hargaTotal"])

    print(f"\nTotal yang akan dibayar untuk produk terpilih: Rp {total_bayar:,}")
    konfirmasi = input("Lanjutkan pembayaran? (y/n): ").strip().lower()
    if konfirmasi != 'y':
        print("Pembayaran dibatalkan.")
        input("Tekan Enter...")
        return 

    # baca data produk untuk update stok
    if not os.path.exists(produk_file):
        print("File produk tidak ditemukan! Gagal update stok.")
        input("Tekan Enter...")
        return

    df_produk = pd.read_csv(produk_file)

    # kurangi stok hanya untuk produk yang dibayar
    for baris in baris_terpilih:
        p = baris["id"] 
        q= int(baris["Jumlah"]) #jumlh produk yg ingin dibeli

        if p in df_produk["id"].values:
            stok_awal = df_produk.loc[df_produk["id"] == p, "Stok"].iloc[0]
            stok_baru = stok_awal - q
            if stok_baru < 0: 
                stok_baru = 0  # menghindari stok negatif
            df_produk.loc[df_produk["id"] == p, "Stok"] = stok_baru 

    # simpan perubahan stok
    df_produk.to_csv(produk_file, index=False)

    # simpan ke transaksi.csv
    # format: NamaUser, NamaProduk, Jumlah, Harga, HargaTotal
    if not os.path.exists(transaksi_file):
        with open(transaksi_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['NamaUser', 'NamaProduk', 'Jumlah', 'Harga', 'HargaTotal', 'Pembayaran'])

    with open(transaksi_file, 'a', newline='') as f:
        writer = csv.writer(f)
        for baris in baris_terpilih:
            writer.writerow([
                username,
                baris["NamaProduk"],
                int(baris["Jumlah"]),
                int(baris["Harga"]),
                int(baris["hargaTotal"]),
                "transfer" if pilih == '1' else
                "di tempat"   # metode pembayaran, sesuai pilihan user
            ])

    if not os.path.exists(riwayat_file):
        with open(riwayat_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['NamaUser', 'TanggalBeli', 'NamaProduk',
                            'JumlahProduk','HargaProduk', 'HargaTotal', 'Pembayaran'])

    with open(riwayat_file, 'a', newline='') as f:
        writer = csv.writer(f)
        for baris in baris_terpilih:
            writer.writerow([
                username,
                baris["tanggal"],
                baris["NamaProduk"],
                int(baris["Jumlah"]),
                int(baris["Harga"]),
                int(baris["hargaTotal"]),
                "transfer" if pilih == '1' else
                "di tempat"   # metode pembayaran, sesuai pilihan user
            ])

    # hapus hanya produk yang sudah dibayar dari keranjang user
    df_keranjang = df_keranjang.drop(index_asal_terpilih)
    df_keranjang.to_csv(keranjang_file, index=False)
    print("\nPembayaran berhasil untuk produk yang dipilih, terima kasih!")
    print("Stok produk sudah diperbarui.")
    input("Tekan Enter...")
    return menu_user(username)

def riwayat(username):
    os.system('cls')
    print("===== RIWAYAT PEMBELIAN ANDA =====")
    riwayat_file = 'riwayat.csv'

    if not os.path.exists(riwayat_file):
        print("Belum ada riwayat pembelian.")
        input("\nTekan Enter untuk kembali...")
        return

    df = pd.read_csv(riwayat_file)
    user_history = df[df['NamaUser'] == username]

    if user_history.empty:
        print("Anda belum pernah melakukan pembelian.")
        input("\nTekan Enter untuk kembali...")
        return

    # Urutkan berdasarkan tanggal (jika kolom tanggal berformat DD-MM-YYYY)
    try:
        user_history['TanggalBeli'] = pd.to_datetime(user_history['TanggalBeli'], format='%d-%m-%Y')
        user_history = user_history.sort_values(by='TanggalBeli', ascending=False)
        user_history['TanggalBeli'] = user_history['TanggalBeli'].dt.strftime('%d-%m-%Y')
    except Exception as e:
        # Jika format tanggal error, tetap tampilkan tanpa urut
        pass

    print("\nRiwayat Pembelian Anda:")
    print(tabulate(
        user_history[['TanggalBeli', 'NamaProduk', 'JumlahProduk', 'HargaProduk', 'HargaTotal', 'Pembayaran']],
        headers=['Tanggal', 'Produk', 'Jumlah', 'Harga Satuan', 'Total', 'Metode'],
        tablefmt='fancy_grid',
        showindex=False
    ))

    input("\nTekan Enter untuk kembali ke menu...")


    print("\nPembayaran berhasil!")
    print("Stok produk sudah diperbarui.")
    print("Transaksi telah dicatat ke file transaksi")
    print("Keranjang Anda sekarang kosong.")

    input("Tekan Enter...")
    return menu_user(username)

    input("\nTekan Enter untuk kembali ke menu admin...")
# ------------------------ JALANKAN PROGRAM ------------------------

main_menu()