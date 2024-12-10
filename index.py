def nivelDoHeroi():
    try:
        exp = int(input("Escreva a quantidade de experiência: "))  # Converte para inteiro
        if exp <= 1000:
            print("Ferro")
        elif exp <= 2000:
            print("Bronze")
        elif exp <= 5000:
            print("Prata")
        elif exp <= 7000:
            print("Ouro")
        elif exp <= 8000:
            print("Platina")
        elif exp <= 9000:
            print("Ascendente")
        elif exp <= 10000:
            print("Imortal")
        elif exp > 10000:
            print("Radiante")
    except ValueError:
        print("Por favor, digite um número válido.")  # Trata entradas inválidas

nivelDoHeroi()
