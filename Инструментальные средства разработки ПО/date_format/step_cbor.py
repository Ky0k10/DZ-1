import cbor2
from data import PROFILE

encoded = cbor2.dumps(PROFILE)
print("=== CBOR ===")
print("HEX:", encoded.hex())
print("Размер:", len(encoded), "байт")

restored = cbor2.loads(encoded)
assert restored == PROFILE
print("Десериализация успешна:", restored["name"])
