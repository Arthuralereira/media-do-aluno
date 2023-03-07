barra = '-' * 25

def iniciar() -> None | ValueError:
    while True:
        try:
            quantidade_de_notas = int(input('Quantidade de notas:'))
            break
        
        except ValueError:
            print('Inválido. Tente novamente.')
    
    nome_do_aluno = input('Nome do aluno: ').title()
    notas_do_aluno = []
    print(barra)

    for i, _ in enumerate(range(quantidade_de_notas), start=1):

        while True:
            try:
                nota = float(input(f'{i}º nota: ').replace(',', '.'))

                if nota <= 10.0:
                    notas_do_aluno.append(nota)
                    break

                else:
                    print('Nota inválida.')
            
            except ValueError:
                print('Inválido. Tente novamente.')

    media = sum(notas_do_aluno) / quantidade_de_notas
    print(f'{barra}\nMedia: {media}')           
