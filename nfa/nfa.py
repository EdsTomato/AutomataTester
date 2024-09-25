class NFA:
    def __init__(self, num_states, transitions, initial_state, accepting_states):
        self.transitions = transitions
        self.initial_state = initial_state
        self.accepting_states = accepting_states

    def epsilon_closure(self, states):
        # Compute epsilon closure of given set of states
        closure = set(states)
        stack = list(states)
        while stack:
            state = stack.pop()
            if 'ε' in self.transitions[state]:
                new_states = self.transitions[state]['ε'] - closure
                closure.update(new_states)
                stack.extend(new_states)
        return closure

    def accepts(self, input_string, debug=False):
        current_states = self.epsilon_closure({self.initial_state})
        if debug:
            print(f"Initial states: {current_states}")

        for c in input_string:
            next_states = set()
            if debug:
                print(f"\nProcessing symbol: '{c}'")
            for state in current_states:
                if c in self.transitions[state]:
                    new_states = self.transitions[state][c]
                    if debug:
                        print(f"From state {state}, transitioning on '{c}' to {new_states}")
                    next_states.update(self.epsilon_closure(new_states))

            current_states = next_states
            if debug:
                print(f"Current states after processing '{c}': {current_states}")

        accepted = any(state in self.accepting_states for state in current_states)
        if debug:
            print(f"Final states: {current_states}. Accepted: {accepted}")
        return accepted


def main():
    num_states = int(input("Enter the number of states in the NFA: "))
    transitions = {state: {'0': set(), '1': set(), 'ε': set()} for state in range(num_states)}

    print("Enter transitions for each state (multiple transitions: 2, 3 | no transition: -1):")
    for state in range(num_states):
        for symbol in ['0', '1', 'ε']:
            next_states = input(
                f"Enter states to transition to on '{symbol}' from state {state}: ").strip().split(
                ',')
            for s in next_states:
                if s.strip() != '-1':
                    transitions[state][symbol].add(int(s.strip()))

    initial_state = int(input("Enter the initial state of the NFA: "))
    num_accepting = int(input("Enter the number of accepting states: "))
    accepting_states = {int(input("Enter an accepting state: ")) for _ in range(num_accepting)}

    nfa = NFA(num_states, transitions, initial_state, accepting_states)

    num_inputs = int(input("How many input strings would you like to check? "))
    debug_mode = input("Enable debug mode? (y/n): ").strip().lower()

    debug_mode = debug_mode == 'y'

    for i in range(num_inputs):
        input_string = input(f"Enter input string {i + 1}: ")
        if nfa.accepts(input_string, debug=debug_mode):
            print(f"The input string '{input_string}' is accepted by the NFA.")
        else:
            print(f"The input string '{input_string}' is not accepted by the NFA.")


# Only call main if this script is run directly
if __name__ == "__main__":
    main()
