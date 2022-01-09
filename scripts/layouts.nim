import 
    "./shell", # Vindaar's module.
    "./paths.nim"
import 
    osproc, 
    strformat,
    strutils

const COMMAND = "setxkbmap"


let KEYBOARDS: seq[string] = @["us", "es"]
proc next_layout(): string =
    let current_l: string = execCmdEx(fmt"{KEYBOARD_SCRIPT()} print %e").output
    var next_l: string

    try:
        next_l = KEYBOARDS[KEYBOARDS.find(current_l.strip()) + 1]
    except:
        next_l = KEYBOARDS[0]
    finally:
        return next_l


proc set_layout() =
        shell:
            ($COMMAND) ($next_layout())


proc main() =
    set_layout()


main()