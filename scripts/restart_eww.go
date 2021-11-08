/*
def run():
    system(f'exec ~/bin/eww kill')
    system(f'exec ~/bin/eww daemon')
    sleep(2)
    system(f'exec {qtile_path}/scripts/bar_complements')

*/
/*
compile after making changes
*/

package main

import (
	"fmt"
	"log"
	"os"
	"os/exec"
	"os/user"
	"time"
)

func restart_eww() {
	user, err := user.Current()
	if err != nil {
		panic(err)
	}
	eww_route := fmt.Sprintf("%s/bin/eww", user.HomeDir)

	eww_kill_err := exec.Command(eww_route, "kill")
	err = eww_kill_err.Start()
	eww_kill_err.Wait()
	if err != nil {
		log.Fatal(err)
		os.Exit(1)
	}

	eww_daemon := exec.Command(eww_route, "daemon")
	eww_daemon.Start()
	eww_daemon.Wait()
	if err != nil {
		log.Fatal(err)
	}
	time.Sleep(1000 * time.Millisecond)

	// Haré llamar a una funcion para ejecutar este bloque
	bar_complements_route := fmt.Sprintf("%s/.config/qtile/scripts/bar_complements", user.HomeDir)
	asd := exec.Command(bar_complements_route)
	err = asd.Start()
	asd.Wait()
	if err != nil {
		log.Fatal(err)
		os.Exit(1)
	}

}

func main() {
	restart_eww()

}
