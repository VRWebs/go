package main

import "fmt"

func main() {
	var s string
	fmt.Print("Enter string (no spaces): ")
	fmt.Scan(&s)
	if len(s) == 0 {
		fmt.Println("Empty string")
		return
	}
	fmt.Println("Length:", len(s))
	fmt.Printf("First: %c\nLast: %c\n", s[0], s[len(s)-1])
}
