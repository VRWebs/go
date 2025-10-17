package main

import (
	"fmt"
	"math"
)

func main() {
	var n int
	fmt.Print("Enter number: ")
	fmt.Scan(&n)
	n = int(math.Abs(float64(n)))
	if n == 0 {
		fmt.Println("Digits = 1")
		return
	}
	c := 0
	for n > 0 {
		c++
		n /= 10
	}
	fmt.Println("Digits =", c)
}
