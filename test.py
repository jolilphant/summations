import random
import subprocess

def test_while_summation():
    # Set up the test input (number to sum up to)
    test_input = str(random.randint(100))
    
    # Expected output (sum of numbers from 1 to 5)
    expected_output = str(n*n/2)

    # Run the student's script and capture output
    # Make sure this path matches the path where student scripts are stored
    result = subprocess.run(
        ['python3', 'while_summation.py'],  # Adjust this to the specific student script file
        input=test_input,
        text=True,
        capture_output=True
    )

    # Assert if the output is as expected
    assert result.stdout.strip() == expected_output.strip(), f"Expected {expected_output}, but got {result.stdout.strip()}"

def test_for_summation():
    # Set up the test input (number to sum up to)
    test_input = str(random.randint(100))
    
    # Expected output (sum of numbers from 1 to 5)
    expected_output = str(n*n/2)

    # Run the student's script and capture output
    # Make sure this path matches the path where student scripts are stored
    result = subprocess.run(
        ['python3', 'for_summation.py'],  # Adjust this to the specific student script file
        input=test_input,
        text=True,
        capture_output=True
    )

    # Assert if the output is as expected
    assert result.stdout.strip() == expected_output.strip(), f"Expected {expected_output}, but got {result.stdout.strip()}"
