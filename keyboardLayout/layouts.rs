use std::process::Command;
use std::path::Path;
use std::collections::HashMap;
use std::env;
// Is a shit of code I know, but it works ;)

/*
1- hacer una lista para los layouts
2- obtener el current layout
3- shift al current layout y si no existe un siguiente layout
   volver al inicio de la lista de layouts
*/


fn send_notification(layout: String) {
    let format = format!("Keyboard Layout: {}", layout.to_uppercase());

    Command::new("notify-send")
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
    let dir = Path::new("/home/eiji/.config/qtile/keyboardLayout/"); // I don't know how to make this dynamic ;(
    assert!(env::set_current_dir(&dir).is_ok());

    let my_layouts = HashMap::from([
        (0, "us".to_string()),
        (1, "es".to_string()),
        // (2, "jp".to_string()),
    ]);

    let next_layout = shift(get_current_layout(), my_layouts);
    set_keyboard(next_layout.clone());
    send_notification(next_layout.clone());
}