import random

def generate_lotto_sets(num_sets, num_numbers, max_number):
    """
    Generates multiple sets of unique lottery numbers.

    Args:
        num_sets: The number of sets to generate.
        num_numbers: The number of numbers in each set.
        max_number: The maximum number that can be selected.

    Returns:
        A list of lists, where each inner list contains a set of unique lottery numbers.
        Returns None if it's impossible to generate the requested sets (e.g., asking for more numbers than available).
    """

    if num_numbers > max_number:
        return None

    lotto_sets = []
    for _ in range(num_sets):
        set_numbers = random.sample(range(1, max_number + 1), num_numbers)
        lotto_sets.append(sorted(set_numbers))  # sort for readability

    return lotto_sets

# Generate 5 sets of 6 numbers from 1 to 45
lotto_results = generate_lotto_sets(5, 6, 45)

if lotto_results:
    for i, lotto_set in enumerate(lotto_results):
        print(f"Set {i+1}: {lotto_set}")
else:
    print("It's impossible to generate the requested sets with the given parameters.")
