package main

import (
	"database/sql"
	"fmt"
	"os"

	_ "github.com/mattn/go-sqlite3"
)

func main() {
	if len(os.Args) != 2 {
		fmt.Println("Usage: go run main.go <kanji>")
		return
	}

	// Open database connection
	db, err := sql.Open("sqlite3", "./db/japanese_dict.db")
	if err != nil {
		fmt.Println("Error opening database:", err)
		return
	}
	defer db.Close()

	// Prepare the statement once for reuse
	stmt, err := db.Prepare("SELECT definition FROM dict WHERE kanji = ?")
	if err != nil {
		fmt.Println("Error preparing statement:", err)
		return
	}
	defer stmt.Close()

	// Query the database
	var definition string
	err = stmt.QueryRow(os.Args[1]).Scan(&definition)
	if err == sql.ErrNoRows {
		fmt.Printf("No definition found for kanji: %s\n", os.Args[1])
		return
	}
	if err != nil {
		fmt.Println("Error querying database:", err)
		return
	}

	fmt.Println(definition)
}