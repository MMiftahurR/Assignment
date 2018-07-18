Case:
buat middleware sebuah perangkat yg bisa dipakai sebuah jembatan untuk mengakses perangkat yg berbeda. sensor suhu sensor kelembapan sensor CO,ketiganya  mengirimkan datanya ke perangkat middleware. data disimpan dimiddlewware, bisa pake list atau dictionary, dan sisi lain ada user, untuk dapat mengakses data tadi, menggunakan rest HTTP. method GET /sensor untuk mendapatkan semuanya data, dan kedua /sensor/<jenis> untuk medapatkan data sensor berenis tertentu. sistem dijalankan dengan mosquitto server sebagai broker.

Running client pada windows:

py client_htpp.py [perangkat]
py middleware.py
py perangkat.py

perangkat = humidity/suhu/co2
