class Carro:
    def __init__(self, pas: int, km: int, gas: int):
        self.pas: int = 0
        self.km: int = 0
        self.passMax: int = 2
        self.gas: int = 0
        self.gasMax: int = 100

    def enter(self):
        self.pas += 1
        if self.pas > self.passMax:
            self.pas = self.passMax
            print("fail: limite de pessoas atingido")
            return
        
    def leave(self):
        self.pas -= 1
        if self.pas < 0:
            self.pas = 0
            print("fail: nao ha ninguem no carro")

    def gasEnter(self, increment: int) -> int:
        self.gas += increment
        if self.gas > self.gasMax:
            self.gas = self.gasMax
    
    def distance(self, distance: int) -> None:
        if self.pas == 0:
            print("fail: nao ha ninguem no carro")
        elif self.gas == 0:
            print("fail: tanque vazio")
        elif self.gas < distance:
            self.km += self.gas
            print(f"fail: tanque vazio apos andar {self.gas} km")
            self.gas = 0
        else:
            self.km += distance
            self.gas -= distance
    
    def __str__(self) -> str:
        return f"pass: {self.pas}, gas: {self.gas}, km: {self.km}"
    
def main():

    carro: Carro = Carro("", "", "")
    while True:

        line: str = input()
        print("$" +  line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(carro)
        elif args[0] == "enter":
            carro.enter()
        elif args[0] == "leave":
            carro.leave()
        elif args[0] == "fuel":
            increment: int = int(args[1])
            carro.gasEnter(increment)
        elif args[0] == "drive":
             increment: int = int(args[1])
             carro.distance(increment)

main()