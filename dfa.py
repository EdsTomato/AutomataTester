def accepts(transitions, initial, accepting, s):
    state = initial
    for c in s:
        state = transitions[state][c]
    return state in accepting


# Wrap the user input logic in a main function
def main():
    # User-defined DFA
    num_states = int(input("Enter the number of states in the DFA: "))
    dfa = {}

    for state in range(num_states):
        dfa[state] = {}
        dfa[state]['0'] = int(input(f"Enter state to transition to on '0' from state {state}: "))
        dfa[state]['1'] = int(input(f"Enter state to transition to on '1' from state {state}: "))

    initial_state = int(input("Enter the initial state of the DFA: "))

    num_accepting = int(input("Enter the number of accepting states: "))
    accepting_states = set()
    for _ in range(num_accepting):
        accepting_state = int(input("Enter an accepting state: "))
        accepting_states.add(accepting_state)

    # Get the number of input strings
    num_inputs = int(input("How many input strings would you like to check? "))
    for i in range(1, num_inputs + 1):
        input_string = input(f"Enter input string {i}: ")
        result = accepts(dfa, initial_state, accepting_states, input_string)
        if result:
            print(f"The input string '{input_string}' is accepted by the DFA.")
        else:
            print(f"The input string '{input_string}' is not accepted by the DFA.")


# Only call main if this script is run directly
if __name__ == "__main__":
    main()