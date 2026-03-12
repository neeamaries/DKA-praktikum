# Konversi suhu dari celcius 
celcius = float(input("Masukkan suhu dalam Celcius : ")) # Meminta input celcius ke user
                                                         # Diubah ke float untuk memudahkan perhitungan
fahrenheit = (celcius * 9/5) + 32 # Konversi celcius ke fahrenhreit sesuai rumus 
kelvin = celcius + 273.15 # Konversi celcius ke kelvin sesuai rumus

print(f"{celcius:.2f} °C = {fahrenheit:.2f} °F = {kelvin:.2f} K") # Menampilkan output dari hasil konversi
                                                                  # Menggunakan print f dan .2f agar terdapat 2 angka dibelakang koma
