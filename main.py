class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo == "mago":
            ataque = "usando magia"
        elif self.tipo == "guerreiro":
            ataque = "usando espada"
        elif self.tipo == "monge":
            ataque = "usando artes marciais"
        elif self.tipo == "ninja":
            ataque = "usando shuriken"
        else:
            ataque = "usando um ataque desconhecido"
        
        print(f"O {self.tipo} atacou {ataque}")

# Aqui chamamoa a função
heroi1 = Heroi("Arthur", 30, "guerreiro")
heroi1.atacar()

heroi2 = Heroi("Merlin", 150, "mago")
heroi2.atacar()

heroi3 = Heroi("Bruce", 25, "monge")
heroi3.atacar()

heroi4 = Heroi("Naruto", 20, "ninja")
heroi4.atacar()

heroi5 = Heroi("Outro heroi", 20, "guru")
heroi5.atacar()
