class PluralizerFSM:
    def __init__(self):
        self.state = 'start'
    def transition(self, char):
        if self.state == 'start':
            if char == 'y':
                self.state = 'y'
            elif char in 'sxz':
                self.state = 'sibilant'
            else:
                self.state = 'normal'
        elif self.state == 'y':
            self.state = 'final'
        elif self.state == 'sibilant':
            self.state = 'final'
        elif self.state == 'normal':
            self.state = 'final'
    def pluralize(self, noun):
        for char in noun:
            self.transition(char)
        if self.state == 'y':
            return noun[:-1] + 'ies'
        elif self.state == 'sibilant':
            return noun + 'es'
        else:
            return noun + 's'
fsm = PluralizerFSM()
nouns = ["cat", "dog", "bus", "box", "lady", "boy", "fox"]
for noun in nouns:
    plural = fsm.pluralize(noun)
    print(f"Singular: {noun}, Plural: {plural}")
