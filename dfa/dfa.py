class DFA:
    def __init__(self, num_states, transitions, initial_state, accepting_states):
        self.transitions = transitions
        self.initial_state = initial_state
        self.accepting_states = accepting_states

    def accepts(self, input_string):
        state = self.initial_state
        for c in input_string:
            state = self.transitions[state][c]
        return state in self.accepting_states


def main():
    num_states = int(input("Enter the number of states in the DFA: "))
    transitions = {state: {'0': 0, '1': 0} for state in range(num_states)}

    for state in transitions:
        transitions[state]['0'] = int(input(f"Enter state to transition to on '0' from state {state}: "))
        transitions[state]['1'] = int(input(f"Enter state to transition to on '1' from state {state}: "))

    initial_state = int(input("Enter the initial state of the DFA: "))
    num_accepting = int(input("Enter the number of accepting states: "))
    accepting_states = {int(input("Enter an accepting state: ")) for _ in range(num_accepting)}

    dfa = DFA(num_states, transitions, initial_state, accepting_states)

    num_inputs = int(input("How many input strings would you like to check? "))
    for i in range(num_inputs):
        input_string = input(f"Enter input string {i + 1}: ")
        if dfa.accepts(input_string):
            print(f"The input string '{input_string}' is accepted by the DFA.")
        else:
            print(f"The input string '{input_string}' is not accepted by the DFA.")


# Only call main if this script is run directly
if __name__ == "__main__":
    main()
