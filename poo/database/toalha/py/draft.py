class Towel:
    def __init__(self):
        self.color: str = ""
        self.size: str = ""
        self.wetness: int = 0

hellys = Towel()
hellys.color = "preta"
hellys.size = "g"

miguel = Towel()
miguel.color = "roxo"
miguel.size = "p"

print(miguel.color)

print("qual a cor da sua toalha") 
color = input()
tamanho = input()

towel: Towel = Towel()
towel.color = color
towel.size = tamanho

print(f"sua toalha é {towel.color} e {towel.size} ")

manel = Towel()
manel.color = "vermeio"
manel.size = "gg"