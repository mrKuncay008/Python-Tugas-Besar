import os

os.system("cls")
os.system("clear")

print("\n\t----------- Welcome To BlueDorzz Mobile -------------")
print("\t =============== Hotel Booking System  ================")
print("\t ------------------------------------------------ ")
print("\t Kelompok 5")
print()
print()

# Fungsi pertama
def print_booking_details(room_number, room_type, number_of_guests, room_rate):
    print("\t\tAnda telah memesan nomor kamar", room_number, "(", room_type, ") Untuk", number_of_guests, "Tamu dengan Tarif Rp."+str(room_rate)+".000 per Malam.")

# Fungsi ke dua
def calculate_total_cost(number_of_rooms, number_of_nights, room_rate, current_rooms):
    if current_rooms > number_of_rooms:
        return 0
    else:
        return calculate_total_cost(number_of_rooms, number_of_nights, room_rate, current_rooms + 1) + number_of_nights * room_rate 


hotel_name = input("\n\t Di Mohon Masukan Nama hotel yang anda ingin Booking: ")
number_of_rooms = int(input("\tMasukkan jumlah kamar yang ingin Anda pesan: "))
number_of_nights = int(input("\tMasukkan jumlah malam Anda akan menginap di hotel: "))

print(" \n\t\t\t Terimakasih Sudah Booking!", number_of_rooms, "Kamar Di", hotel_name, ".")
print()

booking_details = {} # -> Dictionaries ke-1
guests = {} # -> Dictionaries ke-2

# Tuples
room_types = ("single","double","suite")

# ini adalah bagian Nested Loop
for i in range(1, number_of_rooms + 1):
    room_number = int(input("\tSilakan masukkan no kamar " + str(i) + ": "))
    room_type = input("\tMau Pilih Tipe Apa (single/double/suite): ")
    number_of_guests = int(input("\tHarap masukkan jumlah tamu untuk kamar " + str(i) + ": "))
    room_rate = 0

 # Terdapat penggunaan nested IF dan Tuples dalam bagian ini
    if room_type in room_types:
        if room_type == "single":
            room_rate = 200
        elif room_type == "double":
            room_rate = 250
        elif room_type == "suite":
            room_rate = 500
    else:
        print("Tipe Kamar Tidak Valid, Harap Di Coba Lagi")
        continue
    guests_data = []

# Ini adalah Integrasi dari Nested IF, Nested Loop dan Fungsi 
    for j in range(1, number_of_guests + 1):
        guest_name = input("\n\tSilakan masukkan nama tamu: ")
        guests_data.append(guest_name)

    guests[room_number] = guests_data
    booking_details[room_number] = {"room_type": room_type, "number_of_guests": number_of_guests, "room_rate": room_rate}

    print_booking_details(room_number, room_type, number_of_guests, room_rate)

total_cost = calculate_total_cost(number_of_rooms, number_of_nights, room_rate, 1)

# Output Akhir atau Cetak Invoice

print("\n\t\t====================     Invoice      =================")
print("\t\tTotal biaya pemesanan Anda untuk", number_of_nights, "Malam adalah:\n\t\tRp."+ str(total_cost) +".000")

for room_number, details in booking_details.items():
    room_type = details["room_type"]
    number_of_guests = details["number_of_guests"]
    room_rate = details["room_rate"]
    print("\t\tAnda telah memesan nomor kamar", room_number, "(", room_type, ") Untuk", number_of_guests, "Tamu dengan tarif:\n\t\tRp."+ str(total_cost) +".000\n\n")

print("\t\t============================================================")
print("\t\tTotal biaya pemesanan Anda untuk", number_of_nights, "Malam: Rp."+ str(total_cost)+ ".000")

# Exceptions:
try:
    file_name = input("Masukkan nama file untuk menyimpan data pemesanan: ")
    with open(file_name, "w") as file:
        file.write("Nama Hotel: " + hotel_name + "\n")
        file.write("Jumlah Kamar: " + str(number_of_rooms) + " Kamar\n")
        file.write("Jumlah Malam: " + str(number_of_nights) + " Malam\n")
        file.write("\nRincian Pemesanan:\n")
        for room_number, details in booking_details.items():
            file.write("\nNomor Kamar: " + str(room_number) + "\n")
            file.write("Tipe Kamar: " + details["room_type"] + "\n")
            file.write("Jumlah Tamu: " + str(details["number_of_guests"]) + "\n")
            file.write("Tarif Kamar: Rp. " + str(details["room_rate"]) + ".000\n")
            file.write("Tamu:")
            for guest in guests[room_number]:
                file.write(" " + guest + ",")
            file.write("\n")
        file.write("\nTotal Biaya: Rp. " + str(total_cost) + ".000\n")
    print("Data pemesanan berhasil disimpan dalam file", file_name)
except Exception as e:
    print("Terjadi kesalahan saat menyimpan data pemesanan:", str(e))
    
    # Data Processing:
    #   Terdapat beberapa proses pemrosesan data dalam kode ini, seperti:
    #     Meminta input pengguna untuk informasi pemesanan seperti nama hotel, jumlah kamar, jumlah malam menginap, nomor kamar, jenis kamar, dan jumlah tamu.
    #     Menghitung total biaya pemesanan berdasarkan jumlah kamar, jumlah malam menginap, dan tarif kamar.
    #     Menyimpan rincian pemesanan ke dalam dictionaries (booking_details dan guests).
    #     Mencetak invoice dan rincian pemesanan.
    #     Meminta pengguna untuk memasukkan nama file untuk menyimpan data pemesanan ke dalam file teks.
    #     Menyimpan data pemesanan ke dalam file dengan format yang sesuai.