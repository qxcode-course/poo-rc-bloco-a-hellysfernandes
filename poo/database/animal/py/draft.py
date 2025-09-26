class Animal:
    def __init__(self, spacies: str, sound:str):
        self.spacies: str = spacies
        self.age: int = 0
        self.sound: str = sound

    def __str__(self) -> str:
        return f"{self.spacies}:{self.age}:{self.sound}"
    
    def ageBy(self, increment: int) -> None:
        self.age += increment
        if self.age >= 4:
            self.age = 4
            print(f"warning: {self.spacies} morreu")
            return
        elif self.age == 0:
            return "--"
        return f"{self.age}"
    
    def ismakeSound(self) -> str:
        if self.age == 0:
            return "---"
        elif self.age == 1:
            return f"{self.sound}"
        elif self.age == 2:
            return f"{self.sound}"
        elif self.age == 3:
            return f"{self.sound}"
        return "RIP" 
      
def main():
    animal: Animal = Animal("", "")
    while True:

        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "init":
            spacies: str = args[1]
            sound: str = args[2]
            animal = Animal(spacies, sound)
        elif args[0] == "grow":
            increment: int = int(args[1])
            animal.ageBy(increment)
        elif args[0] == "noise":
            print(animal.ismakeSound())
        elif args[0] == "show":
            print(animal)

main()