/*
compile after making changes
*/

package main

import (
	"fmt"
	"os/exec"
	"os/user"
)

func complements(window ...string) {
	user, err := user.Current()
	if err != nil {
		panic(err)
	}
	eww_route := fmt.Sprintf("%s/bin/eww", user.HomeDir)

	for _, e := range window {
		err := exec.Command(eww_route, "open", e).Run()
		if err != nil {
			fmt.Println(err)
		}
	}
}

func main() {
	complements(
		"brightness",
		"volume",
		"battery",
		//"bar",
		//"current_time",
	)
}
