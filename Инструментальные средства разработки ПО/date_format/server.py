import socket
import os
import json
import msgpack
import cbor2	
import profile_pb2

HOST, PORT = "127.0.0.1", 9999

def handle(data: bytes, fmt: str):
    if fmt == "json": return json.loads(data.decode("utf-8"))
    elif fmt == "msgpack": return msgpack.unpackb(data, raw=False)
    elif fmt == "cbor": return cbor2.loads(data)
    elif fmt == "protobuf":
        p = profile_pb2.Profile()
        p.ParseFromString(data)
        return {"id": p.id, "name": p.name, "courses": list(p.courses)}

EXT_MAP = {"json": "json", "msgpack": "msgpack", "cbor": "cbor", "protobuf": "pb"}

def save_message(payload: bytes, fmt: str):
    os.makedirs("received", exist_ok=True)
    path = f"received/message_{fmt}.{EXT_MAP[fmt]}"
    with open(path, "wb") as f: f.write(payload)
    print(f"[СОХРАНЕНО] {path} ({len(payload)} байт)")
def print_message(payload: bytes, fmt: str):
    print(f"\n=== Получено {len(payload)} байт, формат: {fmt} ===")
    print("HEX:", payload.hex())
    try: print("TEXT:", payload.decode("utf-8"))
    except UnicodeDecodeError: print("TEXT: <не текст, бинарные данные>")
    print("DATA:", handle(payload, fmt))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(1)
print(f"Сервер слушает {HOST}:{PORT}...")

conn, addr = server.accept()
print("Подключился:", addr)

fmt_byte = conn.recv(1)
fmt = {b"J": "json", b"M": "msgpack", b"C": "cbor", b"P": "protobuf"}[fmt_byte]

length = int.from_bytes(conn.recv(4), "big")
payload = b""
while len(payload) < length:
    chunk = conn.recv(length - len(payload))
    if not chunk: break
    payload += chunk

print_message(payload, fmt)
save_message(payload, fmt)
conn.close()
server.close()
