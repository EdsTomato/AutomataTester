from nfa import NFA  # Import the NFA class


def run_tests():
    # Define a simple test NFA (no user input here)
    test_nfa = {
        0: {'0': {0, 1}, '1': {0}, 'ε': set()},
        1: {'0': {2}, '1': set(), 'ε': set()},
        2: {'0': {2}, '1': {3}, 'ε': set()},
        3: {'0': {3}, '1': {3}, 'ε': set()}
    }
    initial_state = 0
    accepting_states = {3}

    # Create an NFA instance
    nfa = NFA(num_states=len(test_nfa), transitions=test_nfa, initial_state=initial_state,
              accepting_states=accepting_states)

    # List of test cases: (input_string, expected_result)
    test_cases = [
        ('01', False),   # Ends in state 1, not accepting
        ('001', True),   # Can reach accepting state 3
        ('000', False),  # Ends in state 2, not accepting
        ('0001', True),  # Ends in state 3, accepting
        ('', False),     # Empty string, stays in initial state 0, not accepting
        ('1', False)     # Remains in state 0, not accepting
    ]

    # Loop over test cases
    for i, (input_string, expected) in enumerate(test_cases):
        result = nfa.accepts(input_string)  # Use the accepts method of the NFA class
        assert result == expected, f"Test case {i + 1} failed: input '{input_string}'"
        print(f"Test case {i + 1} passed: input '{input_string}'")

# Run the tests
if __name__ == "__main__":
    run_tests()
