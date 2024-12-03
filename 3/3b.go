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
	enabled := true

	pattern := regexp.MustCompile(`mul\((-?\d+),(-?\d+)\)|do\(\)|don't\(\)`)

	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		line := scanner.Text()

		matches := pattern.FindAllStringSubmatch(line, -1)
		for _, match := range matches {
			if match[1] != "" { 
				if enabled {
					x, _ := strconv.Atoi(match[1])
					y, _ := strconv.Atoi(match[2])
					ans += x * y
				}
			} else { 
				if match[0] == "do()" {
					enabled = true
				} else if match[0] == "don't()" {
					enabled = false
				}
			}
		}
	}
	
	fmt.Println(ans)
}