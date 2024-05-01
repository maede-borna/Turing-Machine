class Transition:
    def __init__(self, current_state, input_symbol, next_state, write_symbol, move):
        self.current_state = current_state
        self.input_symbol = input_symbol
        self.next_state = next_state
        self.write_symbol = write_symbol
        self.move = move


class TuringMachine:
    def __init__(self, states, initial_state, final_states, input_alphabet, tape_alphabet, transitions):
        self.states = states
        self.initial_state = initial_state
        self.final_states = final_states
        self.input_alphabet = input_alphabet
        self.tape_alphabet = tape_alphabet
        self.transitions = transitions

    def accept(self, string):
        cur_state = self.initial_state
        tape = self.makeTape(string)
        tape_head = 2                 

        while cur_state not in self.final_states:
            self.show_tape(tape, cur_state, tape_head)
            if tape_head < 0:
                tape.insert(0, "#")
            elif tape_head >= len(tape):
                tape.append("#")

            cur_symbol = tape[tape_head]
            transition = self.find_transition(cur_state, cur_symbol)
            if transition is not None:
                tape[tape_head] = transition.write_symbol
                if transition.move == "L":
                    tape_head += -1
                else:
                    tape_head += 1
                cur_state = transition.next_state
            else:
                return False

        return True if cur_state in final_states else False

    def makeTape(self, string):
        tape = ["#"] * (len(string) + 6)
        index = 2
        for symbol in string:
            tape[index] = symbol
            index += 1
        return tape

    def find_transition(self, cur_state, cur_symbol):
        temp = []
        for i in range(len(self.transitions)):
            if str(transitions[i].current_state) == str(cur_state) and str(transitions[i].input_symbol) == str(cur_symbol):
                temp.append(transitions[i])

        if len(temp) != 0:
            return temp[0]
        else:
            return None

    def show_tape(self, tape, cur_state, tape_head):
        print(f"tape: {tape} , ", end=" ")
        print(f"current state: {cur_state} , ", end=" ")
        print(f"tape head: {tape_head} , ", end=" ")

        transition = self.find_transition(cur_state, tape[tape_head])

        if transition is not None:
            cur_symbol = transition.input_symbol
            next_state = transition.next_state
            write_symbol = transition.write_symbol
            move = transition.move
            print(
                f"transition: ({transition.current_state}, {cur_symbol}) = ({next_state}, {write_symbol}, {move})")
        else:
            print("no transition.")

        print()


states = input("States: ").split(" ")
initial_state = input("Initial state: ")
final_states = input("Final states: ").split(" ")
input_alphabet = input("Input alphabet: ").split(" ")
tape_alphabet = input("Tape alphabet: ").split(" ")
number_of_transitions = int(input("Number of transitions: "))
print()
transitions = []

for i in range(number_of_transitions):
    print(f"transition {i+1}:")
    current_state = input("current state: ")
    input_symbol = input("input symbol: ")
    next_state = input("next state: ")
    write_symbol = input("write symbol: ")
    move = input("move direction (L/R): ")
    transition = {"current_state":current_state, "input_symbol":input_symbol
                  ,"next_state":next_state, "write_symbol":write_symbol
                  ,"move":move}
    transition = Transition(current_state,input_symbol,next_state,write_symbol,move)
    transitions.append(transition)
    print()

turing_machine = TuringMachine(states, initial_state, final_states, input_alphabet, tape_alphabet, transitions)

while True:
    # end: enter "-1"
    string = input("String: ")
    if string != "-1":
        if turing_machine.accept(string):
            print("Accepted.\n")
        else:
            print("Rejected.\n")
    else:
        break


