def olhar_notas(notas):
    print("Qual aluno você deseja ver a nota")
    for i in range(len(notas)):
        print(notas[i][0])
    aluno = input("Digite o nome de um dos alunos a cima: ")
    for i in range(len(notas)):
        if aluno in notas[i]:
            posição = i
    print(notas[posição][1:])
    return posição

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivo = lista[0]
        listae = []
        listad = []
        for i in lista[1:]:
            if i > pivo:
                break
            listae.append(i)
        for i in lista[1:]:
            if i <= pivo:
                break
            listad.append(i)
        return quick_sort(listae) + [pivo] + quick_sort(listad)

notas = [['Jonatas', 10, 9, 5.5, 7],['Pedro', 7, 8.5, 9, 7.5],['Lucas', 10, 10, 7, 9]]

ligado = True
while ligado:
    print("""O que você desejá fazer agora?
          [ 1 ] Olhar as notas
          [ 2 ] alterar as notas
          [ 3 ] adicionar notas
          [ 4 ] Sair""")
    opcao = int(input("Digite um número: "))
    if opcao == 1:
        posição = olhar_notas(notas)
        resposta = int(input("Para ordenar as notas desse aluno digite 1, para seguir sem ordenar digete 2: "))
        if resposta == 1:
            notas[posição] = [notas[posição][0]] + quick_sort(notas[posição][1:])
            print(f"Notas ordenadas: {notas[posição][1:]}")
    elif opcao == 2:
        posição = olhar_notas(notas)
        alterar = int(input("Qual das 4 notas você deseja alterar (1 a 4): "))
        valor = float(input("Digite o valor da nova nota: "))
        notas[posição][alterar] = valor
        print(f"Notas alteradas: {notas[posição][1:]}")
    elif opcao == 3:
        posição = olhar_notas(notas)
        valor = float(input("Digite o valor da nova nota: "))
        notas[posição].append(valor)
        print(f"Notas adicionadas: {notas[posição][1:]}")
    elif opcao == 4:
        print("Programa finalizado")
        ligado = False
    else:
        print("Opção inválida")
        pass