package main

import "fmt"

type Student struct {
	id          int
	name, class string
}

func main() {
	s := Student{101, "A", "B.Sc CS"}
	fmt.Println("UID:", s.id, "Name:", s.name, "Class:", s.class)
}
