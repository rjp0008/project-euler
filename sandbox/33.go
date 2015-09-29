package main

import (
	"fmt"
)

func IsSimplified(numerator int, denominator int) bool {
	if numerator%10 == 0 || denominator%10 == 0 || numerator == denominator || numerator > denominator {
		return false
	}
	value := float64(numerator) / float64(denominator)
	if float64(numerator/10)/float64(denominator/10) == value {
		return true
	}
	if float64(numerator%10)/float64(denominator/10) == value {
		return true
	}
	if float64(numerator%10)/float64(denominator%10) == value {
		return true
	}
	if float64(numerator/10)/float64(denominator%10) == value {
		return true
	}
	return false
}

func main() {
	for i := 10; i < 100; i++ {
		for j := 10; j < 100; j++ {
			if IsSimplified(i, j) {
				fmt.Print(i)
				fmt.Print(" ")
				fmt.Println(j)
			}
		}
	}
}
