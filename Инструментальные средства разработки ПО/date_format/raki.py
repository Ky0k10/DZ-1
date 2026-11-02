import profile_pb2
p = profile_pb2.Profile()
with open("received/message_protobuf.pb", "rb") as f:
    p.ParseFromString(f.read())
print("Имя:", p.name)
print("Email (новое поле):", repr(p.email)) # Будет пустая строка!
