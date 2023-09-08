import pexpect
import sys
 
DEVICE = "be:58:da:01:69:ce"
selected_color = {
    "red" : "7e000503FF000000ef",
    "green": "7e00050300440000ef",
    "yellow": "7e000503FF4D0000ef",
    "boot": "7e00050300000000ef",
    "off": "7e0004000000ff00ef"
}

if len(sys.argv) > 1:
    argument = sys.argv[1]
    #print(f"Argument received: {argument}")
else:
    print("No argument provided.")
    sys.exit()

try:
    #print("Hexiwear address:"),
    #print(DEVICE)
    
    # Run gatttool interactively.
    #print("Run gatttool...")
    child = pexpect.spawn("gatttool -I")
    
    # Connect to the device.
    #print("Connecting to "),
    #print(DEVICE),
    child.sendline("connect {0}".format(DEVICE))
    child.expect("Connection successful", timeout=5)
    print(" Connected!")

    #power_on_cmd = "char-write-req 0x0009 7e0004f00001ff00ef"
    #child.sendline(power_on_cmd)
    #child.expect("Characteristic value/descriptor: ", timeout=10)
    #child.expect("\r\n", timeout=10)

    command = "char-write-req 0x0009 "+selected_color[argument]
    print(command)
    child.sendline(command)
    child.expect("Characteristic value was written successfully", timeout=10)
    child.expect("\r\n", timeout=10)


except Exception as e:
    print("Error: "+str(e))