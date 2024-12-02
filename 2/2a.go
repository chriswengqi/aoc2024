package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func checkValid(lst []int) bool {
	inc := lst[1] > lst[0]
	valid := true

	for i := 1; i < len(lst); i++ {
		if (inc && (lst[i] <= lst[i-1] || lst[i] > lst[i-1]+3)) || (!inc && (lst[i] >= lst[i-1] || lst[i] < lst[i-1]-3)) {
			valid = false
			break
		}
	}

	return valid
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	ans := 0

	for scanner.Scan() {
		line := scanner.Text()
		parts := strings.Fields(line)
		var lst []int

		for _, part := range parts {
			num, err := strconv.Atoi(part)
			if err != nil {
				fmt.Println("Error converting input to integer:", err)
				return
			}
			lst = append(lst, num)
		}

		if len(lst) >= 2 && checkValid(lst) {
			ans++
		}
	}

	fmt.Println(ans)
}