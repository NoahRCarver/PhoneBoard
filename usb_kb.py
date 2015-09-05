#______                 ___                   __   _______ _____ 
#| ___ \               / _ \                  \ \ / /_   _|_   _|
#| |_/ /__ _ __  _ __ / /_\ \_ __  _ __  ___   \ V /  | |   | |  
#|  __/ _ \ '_ \| '_ \|  _  | '_ \| '_ \/ __|  /   \  | |   | |  
#| | |  __/ | | | | | | | | | |_) | |_) \__ \ / /^\ \_| |_ _| |_ 
#\_|  \___|_| |_|_| |_\_| |_/ .__/| .__/|___/ \/   \/\___/ \___/ 
#                           | |   | |                            
#                           |_|   |_|
# USB connection to keyboard
import os, platform, ctypes, time

if platform.system() == "Windows":
    SendInput = ctypes.windll.user32.SendInput

    # C struct redefinitions (by lucasg) 
    PUL = ctypes.POINTER(ctypes.c_ulong)
    class KeyBdInput(ctypes.Structure):
        _fields_ = [("wVk", ctypes.c_ushort),
                    ("wScan", ctypes.c_ushort),
                    ("dwFlags", ctypes.c_ulong),
                    ("time", ctypes.c_ulong),
                    ("dwExtraInfo", PUL)]

    class HardwareInput(ctypes.Structure):
        _fields_ = [("uMsg", ctypes.c_ulong),
                    ("wParamL", ctypes.c_short),
                    ("wParamH", ctypes.c_ushort)]

    class MouseInput(ctypes.Structure):
        _fields_ = [("dx", ctypes.c_long),
                    ("dy", ctypes.c_long),
                    ("mouseData", ctypes.c_ulong),
                    ("dwFlags", ctypes.c_ulong),
                    ("time",ctypes.c_ulong),
                    ("dwExtraInfo", PUL)]

    class Input_I(ctypes.Union):
        _fields_ = [("ki", KeyBdInput),
                     ("mi", MouseInput),
                     ("hi", HardwareInput)]

    class Input(ctypes.Structure):
        _fields_ = [("type", ctypes.c_ulong),
                    ("ii", Input_I)]

    # Actuals Functions

    def PressKey(hexKeyCode):

        extra = ctypes.c_ulong(0)
        ii_ = Input_I()
        ii_.ki = KeyBdInput( hexKeyCode, 0x48, 0, 0, ctypes.pointer(extra) )
        x = Input( ctypes.c_ulong(1), ii_ )
        SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

    def ReleaseKey(hexKeyCode):

        extra = ctypes.c_ulong(0)
        ii_ = Input_I()
        ii_.ki = KeyBdInput( hexKeyCode, 0x48, 0x0002, 0, ctypes.pointer(extra) )
        x = Input( ctypes.c_ulong(1), ii_ )
        SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


    def key_to_hexcode(key):
        if key in "1234567890":
            return int(key) + 0x60
        else:
            lookup = {"NUMLOCK": 0x90, '/': 0xBF, '*': 0x6A, '-': 0x6D, '+': 0x6B,
                      '.': 0x6E, "ENTER": 0x0D}
            return lookup[key]
                


if __name__ == "__main__":
    PressKey(key_to_hexcode('+'))
        
            
        
