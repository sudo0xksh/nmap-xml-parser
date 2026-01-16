import xml.etree.ElementTree as ET
import sys

def xmlparse(output):
    tree = ET.parse(output)
    root = tree.getroot()

    for port in root.findall(".//port"):
        id = port.get("portid")
        state = port.find("state").get("state")
        service = port.find("service").get("name")
        print(f"Port {id} → {state} ({service})")

if len(sys.argv) < 2:
    print("Usage: python nmap_xmlparser.py <output.xml>")
    sys.exit()

output = sys.argv[1]

xmlparse(output)