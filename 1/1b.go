package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	var left []int
	right := make(map[int]int)
	scanner := bufio.NewScanner(os.Stdin)

	for scanner.Scan() {
		line := strings.TrimSpace(scanner.Text())
		parts := strings.Split(line, "   ")
		a, err1 := strconv.Atoi(parts[0])
		b, err2 := strconv.Atoi(parts[1])
		if err1 != nil || err2 != nil {
			continue
		}
		left = append(left, a)
		right[b] += 1
	}

	sum := 0
	for i := 0; i < len(left); i++ {
		sum += left[i] * right[left[i]]
	}

	fmt.Println(sum)
}