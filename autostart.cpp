#include <iostream>

/*
#!/bin/sh

# systray battery icon
cbatticon -u 5 &
# systray volume
volumeicon &
*/

using std::cout;
using std::endl;
using std::cin;

void autostart();

int main(){
    autostart();

    return 0;
}

void autostart(){
    // systray battery icon
    system("cbatticon -u 5 &");
    // systray volume
    system("volumeicon &");

    system("notify-send 'Qtile successfully started!'");
}
