import 
    nimpy, # https://github.com/yglukhov/nimpy
    osproc,
    os,
    "./shell",
    "./paths" 

proc notifyDaemon(): string = 
    if execCmdEx("whereis dunst").exitCode == 1:
        return "dunst"
    else: 
        return "notify-send"

proc notifySend*(
    title: string = "System", 
    subtitle: string = "Notification",
    icon_path: string = QTILE_PATH / "icons" / "Settings.png", 
    time_out: int = 5000,
) {.exportpy.} =
    case notifyDaemon():
        of "dunst":
            shell:
                dunstify "\""($title)"\"" "\""($subtitle)"\"" -t ($time_out) -I "\""($icon_path)"\""
        of "notify-send":
            shell:
                "notify-send" "\""($title)"\"" "\""($subtitle)"\"" -t ($time_out)