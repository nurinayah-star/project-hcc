# daftar_nama = []

daftar_nama = None

def buka_file(mode):
    global daftar_nama
    daftar_nama = open("data.txt",mode)

def tutup_file():
    global daftar_nama
    if daftar_nama:
        daftar_nama.close()
        daftar_nama = None

def tambah_nama():
    global daftar_nama
    buka_file("a")
    print("silahkan tambahkan nama baru\n")
    nama_baru = input("masukkan nama baru: ")
    daftar_nama.write(nama_baru + "\n")
    print(f"tugas {nama_baru} telah ditambahkan ke")
    tutup_file()

def lihat_nama():
    global daftar_nama
    try:
        buka_file("r")
        print("Daftar Nama yang tersimpan:\n")
        isi = daftar_nama.readlines()
        if not isi:
            print("belum ada yang tersimpan")
        else:
            for i, nama in enumerate(isi,start=1):
                print(f"{i} {nama.strip()}")

    except FileNotFoundError:
        print("file tidak di temukan")
    finally:
        tutup_file()
            
def ubah_nama():
    print(f"--- ubah nama ---")
    global daftar_nama
    buka_file("r")
    print("Daftar Nama yang tersimpan:\n")
    isi = daftar_nama.readlines()
    tutup_file()

    if not isi:
        print("belum ada data yang tersimpan")

    for i, nama in enumerate(isi, start=1):
        print(f"{i} {nama.strip()}")

    try:
        pilihan = int(input("\nPilih nama yang ingin di ubah : "))
        if pilihan < 1 or pilihan > len(isi):
            print("nomor tidak valid")
            return

        nama_lama = isi[pilihan - 1].strip()
        nama_baru = input(f"Masukan nama untuk menggantikan {nama_lama} : ")
        isi[pilihan - 1] = nama_baru + "\n"

        buka_file("w")
        daftar_nama.writelines(isi)

    except FileNotFoundError:
        print("File data.txt belum ada. Tambahkan nama dulu.\n")
    except ValueError:
        print("Input harus berupa angka yang sesuai dengan daftar nama.\n")
    
    finally:
        tutup_file()


def hapus_nama():
    print("--- hapus nama ---")
    global daftar_nama
    buka_file("r")
    print("Daftar Nama yang tersimpan:\n")
    isi = daftar_nama.readlines()
    tutup_file()

    if not isi:
        print("belum ada data yang tersimpan")

    for i, nama in enumerate(isi, start=1):
        print(f"{i} {nama.strip()}")

    try:
        pilihan = int(input("\nPilih nama yang ingin di ubah : "))
        if pilihan < 1 or pilihan > len(isi):
            print("nomor tidak valid")
            return
        
        nama_dihapus = isi.pop(pilihan - 1).strip()
        buka_file("w")
        daftar_nama.writelines(isi)
    
    except FileNotFoundError:
        print("File data.txt belum ada. Tambahkan nama dulu.\n")
    except ValueError:
        print("Input harus berupa angka yang sesuai dengan daftar nama.\n")
    
    finally:
        tutup_file()

   
def main():
    while True:
        print("\n----Daftar nama ----")
        print("1. Tambah nama")
        print("2. Lihat nama")
        print("3. Perbarui nama")
        print("4. Hapus nama")
        print("5 keluar")
        
        pilihan = input("Pilih (1-4): ")
        print("-----------------------")
        
        if pilihan == '1':
            tambah_nama()
        elif pilihan == '2':
            lihat_nama()
        elif pilihan == '3':
            ubah_nama()
        elif pilihan == '4':
            hapus_nama()
        elif pilihan == '5':
            print("anda keluar dari program")
            break
            
if __name__ == "__main__":
    main()