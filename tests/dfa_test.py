from dfa import accepts  # Import only the function, not the main logic


def run_tests():
    # Define a simple test DFA (no user input here)
    test_dfa = {
        0: {'0': 0, '1': 1},
        1: {'0': 2, '1': 0},
        2: {'0': 1, '1': 2}
    }
    initial_state = 0
    accepting_states = {0}

    # List of test cases: (input_string, expected_result)
    test_cases = [
        ('101', False),  # Ends in state 1, not accepting
        ('010', False),  # Ends in state 0, accepting
        ('0011', True),  # Ends in state 0, accepting
        ('111', False),  # Ends in state 2, not accepting
        ('', True)  # Empty string stays in initial state 0, accepting
    ]

    # Loop over test cases
    for i, (input_string, expected) in enumerate(test_cases):
        result = accepts(test_dfa, initial_state, accepting_states, input_string)
        assert result == expected, f"Test case {i + 1} failed: input '{input_string}'"
        print(f"Test case {i + 1} passed: input '{input_string}'")


# Run the tests
if __name__ == "__main__":
    run_tests()
