
# Python Program to Implement the 7 Logic Gates

print("LOGIC GATES SIMULATOR")
print("---------------------")

# Input two binary values
A = int(input("Enter input A (0 or 1): "))
B = int(input("Enter input B (0 or 1): "))

# Check inputs
if A not in [0, 1] or B not in [0, 1]:
    print("Invalid input! Enter only 0 or 1.")
else:
    # Implement the 7 logic gates
    AND = A & B
    OR = A | B
    NOT_A = 1 - A
    NAND = 1 - AND
    NOR = 1 - OR
    XOR = A ^ B
    XNOR = 1 - XOR

    # Display results
    print("\nRESULTS")
    print("-------")
    print("AND  =", AND)
    print("OR   =", OR)
    print("NOT A=", NOT_A)
    print("NAND =", NAND)
    print("NOR  =", NOR)
    print("XOR  =", XOR)
    print("XNOR =", XNOR)
