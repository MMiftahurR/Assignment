Case:
Membuat middleware untuk mentranslasikan perintah dari client http ke mesin di smart home. Perintah berupa perintah nyala/mati. perangkat melakukan subscribe ke broker untuk mendapatkan perintah dari client. Sistem dijalankan dengan mosquitto server sebagai broker.

Running client pada windows:

py client_htpp.py [perangkat]
py middleware.py
py perangkat.py [perangkat]

perangkat = kulkas/kipas/lampu
