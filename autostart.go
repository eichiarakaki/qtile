/*
compile after making changes
*/

package main

import (
	"fmt"
	"os/exec"
	"time"
)

type Exec struct {
	command  string
	argument []string
}

func get_time(hour, min *int) {
	*hour = time.Now().Hour()
	*min = time.Now().Minute()
}

func (cmd Exec) executor() {
	for _, e := range cmd.argument {
		err := exec.Command(cmd.command, e).Run()
		if err != nil {
			fmt.Println(err)
		}
	}
}

func main() {

	eww_daemon := Exec{
		command:  "~/bin/eww",
		argument: []string{"daemon"},
	}
	picom := Exec{
		command:  "picom",
		argument: []string{"&"},
	}
	udiskie := Exec{
		command:  "udiskie",
		argument: []string{"&"},
	}
	feh := Exec{
		command:  "~/.fehbg",
		argument: []string{"&"},
	}
	dunst := Exec{
		command:  "dunst",
		argument: []string{"&"},
	}

	var current_hour, current_minute int
	get_time(&current_hour, &current_minute)

	if current_hour >= 17 && current_minute >= 0 {
		redshift := Exec{
			command:  "redshift",
			argument: []string{"-C", "4000"},
		}
		brightness := Exec{
			command:  "brightnessctl",
			argument: []string{"set", "30%"},
		}

		redshift.executor()
		brightness.executor()

	} else {
		redshift := Exec{
			command:  "redshift",
			argument: []string{"-x"},
		}
		brightness := Exec{
			command:  "brightnessctl",
			argument: []string{"set", "80%"},
		}

		redshift.executor()
		brightness.executor()
	}

	eww_daemon.executor()
	picom.executor()
	udiskie.executor()
	feh.executor()
	dunst.executor()

}
