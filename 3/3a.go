package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
)

func main() {
	var ans int

	pattern := regexp.MustCompile(`mul\((-?\d+),(-?\d+)\)`)

	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		line := scanner.Text()

		matches := pattern.FindAllStringSubmatch(line, -1)
		for _, match := range matches {
			x, _ := strconv.Atoi(match[1])
			y, _ := strconv.Atoi(match[2])

			ans += x * y
		}
	}

	fmt.Println(ans)

}