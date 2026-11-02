import profile_pb2
from data import PROFILE

p = profile_pb2.Profile()
p.id = PROFILE["id"]
p.name = PROFILE["name"]
p.age = PROFILE["age"]
p.is_student = PROFILE["is_student"]
p.courses.extend(PROFILE["courses"])
p.address.city = PROFILE["address"]["city"]
p.address.zip = PROFILE["address"]["zip"]

binary = p.SerializeToString()
print("=== Protobuf ===")
print("HEX:", binary.hex())
print("Размер:", len(binary), "байт")

p2 = profile_pb2.Profile()
p2.ParseFromString(binary)
print("Десериализация успешна:", p2.name)
