class Phonebook:
    def __init__(self):
        self.entries = {}
    
    def add(self, name, number):
        self.entries[name] = number
        
    def lookup(self, name):
        return self.entries[name]
        
    def is_consistent(self):
        numbers = self.get_numbers()
        consistent = len(numbers) == len(set(numbers))
        if(consistent):
            for i, outerNumber in enumerate(numbers):
                for x, innerNumber in enumerate(numbers):
                    if(consistent & i != x):
                        consistent = (not innerNumber.startswith(outerNumber)) & (not outerNumber.startswith(innerNumber))
        return consistent 
        
    def get_names(self):
        return self.entries.keys()
        
    def get_numbers(self):
        return self.entries.values()