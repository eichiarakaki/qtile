import "./shell"
import 
    nimpy, # https://github.com/yglukhov/nimpy
    os

proc notifyDaemon(): string = 
    
proc sendNotify(
    title: string, 
    subtitle: string, 
    icon_path: string, 
    time_out: int = 5,
) {.exportpy.} =
    const default_notification: string = "Keyboard Notification"
    shell:




