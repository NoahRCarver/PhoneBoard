#______                 ___                   __   _______ _____ 
#| ___ \               / _ \                  \ \ / /_   _|_   _|
#| |_/ /__ _ __  _ __ / /_\ \_ __  _ __  ___   \ V /  | |   | |  
#|  __/ _ \ '_ \| '_ \|  _  | '_ \| '_ \/ __|  /   \  | |   | |  
#| | |  __/ | | | | | | | | | |_) | |_) \__ \ / /^\ \_| |_ _| |_ 
#\_|  \___|_| |_|_| |_\_| |_/ .__/| .__/|___/ \/   \/\___/ \___/ 
#                           | |   | |                            
#                           |_|   |_|                            
# Bluetooth to keyboard event
import bluetooth, sys

TARGET_NAME = "Galaxy S5 CM"


target_address = None

print("Recommended: pair the phone with Bluetooth.")
print("Searching for nearby devices...")

nearby_devices = bluetooth.discover_devices(duration=10)
for bdaddr in nearby_devices:
    lookup = bluetooth.lookup_name(bdaddr)
    print(bdaddr, lookup)

    if TARGET_NAME == lookup:
        target_address = bdaddr
        break

if target_address:
    print("Found target", TARGET_NAME)
else:
    print("Could not find bluetooth device nearby.")
    sys.exit()


server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
PORT = 1337
server_sock.bind(("", PORT))
server_sock.listen(1)

print(server_sock.getsockname())







