import win32api

keyList = ["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'APS$/\\":
    keyList.append(char)

# returns cursor position, stored in a tuple (x,y)    
def cursorPos():
    pos = win32api.GetCursorPos()
    return pos

# 
def key_input():
    keys = []
    for key in keyList:
        if win32api.GetAsyncKeyState(ord(key)):
            keys.append(key)
    if 'S' in keys: # S and D match with my bindings is osu!
        return 'S'
    elif 'D' in keys:
        return 'D'
    elif 'B' in keys: # button to start recording data
        return 'B'
    elif 'H' in keys: # button to stop recording data
        return 'H'
    else:
        return None # in the case that no key is pressed