def print_fibonacci(length):
    sequence = []

    if length == 0:
        print("[]")  # Print an empty list when length is 0
        return

    if length >= 1:
        sequence.append(0)

    if length >= 2:
        sequence.append(1)

    print(sequence)  # Print the initial sequence

    while len(sequence) < length:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
        print(next_number)

# Example usage:
print_fibonacci(0)  # Should print: []
print_fibonacci(1)  # Should print: [0]
print_fibonacci(2)  # Should print: [0, 1]
print_fibonacci(8)  # Should print the Fibonacci sequence up to length 8
