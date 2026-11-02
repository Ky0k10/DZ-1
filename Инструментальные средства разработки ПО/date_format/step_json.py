import json
from data import PROFILE

json_str = json.dumps(PROFILE, ensure_ascii=False, indent=2)
print("=== JSON ===")
print(json_str)
print("Размер:", len(json_str.encode("utf-8")), "байт")

restored = json.loads(json_str)
assert restored == PROFILE
print("Десериализация успешна:", restored["name"])
