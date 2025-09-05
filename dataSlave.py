import paho.mqtt.client as mqtt

client = mqtt.Client("dataUpload");

#/gokart/dataPack
#/gokart/dataFaults

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Forbundet til hiveMQ cluster")
        client.subscribe("gokart/dataPack")
        client.subscribe("gokart/dataFaults")
    else:
        print("Forbindelse fejlet rc: ", rc)

def on_logIn(client, userdata, level, buf):
    print("log: ", buf);

def on_message(client, userdata, msg):
    print(f"Modtaget besked på {msg.topic}: {msg.payload.decode()}")

client.on_connect = on_connect
client.on_log = on_logIn
client.on_message = on_message

broker = "4d881b47b776416f9fe8b1df9fe3ae48.s1.eu.hivemq.cloud"
port = 8883

client.username_pw_set("dataUpload", "dataUpload123")

client.tls_set()

client.connect(broker, port)

client.loop_forever()
