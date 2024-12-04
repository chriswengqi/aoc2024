package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

var (
	directions = [][2]int{
		{0, 1}, {1, 1}, {1, 0}, {1, -1},
		{0, -1}, {-1, -1}, {-1, 0}, {-1, 1},
	}
	word = "XMAS"
)

func search(idx, x, y, dx, dy int, grid []string, n, m int) int {
	if x < 0 || x >= n || y < 0 || y >= m || grid[x][y] != word[idx] {
		return 0
	}
	if idx == len(word)-1 {
		return 1
	}
	return search(idx+1, x+dx, y+dy, dx, dy, grid, n, m)
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var grid []string

	for scanner.Scan() {
		grid = append(grid, strings.TrimSpace(scanner.Text()))
	}

	n, m := len(grid), len(grid[0])
	ans := 0

	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			for _, dir := range directions {
				dx, dy := dir[0], dir[1]
				ans += search(0, i, j, dx, dy, grid, n, m)
			}
		}
	}

	fmt.Println(ans)
}