from random import choice

jogador_vitorias = 0
maq_vitorias = 0 

def Opcao_Jogador():
    #Eu posso declarar uma variável igual ao do while sem dar conflito porque são variáveis locais, então não tem problema
    esc_jogador = input("Escolha Pedra, Papel ou Tesoura: ")
    esc_jogador.lower() #Tudo vai ser transformado em minusculo
    if esc_jogador == "pedra":
        return esc_jogador #Vai retornar pedra
    elif esc_jogador == "papel":
        return esc_jogador
    elif esc_jogador == "tesoura":
        return esc_jogador
    else:
        print("Opção inválida. Tente novamente")
        Opcao_Jogador()#Aqui vai chamar a função novamente e recomeçar tudo a partir da linha 4 

def Opcao_maquina():
    esc_maquina = choice(["pedra", "papel", "tesoura"]) #Essa função choice vai escolher alguma op da lista para armazenar na variavel -> esc_maquina
    return esc_maquina

while True: 
    print("-"*30)
    esc_jogador = Opcao_Jogador()
    esc_maquina = Opcao_maquina()
    print("-"*30)

    if(esc_jogador == "pedra") and (esc_maquina == "tesoura") \
        or (esc_jogador == "papel") and (esc_maquina == "pedra")\
            or esc_jogador == "tesoura" and (esc_maquina == "papel"):
            #Jogador ganha
            print(f"Jogador escolheu {esc_jogador} e maquina escolheu {esc_maquina}"
            "Resultado: Você ganhou")
            jogador_vitorias += 1
    elif esc_jogador == esc_maquina:
        #Empate
        print(f"Jogador escolheu {esc_jogador} e maquina escolheu {esc_maquina}"
            "Resultado: Empate")
    else: 
        #Máquina ganha
        print(f"Jogador escolheu {esc_jogador} e maquina escolheu {esc_maquina}"
            "Resultado: Derrota")
        maq_vitorias += 1

    print("-"*30)
    print(f"Vitórias do jogador: {jogador_vitorias}")
    print(f"Vitórias da máquina: {maq_vitorias}")
    print("-"*30)

    esc_jogador = input("Você quer jogar novamente? ")
    if esc_jogador in ["Sim", "sim", "Sim", "s", "S"]:
        pass
    elif esc_jogador in ["NAO", "Nao", "nao", "n", "N" ]:
        break
    else:
        break
