package test

import "core:fmt"
print :: fmt.println

main :: proc() {

	print(find_consecutive_numbers_02([]int{2, 4, 5, 8, 9, 10, 11, 12, 24, 14, 8}, 4))
	// OUTPUT:
	// [8, 9, 10, 11]

}


find_consecutive_numbers_02 :: proc(l: []int, num: int) -> []int {
	failed: bool

	for i in 0 ..< len(l) - num + 1 {
		for j in i + 1 ..< i + num {
			if l[j - 1] == l[j] - 1 {
				failed = false
			} else {
				failed = true
				break
			}
		}

		if failed == false {
			return l[i:i + num]
		}
	}
	return l[0:0]
}

/*
def find_consecutive_numbers_02(l, num):

    consecutive_nums = []
    for i in range(0, len(l) - num + 1):
        for j in range(i + 1, i + num):
            if l[j - 1] == l[j] - 1:
                failed = False
            else:
                failed = True
                break

        if failed == False:
            consecutive_nums.append(l[i: i + num])
            return consecutive_nums

    return consecutive_nums
*/
