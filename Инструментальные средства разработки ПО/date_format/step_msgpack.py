import msgpack
from data import PROFILE

packed = msgpack.packb(PROFILE, use_bin_type=True)
print("=== MessagePack ===")
print("HEX:", packed.hex())
print("Размер:", len(packed), "байт")

restored = msgpack.unpackb(packed, raw=False)
assert restored == PROFILE
