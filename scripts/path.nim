import os

let ROFI_LAUNCHER*: string = expandTilde("~") / ".config" / "rofi"
let QTILE_PATH*: string = expandTilde("~") / ".config" / "qtile"
let KEYBOARD_NAME*: string = QTILE_PATH / "scripts" / "bin" / "xkblayout-state"

proc KEYBOARD_SCRIPT*(): string {.inline.} = 
    if fileExists(KEYBOARD_NAME):
        return expandFilename(KEYBOARD_NAME)
    else: 
        raise newException(OSError, "Keyboard File was not found!")
