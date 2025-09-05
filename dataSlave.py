import paho.mqtt.client as mqtt

client = mqtt.Client(client_id="dataUpload", protocol=mqtt.MQTTv5)


def on_connect(client, userdata, flags, reasonCode, properties):
    if reasonCode == 0:
        print("Forbundet til HiveMQ cluster")
        client.subscribe("gokart/dataPack")
        client.subscribe("gokart/dataFaults")
    else:
        print("Forbindelse fejlet rc:", reasonCode)

def on_message(client, userdata, msg):
    print(f"Modtaget besked på {msg.topic}: {msg.payload.decode()}")

def on_log(client, userdata, level, buf):
    print("log:", buf)

client.on_connect = on_connect
client.on_message = on_message
client.on_log = on_log

client.username_pw_set("dataUpload", "dataUpload123")
client.tls_set()

broker = "4d881b47b776416f9fe8b1df9fe3ae48.s1.eu.hivemq.cloud"
port = 8883
client.connect(broker, port)

client.loop_forever()
