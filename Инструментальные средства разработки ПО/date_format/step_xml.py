import xml.etree.ElementTree as ET
from data import PROFILE

def dict_to_xml(tag, d):
    elem = ET.Element(tag)
    for key, val in d.items():
        if isinstance(val, dict):
            elem.append(dict_to_xml(key, val))
        elif isinstance(val, list):
            list_elem = ET.SubElement(elem, key)
            for item in val:
                item_elem = ET.SubElement(list_elem, "item")
                item_elem.text = str(item)
        else:
            child = ET.SubElement(elem, key)
            child.text = str(val)
    return elem

root = dict_to_xml("profile", PROFILE)
xml_str = ET.tostring(root, encoding="unicode")
print("=== XML ===")
print(xml_str)
print("Размер:", len(xml_str.encode("utf-8")), "байт")

parsed = ET.fromstring(xml_str)
