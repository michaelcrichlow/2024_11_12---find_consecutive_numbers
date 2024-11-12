def find_consecutive_numbers(l, num):
  """
  Finds consecutive numbers in a list.

  Args:
    l: The list of integers.
    num: The length of consecutive numbers to find.

  Returns:
    A list of consecutive numbers, or an empty list if none found.
  """

  consecutive_nums = []
  for i in range(len(l) - num + 1):
    if all(l[j] == l[j+1] - 1 for j in range(i, i + num - 1)):
      consecutive_nums.append(l[i:i+num])
  return consecutive_nums

# Example usage:
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = 3

result = find_consecutive_numbers(l, num)
print(result)  # Output: [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9]]
