class Retangulo:
    def __init__(self, lado_a, lado_b):
        # Atributos iniciais
        self.a = lado_a
        self.b = lado_b

    def mudar_valor(self, novo_a, novo_b):
        # Atributos que podem ser convertidos
        self.a = novo_a
        self.b = novo_b

    def retornar_lado(self):
        # Retorno
        print(f"O retângulo possui as dimensões: {self.a}m X {self.b}m")

    def area(self):
        # Produto
        return self.a * self.b
