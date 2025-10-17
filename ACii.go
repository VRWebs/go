package main

import "fmt"

func main() {
	var s string
	fmt.Print("Enter a string (no spaces): ")
	fmt.Scan(&s) // word only
	for i := 0; i < len(s); i++ {
		fmt.Printf("%c = %d\n", s[i], s[i])
	}
}
