// main.go
package main

import (
	"database/sql"
	"fmt"
	"log"
	"os"
	_ "github.com/mattn/go-sqlite3" // SQLite driver
)

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage: ./dicttool <word>")
		return
	}
	query := os.Args[1]

	// Open SQLite database
	db, err := sql.Open("sqlite3", "./japanese_dict.db")
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

	// Query the database
	var definition string
	err = db.QueryRow(`
		SELECT definition FROM dict 
		WHERE kanji = ? OR kana = ?`, query, query).Scan(&definition)

	if err != nil {
		if err == sql.ErrNoRows {
			fmt.Println("Word not found in database")
		} else {
			fmt.Println("Database error:", err)
		}
		return
	}

	fmt.Println(definition)
}
