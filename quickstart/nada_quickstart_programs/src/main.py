from nada_dsl import *

def nada_main():
    # Define two parties
    party1 = Party(name="Alice")
    party2 = Party(name="Bob")

    # Input secret integers from Party1 and Party2
    x = SecretInteger(Input(name="InputX", party=party1))
    y = SecretInteger(Input(name="InputY", party=party2))

    # Perform the computation: multiplication of the two secret integers
    result = x * y

    # Output the result to Party2
    return [Output(result, "result_output", party2)]

# Create a new nada program based on the reference program
if __name__ == "__main__":
    nada_main()
