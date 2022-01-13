import
    osproc,
    os,
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
            shell:
                dunstify "\'"($title)"\'" "\'"($subtitle)"\'" -t ($time_out) -I "\'"($icon)"\'"
        of "notify-send":
            shell:
                "notify-send" "\""($title)"\"" "\""($subtitle)"\"" -t ($time_out)