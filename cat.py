import random

def tebak_kucing():
    # Pilih lubang secara acak dari 1 sampai 5
    lubang_kucing = random.randint(1, 5)
    print("Selamat datang di permainan Tebak Kucing!")
    print("Kucing tersembunyi di salah satu lubang dari 1 sampai 5.")
    print("Coba tebak di lubang mana kucing berada!")

    while True:
        try:
            tebakan = int(input("Masukkan nomor lubang (1-5): "))
            if tebakan < 1 or tebakan > 5:
                print("Nomor lubang harus antara 1 dan 5. Coba lagi!")
                continue
            if tebakan == lubang_kucing:
                print("Selamat! Anda menemukan kucing di lubang", tebakan)
                break
            else:
                print("Salah! Kucing tidak di lubang", tebakan, ". Coba lagi!")
        except ValueError:
            print("Masukkan nomor yang valid!")

if __name__ == "__main__":
    tebak_kucing()
