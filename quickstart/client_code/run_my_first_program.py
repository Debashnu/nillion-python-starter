from nada_dsl import *

def nada_main():
    # Define parties
    party1 = Party(name="FactorialProvider")
    party2 = Party(name="FactorialCalculator")

    # Input secret integer for factorial calculation
    n = SecretInteger(Input(name="Number", party=party1))

    # Initialize result as 1 (factorial base case)
    result = SecretInteger(1)

    # Loop to compute factorial using iterative multiplication
    for i in range(1, n + 1):
        result = result * SecretInteger(i)

    # Output the factorial result to the factorial calculator party
    return [Output(result, "Factorial", party2)]

# Create a new nada program to calculate factorial
if __name__ == "__main__":
    nada_main()

