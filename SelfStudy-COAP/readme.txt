Referensi:
Untuk contoh coap.server.py dan coap.client.py didapatkan dari https://github.com/Tanganelli/CoAPthon

Case:
Translasi perintah nyala/mati perangkat dari client http ke perangkat (sama seperti MQTT-Quiz). Perangkat merequest perintah dari coap server yang sudah dimodifikasi untuk mengakomodasi perangkat dan client http.

Running pada windows :
py coap.server.appliance.py
py coap.middleware.py
py client_http [perangkat]
py coap.perangkat.py [serverhost:serverport] [perangkat]

perangkat = app1/app2/app3
