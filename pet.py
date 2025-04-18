class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger -= 3
        print(f"\n{self.name} has eaten.")
        if self.hunger < 0:
            self.hunger = 0    
        self.happiness += 1        
        if self.happiness > 10:
            self.happiness = 10   
        
    def sleep(self):
        self.energy += 5
        print(f"{self.name} has slept.")
        if self.energy > 10:
            self.energy = 10

    def play(self):
        self.energy -= 2
        self.hunger -= 1
        self.happiness += 2
        print(f"{self.name} has played.")

    def train(self, trick):
        self.tricks.append(trick)

    def show_tricks(self):
        print(f"\n{self.name} tricks:\n\t{"\n\t".join(self.tricks) if self.tricks else 'no tricks'}")

    def get_status(self):
        print(f"{self.name}'s status:")
        print(f"\tHunger: {self.hunger}")
        print(f"\tEnergy: {self.energy}")
        print(f"\tHappiness: {self.happiness}")
        