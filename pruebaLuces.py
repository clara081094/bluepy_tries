from bluepy import btle
import sys

argument = None
peripheral = None
selected_color = {
    "red" : bytearray([0x7e, 0x00, 0x05, 0x03, 0xFF, 0x00, 0x00, 0x00, 0xef]),
    "green": bytearray([0x7e, 0x00, 0x05, 0x03, 0x00, 0x44, 0x00, 0x00, 0xef]),
    "yellow": bytearray([0x7e, 0x00, 0x05, 0x03, 0xFF, 0x4D, 0x00, 0x00, 0xef]),
    "off": bytearray([0x7e, 0x00, 0x04, 0x00, 0x00, 0x00, 0xff, 0x00, 0xef])
}

if len(sys.argv) > 1:
    argument = sys.argv[1]
    #print(f"Argument received: {argument}")
else:
    print("No argument provided.")
    sys.exit()

mac_address = "be:58:da:01:69:ce"
peripheral = btle.Peripheral(mac_address)

#uuid_service = "0000fff0-0000-1000-8000-00805f9b34fb"
#uuid_char = "0000fff3-0000-1000-8000-00805f9b34fb"

try:  
    #for service in peripheral.getServices():
    #    print(f"Service UUID: {service.uuid}")
    #    for characteristic in service.getCharacteristics():
    #        print(f"Characteristic UUID: {characteristic.uuid}")

    power_on_cmd = bytearray([0x7e, 0x00, 0x04, 0xf0, 0x00, 0x01, 0xff, 0x00, 0xef])
    power_off_cmd = bytearray([0x7e, 0x00, 0x04, 0x00, 0x00, 0x00, 0xff, 0x00, 0xef])

    peripheral.writeCharacteristic(0x0009, power_on_cmd, withResponse=True)
    peripheral.writeCharacteristic(0x0009, selected_color[argument], withResponse=True)
    peripheral.disconnect()
    print("Done")

except Exception as e:
    print("Error")