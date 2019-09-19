import ctypes, time
# Bunch of stuff so that the script can send keystrokes to game #

SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions
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
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def KeyPress(hexkeycode, step=3, length=.05):
    time.sleep(step)
    PressKey(hexkeycode)
    time.sleep(length)
    ReleaseKey(hexkeycode)

def MultiKeyPress(hexkeycode, hexkey2, step=3, length=.05):
    time.sleep(step)
    PressKey(hexkeycode)
    PressKey(hexkey2)
    time.sleep(length)
    ReleaseKey(hexkey2)
    ReleaseKey(hexkeycode)

tilde = 0x29
space_bar = 0x39
tab = 0x0F
period = 0x34

lctrl = 0x1D
shift = 0x2A
enter = 0x1C

jump_step = .5
jump_time = 0

beginner_step = .7
beginner_time = .245

intermediate_step = .736
intermediate_time = .18

test_step = .55
test_time = .06

seventy_five = .50

if __name__ == '__main__':
    numbers = [0x0B, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A]

    time.sleep(3)

    curr = 9000
    while True:
        # KeyPress(tab, .5, .5) # 0x29 = `
        temp = curr
        first = temp % 10
        temp = temp // 10
        second = temp % 10
        temp = temp // 10
        third = temp % 10
        temp = temp // 10
        fourth = temp % 10
        temp = temp // 10

        KeyPress(period, .03, .03)
        KeyPress(numbers[fourth], .03, .03)
        KeyPress(numbers[third], .03, .03)
        KeyPress(numbers[second], .03, .03)
        KeyPress(numbers[first], .03, .03)

        # print(curr)
        # KeyPress(numbers[third], numbers[second], numbers[first])

        KeyPress(tab, .05, .05)

        temp = 10000 - curr
        first = temp % 10
        temp = temp // 10
        second = temp % 10
        temp = temp // 10
        third = temp % 10
        temp = temp // 10
        fourth = temp % 10
        temp = temp // 10

        KeyPress(period, .03, .03)
        KeyPress(numbers[fourth], .03, .03)
        KeyPress(numbers[third], .03, .03)
        KeyPress(numbers[second], .03, .03)
        KeyPress(numbers[first], .03, .03)

        curr += 1

        KeyPress(tab, .05, .05)
        KeyPress(enter, .05, .05)
        MultiKeyPress(shift, tab, .05, .05)
        MultiKeyPress(shift, tab, .05, .05)
