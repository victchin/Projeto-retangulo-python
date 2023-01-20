from Objeto_Retângulo import Retangulo
import math

while True:
    # Inserção do valor
    piso_a = float(input("Digite um lado do piso: "))
    piso_b = float(input("Digite outro lado do piso: "))

    # Intânciação e atribuição dos valores
    piso = Retangulo(piso_a, piso_b)

    # Nova Inserção, instânciação e atribuição de valores
    # Inserção do valor
    azulejo_a = float(input("Digite o lado do azulejo: "))
    azulejo_b = float(input("Digite outro lado do azulejo: "))

    # Intânciação e atribuição de valores
    azulejo = Retangulo(azulejo_a, azulejo_b)

    # Função de retorno do produto dos valores
    area_piso = piso.area()
    area_azulejo = azulejo.area()

    # Variável que vai conter o quociente da
    # quantidade de azulejos necessários
    qntd_azulejo = area_piso / area_azulejo

    # Quantidade máxima de azulejos
    if area_piso % area_azulejo == 0:
        print(f"A quantidade exata de azulejos para preencher o piso é de {qntd_azulejo}")

    # Quantidade mínima de azulejos
    else:
        print(f"A quantidade mínima de azulejos para preencher o piso é de {math.ceil(qntd_azulejo)}")
