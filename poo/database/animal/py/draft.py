class Animal:
    def __init__(self, spacies: str, sound:str):
        self.spcacies: str = spacies
        self.age: int = 0
        self.sound: str = sound

    def __str__(self) -> str:
        return f"{self.spcacies}, {self.age}, {self.sound}"
    
    def ismakeSound(self) -> str:
        if self.age == 0:
            return "--"
        elif self.age == 1:
            return f"{self.sound}"
        elif self.age == 2:
            return f"{self.sound}"
        elif self.age == 3:
            return f"{self.sound}"
        return "RIP"
    
    def ageBy(self, increment: int) -> None:
        self.age += increment
        if self.age >= 4:
            self.age = 4
            print(f"warning: {self.species} morreu")
            return
        elif self.age == 0:
            return "--"
        return f"{self.age}"
        
def main():
    
main()