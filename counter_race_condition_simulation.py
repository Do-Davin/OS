# Problem 3 (A)
GREEN = "\033[92m"
RESET = "\033[0m"

# Shared variable
counter = 10

# Define all operations as functions
def A1():
    global R0_A, counter
    R0_A = counter
    R0_A += 1  # ADDC(R0, 1, R0)

def A2():
    global counter, R0_A
    counter = R0_A

def B1():
    global R0_B, counter
    R0_B = counter
    R0_B += 2  # ADDC(R0, 2, R0)

def B2():
    global counter, R0_B
    counter = R0_B

# Runner to simulate a given order
def run_sequence(name, sequence):
    global counter, R0_A, R0_B
    counter = 10
    R0_A = 0
    R0_B = 0
    steps = {
        'A1': A1,
        'A2': A2,
        'B1': B1,
        'B2': B2
    }
    print(f"\n{name}:")
    for step in sequence:
        steps[step]()  # Run the function (A1, A2, B1, B2)
        print(f"{step} → counter = {counter}")
    print(GREEN + f"Final counter = {counter}" + RESET)

# List of 6 sequences from the problem
sequences = {
    'A1 A2 B1 B2': ['A1', 'A2', 'B1', 'B2'],
    'A1 B1 A2 B2': ['A1', 'B1', 'A2', 'B2'],
    'A1 B1 B2 A2': ['A1', 'B1', 'B2', 'A2'],
    'B1 A1 B2 A2': ['B1', 'A1', 'B2', 'A2'],
    'B1 A1 A2 B2': ['B1', 'A1', 'A2', 'B2'],
    'B1 B2 A1 A2': ['B1', 'B2', 'A1', 'A2']
}

# Run all sequences
for name, sequence in sequences.items():
    run_sequence(name, sequence)