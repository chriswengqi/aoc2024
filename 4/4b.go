package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var grid []string

	for scanner.Scan() {
		grid = append(grid, strings.TrimSpace(scanner.Text()))
	}

	n, m := len(grid), len(grid[0])
	words := map[string]bool{"MAS": true, "SAM": true}
	ans := 0

	for i := 0; i < n-2; i++ {
		for j := 0; j < m-2; j++ {
			left := string(grid[i][j]) + string(grid[i+1][j+1]) + string(grid[i+2][j+2])
			right := string(grid[i][j+2]) + string(grid[i+1][j+1]) + string(grid[i+2][j])
			if words[left] && words[right] {
				ans++
			}
		}
	}

	fmt.Println(ans)
}