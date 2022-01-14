import
    osproc,
    os,
    strformat,
    "./shell",
    "./path" 

proc notifyDaemon(): string = 
    if execCmdEx("whereis dunst").exitCode == 0:
        return "dunst"
    else: 
        return "notify-send"

proc notifySend*(
    title: string = "System", 
    subtitle: string = "Notification",
    icon: string = QTILE_PATH / "icons" / "Settings.png", 
    time_out: int = 5000,
) =
    case notifyDaemon():
        of "dunst":
            let cmd = &"dunstify \"{title}\" \"{subtitle}\" -t {time_out} -I \"{icon}\""
            shell:
                ($cmd)
        of "notify-send":
            let cmd = &"notify-send \"{title}\" \"{subtitle}\" -t {time_out}"
            shell:
                ($cmd)