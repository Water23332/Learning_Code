package main

import "fmt"

func main() {
	var msutafa int8
	msutafa = 50
	for msutafa > 40 {
		fmt.Println("Hello World")
		msutafa += 10
		fmt.Println("Msutafa is", msutafa)
	}
}
