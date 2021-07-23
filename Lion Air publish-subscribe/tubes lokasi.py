import paho.mqtt.client as mqtt
import time
from datetime import datetime

# mendefinisikan broker serta port yang akan digunakan
broker = ('192.168.43.3')
port = 12345

# membuat publisher dengan nama P2
print("creating new publisher")
publisher = (mqtt.Client('P2'))
print("publisher P1 successfully create") 

# melakukan koneksi ke broker dengan port
print("connecting to broker")
publisher.connect(broker,port)
print("connect with :",broker,port)

# loop untuk dimulai
publisher.loop_start()

# memulai mempublish topic 
print("publishing topic")
for i in range(20):
    time.sleep(1)
    publisher.publish('Lokasi',input(("Kota :")))
# jika sudah mempublish 20 topic 
print("sucess publish topic")
publisher.loop_stop()