import json
from bluepy.btle import Scanner

try:

    scanner = Scanner()
    devices = scanner.scan(20)

    devices_m = []

    for dev in devices:
        name = ""
        power = ""
        for (adtype, desc, value) in dev.getScanData():
            if (desc == "Complete Local Name"):
                name = str(value)
            elif (desc == "Tx Power"):
                power = str(value)

        devices_m.append({'addr': dev.addr, 'addType': dev.addrType, 'rssi': dev.rssi, 'name': name, 'power': power})

    json_devices = json.dumps(devices_m)
    for device in devices_m:
        print(device)

except Exception as ex:
    print ( "Unexpected error in BLE Scanner BLUEPY: %s" % ex )