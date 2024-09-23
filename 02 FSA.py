class FiniteStateAutomaton:
    def __init__(self):

        self.current_state = "q0"
    
    def transition(self, char):
        
        if self.current_state == "q0":
            if char == "a":
                self.current_state = "q1"
            else:
                self.current_state = "q0"
        elif self.current_state == "q1":
            if char == "b":
                self.current_state = "q2"
            elif char == "a":
                self.current_state = "q1"
            else:
                self.current_state = "q0"
        elif self.current_state == "q2":
            
            self.current_state = "q0" if char != "a" else "q1"

    def is_accepting(self):
        
        return self.current_state == "q2"
    
    def reset(self):
        
        self.current_state = "q0"
    
    def process_string(self, input_string):
        
        self.reset()
        for char in input_string:
            self.transition(char)
        return self.is_accepting()

fsa = FiniteStateAutomaton()

test_strings = [
    "aab",    
    "abab",   
    "abc",    
    "ab",     
    "ba",     
    "cabab",  
]

for s in test_strings:
    if fsa.process_string(s):
        print(f"'{s}' is accepted by the automaton (ends with 'ab').")
    else:
        print(f"'{s}' is rejected by the automaton.")
