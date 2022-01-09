import 
    "./shell", # Vindaar's module.
    "./paths.nim"
import 
    osproc, 
    strformat


let KEYBOARDS = @["us", "es"]


proc currentLayout(): string {.inline.} = 
    execCmdEx(fmt"{KEYBOARD_SCRIPT()} print %e").output

    
proc next_layout(): string =
    let cy: string = currentLayout()
    echo cy
    var next_l: string
    
    echo KEYBOARDS[0]
    echo KEYBOARDS[1]

    try:
        echo "try"
        next_l = KEYBOARDS[KEYBOARDS.find(cy) + 1]
        echo KEYBOARDS.find(cy)
    except:
        echo "except"
        next_l = KEYBOARDS[0]
    finally:
        echo "finally"
        return next_l


proc main() =
    let a = next_layout()
    echo a


main()