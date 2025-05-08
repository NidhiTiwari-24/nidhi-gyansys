# Function to calculate age after 5 years
def display_future_age(name: str, age: int):
    future_age = age + 5
    print(f"Hello {name}, you will be {future_age} years old after 5 years.")

# Function to count even and odd numbers in a list
def count_even_odd(numbers: list) -> dict:
    even_count = sum(1 for num in numbers if num % 2 == 0)
    odd_count = len(numbers) - even_count
    return {"even": even_count, "odd": odd_count}

# Example usage
if __name__ == "__main__":
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    display_future_age(name, age)

    numbers = [1, 2, 3, 4, 5, 6, 7]
    result = count_even_odd(numbers)
    print(f"Even numbers: {result['even']}, Odd numbers: {result['odd']}")
