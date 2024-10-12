import time
from datetime import datetime


# Function to multiply two numbers
def multiply(a, b):
    return a * b


# Function to add two numbers
def add(x, y):
    return x + y

initial_time =datetime.now()
print(initial_time)
# Function to perform operations and measure time for each
def perform_operations(a,b,c):
     # Record the start time for multiplication
    start_time_multiply = time.time()

    # Perform multiplication
    multiplication_result = multiply(a, b)

    # Record the end time for multiplication
    end_time_multiply = time.time()

    # Calculate the duration for multiplication
    duration_multiply = end_time_multiply - start_time_multiply

    # Record the start time for addition
    start_time_add = time.time()

    # Perform addition
    addition_result = add(multiplication_result, c)

    # Record the end time for addition
    end_time_add = time.time()

    # Calculate the duration for addition
    duration_add = end_time_add - start_time_add

    # Print the results
    print("Multiplication Result:", multiplication_result)
    print("Time taken for multiplication:", duration_multiply, "seconds")
    #
    print("Addition Result:", addition_result)
    print("Time taken for addition:", duration_add, "seconds")


# Main function to call the operations
def main():
    a = 5
    b = 10
    c = 20
    perform_operations(a, b, c)


# Run the main function
if __name__ == "__main__":
    main()