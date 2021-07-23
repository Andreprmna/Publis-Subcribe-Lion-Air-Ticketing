import paho.mqtt.client as mqtt
import time
import re

# fungsi untuk mengecek topic
def cek_message(client,userdata, message):
    #  decode message menjadi string
    dMessage = str(message.payload.decode("utf-8"))
    print(dMessage)
    # menyimpat pesan yang di decode bila terdapat waktu
    boarding = re.search('Waktu',dMessage)
    # jika boarding maka akan di simpan ke boarding.txt
    if boarding:
        file = open('Boarding.txt','a')
        file.write(_message)
        file.close()
    else:
        file = open('Lokasi.txt','a')
        file.write(_message)
        file.close()

broker = '192.168.43.3'
port = 12345

print("creating new instance")
subscriber = mqtt.Client('S1')

subscriber.on_message = cek_message

print("connection to broker")
subscriber.connect(broker,port)

subscriber.loop_start()

print("subscribing to topic")
subscriber.subscribe([('Lokasi',2),('Boarding',1)])

while True:
    time.sleep(1)
subscriber.loop_stop()