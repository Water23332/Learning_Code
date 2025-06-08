package main

import (
	"github.com/mappu/miqt"
)

func main() {
	app := miqt.NewApplication()

	window := miqt.NewMainWindow()
	window.SetTitle("Hello, miqt!")
	window.SetFixedSize(300, 200)

	label := miqt.NewLabel("Hello, World!")
	window.SetCentralWidget(label)

	window.Show()

	app.Exec()
}
