import copy
from random import randrange


def find_consecutive_numbers(l, num):

    consecutive_nums = []
    for i in range(len(l) - num + 1):
        if all(l[j] == l[j+1] - 1 for j in range(i, i + num - 1)):
            consecutive_nums.append(l[i:i+num])
    return consecutive_nums


def generate_random_list():
    local_array = []
    for _ in range(0, randrange(20, 40)):
        local_array.append(randrange(1, 40))

    return local_array


def longestConsecutive(l: list[int]) -> int:
    _l = copy.deepcopy(l)
    _l.sort()
    print("sorted list: ", _l)

    stretch_array = []
    current_stretch = 1
    max_len = 0

    for i in range(1, len(_l) - 1):
        if _l[i] == _l[i - 1] + 1:
            current_stretch += 1
            if current_stretch > max_len:
                max_len = current_stretch

        else:
            current_stretch = 1

    stretch_array = find_consecutive_numbers(_l, max_len)
    print("stretch_array: ", stretch_array)
    return max_len


def main() -> None:

    for _ in range(10):
        some_list = generate_random_list()
        print("generated list: ", some_list)
        print(longestConsecutive(some_list))
        print("")


if __name__ == '__main__':
    main()
