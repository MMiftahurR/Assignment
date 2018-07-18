Case:
Sensor-to-Cloud  Gateway  
a.Komponen  ini  berperan  untuk  menerima  data  yang  dikirimkan  oleh  perangkat  sensor  node  untuk  kemudian  disimpan  dalam  perangkat  Distributed  Database.  
b.Terdiri  atas  MQTT  broker  dan  subscriber tunggal.  
c.Komponen  ini  harus  dapat  berkomunikasi  dengan  Distributed  Database.

User-to-  Cloud  Gateway
a.Komponen  ini  berperan  sebagai  perantara  antara  cloud  dan  pengguna  akhir.
b.Aplikasi  pengguna  mengakses  data  yang  disimpan  di  cloud  menggunakan  protokol  HTTP  berarsitektur  Restful  Webservice.

Untuk database pada project yang saya kerjakan tidak bersifat distributed. sehingga untuk source code sensor-to-cloud gateway hanya terhubung dengan database biasa, bukan distributed database.
