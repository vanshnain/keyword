def cubes_of_even_numbers_list_comprehension(input_list):
    """Returns a list of cubes of even integers from the input list using list comprehension."""
    return [num ** 3 for num in input_list if num % 2 == 0]

# Example usage
if __name__ == "__main__":
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = cubes_of_even_numbers_list_comprehension(input_list)
    print("Cubes of even integers (list comprehension):", result)
