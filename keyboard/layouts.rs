use std::process::Command;
use std::path::{Path, PathBuf};
use std::collections::HashMap;
use std::env;
// Is a shit of code I know, but it works uwu

fn send_notification(layout: String) {
    let format = format!("Layout: {}", layout.to_uppercase());
    let config_dir = std::env::var("XDG_CONFIG_HOME")
            .map(PathBuf::from)
            .unwrap_or_else(|_| PathBuf::from(std::env::var("HOME").unwrap())
            .join(".config")
            .join("dunst"))
            .join("icons")
            .join("SettingsBlue.png");

    Command::new("dunstify")
            .args(&["-I", &config_dir.into_os_string().into_string().unwrap()])
            .arg("Keyboard Notification")
            .arg(format)
            .args(&["-t", "1000"])
            .spawn()
            .expect("failed to execute process");
}


fn set_keyboard(layout: String) {
    let cmd: &str = "setxkbmap";
    
    Command::new(cmd)
            .arg(layout)
            .spawn()
            .expect("Failed to execute process");
}


fn shift(current: String, all_layouts: HashMap<i32, String>) -> String {
    let current_layout = current;
    let mut index_layout: i32 = 0;
    for (index, layout) in all_layouts.iter() {
        if current_layout == String::from(layout) {
            index_layout = *index + 1;
        }
    }

    let mut shifted = all_layouts.get(&index_layout);
    if shifted == None {
        index_layout = 0;
        shifted = all_layouts.get(&index_layout);
    }

    return String::from(shifted.unwrap());
}


fn get_current_layout() -> String {
    let xkblayout_state = Path::new("./xkblayout-state"); // xkblayout state file must be in the same directory
    let out = Command::new(xkblayout_state)
                         .args(&["print", "%e"])
                         .output()
                         .expect("Failed to execute process.");
    let current_layout = match std::str::from_utf8(&out.stdout) {
        Ok(out) => out,
        Err(error) => panic!("Failed to get current layout: {}", error)
    };
    
    return String::from(current_layout);
}


fn main() {
    let config_dir = std::env::var("XDG_CONFIG_HOME")
            .map(PathBuf::from)
            .unwrap_or_else(|_| PathBuf::from(std::env::var("HOME").unwrap())
            .join(".config")
            .join("qtile"))
            .join("keyboardLayout");

    assert!(env::set_current_dir(&config_dir).is_ok());

    let my_layouts = HashMap::from([
        (0, "us".to_string()),
        (1, "es".to_string()),
        // (2, "jp".to_string()),
    ]);

    let next_layout = shift(get_current_layout(), my_layouts);
    set_keyboard(next_layout.clone());
    send_notification(next_layout.clone());
}