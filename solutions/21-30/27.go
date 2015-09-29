package main

import (
	"fmt"
	"math"
)

func IsPrime(input int) bool {
	if input < 0{
		return false
	}
	if input%2 == 0 {
		return false
	}
	for i := 3; i <= int(math.Sqrt(float64(input))); i++ {
		if input%i == 0 {
			return false
		}
	}
	return true
}

func PrimeCounter(a int, b int) int {
	
	for count := 0;;count++{
		nSquared := count * count
		if !(IsPrime(nSquared + (count * a) + b)) {
			return count
		}
		
	}
}

func main() {
	a := 0
	b := 0
	max := 0
	for i := -1000; i <= 1000; i++ {
		for j := 1; j <= 1000; j++ {
			temp := PrimeCounter(i, j)
			if temp > max {
				max = temp
				a = i
				b = j
			}
		}
	}
	//fmt.Println(max)
	//fmt.Println(a)
	//fmt.Println(b)
	fmt.Println(a * b)
}
