class Calculadora:
    def __init__(self,  batteryMax: int):
        self.batteryMax: int = batteryMax
        self.battery: int  = 0
        self.display: float = 0.0
        
    def __str__(self) -> str:
        return f"display = {self.display:.2f}, battery = {self.battery}"
    
    def charge(self, increment: int) -> None:
        self.battery += increment
        if self.battery > self.batteryMax:
            self.battery = self.batteryMax

    def sum(self, a:float, b:float) -> None:
        if self.battery == 0:
            print("fail: bateria insuficiente")
        else:
            self.display = a + b
            self.battery -= 1

    def div(self, den: float, num: float) -> None:
        if self.battery == 0:
            print("fail: bateria insuficiente")
        else:
            self.battery -= 1
            if den == 0 or num == 0:
                print("fail: divisao por zero")
            else:
                self.display = den / num
                
def main():

    calculadora: Calculadora = None
    while True:

        line: str = input()
        print("$" +  line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "init":
            batteryMax: int = int(args[1])
            calculadora = Calculadora(batteryMax)
        elif args[0] == "show":
            print(calculadora)
        elif args[0] == "charge":
            increment: int = int(args[1])
            calculadora.charge(increment)
        elif args[0] == "sum":
            a: float = float(args[1])
            b: float = float(args[2])
            calculadora.sum(a,b)
        elif args[0] == "div":
            den: float = float(args[1])
            num: float = float(args[2])
            calculadora.div(den,num)

main()