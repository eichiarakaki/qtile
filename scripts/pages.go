package main

import (
	"errors"
	"fmt"
	"log"
	"os"
	"os/exec"
	"path/filepath"
	"runtime"
)

func raiseError(err error) {

}

func open_page(url string) {
	var err error

	switch runtime.GOOS {
	case "linux":
		err = exec.Command("xdg-open", url).Start()
	default:
		err = fmt.Errorf("Unsupported platform.")
	}
	if err != nil {
		log.Fatal(err)
	}
}

func length_verifier(mrt bool, l int) bool {
	var err error
	if mrt {
		if len(os.Args) >= l {
			err = errors.New(usage)
		}
	} else {
		if len(os.Args) != l {
			err = errors.New(usage)
		}
	}

	if err != nil {
		log.Fatal(err)
	} else {
		return true
	}
}

func args_verifier(arg string) {

	switch arg {
	case "open":
		if length_verifier(false, 3) {

		}

	}
}

func main() {
	var err error
	ex, _ := os.Executable()
	usage := fmt.Sprintf("usage: .%s <Web>", filepath.Dir(ex))

	if len(os.Args) > 2 {
		err = errors.New(usage)
	}
	if err != nil {
		log.Fatal(err)
	}

	args_verifier(os.Args[1])

	fmt.Printf("%s\n", page)
}
