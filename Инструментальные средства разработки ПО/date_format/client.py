import socket
import json
import msgpack
import cbor2
import profile_pb2
from data import PROFILE

HOST, PORT = "127.0.0.1", 9999
FMT = "yaml"  # ВАЖНО: меняйте это значение для теста разных форматов!

if FMT == "json":
    payload = json.dumps(PROFILE, ensure_ascii=False).encode("utf-8")
    fmt_byte = b"J"
elif FMT == "msgpack":
    payload = msgpack.packb(PROFILE, use_bin_type=True)
    fmt_byte = b"M"
elif FMT == "cbor":
    payload = cbor2.dumps(PROFILE)
    fmt_byte = b"C"
elif FMT == "protobuf":
    p = profile_pb2.Profile()
    p.id = PROFILE["id"]
    p.name = PROFILE["name"]
    p.age = PROFILE["age"]
    p.is_student = PROFILE["is_student"]
    p.courses.extend(PROFILE["courses"])
    p.address.city = PROFILE["address"]["city"]
    p.address.zip = PROFILE["address"]["zip"]
    payload = p.SerializeToString()
    fmt_byte = b"P"

print(f"Отправка в формате {FMT}, размер: {len(payload)} байт")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
client.sendall(fmt_byte)
client.sendall(len(payload).to_bytes(4, "big"))
client.sendall(payload)
client.close()
print("Отправлено.")
