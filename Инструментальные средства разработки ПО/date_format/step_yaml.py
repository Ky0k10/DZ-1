import yaml
from data import PROFILE

yaml_str = yaml.dump(PROFILE, allow_unicode=True, sort_keys=False, default_flow_style=False)
print("=== YAML ===")
print(yaml_str)
print("Размер:", len(yaml_str.encode("utf-8")), "байт")

restored = yaml.safe_load(yaml_str)
assert restored == PROFILE
print("Десериализация успешна:", restored["name"])
