def sum_of_even_numbers(nums):
  total = 0
  for num in nums:
    if num % 2 == 0:
      total += num
  return total

def main():
  user_input = input("Enter a list of integers separated by spaces: ")
  numbers = [int(x) for x in user_input.split()]
  result = sum_of_even_numbers(numbers)
  print("Sum of even numbers:", result)

if __name__ == "__main__":
  main()
