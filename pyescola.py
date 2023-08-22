def deletar_informacao_do_arquivo(cpf_para_deletar):
    # Abre o arquivo em modo de leitura
    with open('funcionarios.txt', 'r', encoding='utf-8') as arquivo:
        # Lê todas as linhas do arquivo e armazena em uma lista
        linhas = arquivo.readlines()

    # Inicializa uma lista para armazenar os índices das linhas a serem deletadas
    indices_para_deletar = []
    for i, linha in enumerate(linhas):
        # Verifica se a linha contém o CPF a ser deletado
        if f'CPF: {cpf_para_deletar}' in linha:
            indices_para_deletar.append(i)

    # Se não houver registros para deletar, exibe uma mensagem e retorna
    if not indices_para_deletar:
        print("Nenhum registro encontrado para deleção.")
        return

    # Adiciona os índices das linhas seguintes (Data de Nascimento e Endereço) para deletar todas as informações
    indices_para_deletar.append(indices_para_deletar[0] + 1)  # Para deletar também a linha de Data de Nascimento
    indices_para_deletar.append(indices_para_deletar[0] + 2)  # Para deletar também a linha de Endereço

    # Cria uma lista modificada sem as linhas a serem deletadas
    linhas_modificadas = [linha for i, linha in enumerate(linhas) if i not in indices_para_deletar]

    # Abre o arquivo em modo de escrita para sobrescrever com as linhas modificadas
    with open('funcionarios.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.writelines(linhas_modificadas)

# Solicita ao usuário o CPF do funcionário cujas informações devem ser deletadas
cpf_para_deletar = input("Digite o CPF do funcionário cujas informações você deseja deletar: ")
# Chama a função para deletar as informações do arquivo
deletar_informacao_do_arquivo(cpf_para_deletar)

def cadastro_de_funcionario():
    nomeF = input('Nome: ')
    data_de_nascimentoF = input('Data de nascimento: ')
    cpfF = input('CPF: ')
    enderecoF = input('Endereço: ')

    with open('funcionarios.txt', 'a', encoding='utf-8') as file:
        file.write(f'Nome: {nomeF}\nData de Nascimento: {data_de_nascimentoF}\nCPF: {cpfF}\nEndereço: {enderecoF}\n\n')

def cadastro_do_curso():
    todas_materias = input('Todas as matérias: ')
    todos_nomes_professores = input('Todos os nomes dos professores? ')
    dias_semana_todas_aulas = input('Os dias da semana de todas as aulas? ')
    todos_os_horarios = input('Todos os horários de todas as aulas? ')

    with open('cursos.txt', 'a') as file:
        file.write(f'Matérias: {todas_materias}, Professores: {todos_nomes_professores}, Dias da Semana: {dias_semana_todas_aulas}, Horários: {todos_os_horarios}\n')

def cadastro_materia():
    materia = input('Matéria: ')
    nome_professor = input('Nome do professor? ')
    dias_da_semana = input('Dias da semana?')
    horarios = input('Horários das aulas? ')

    with open('materias.txt', 'a') as file:
        file.write(f'Matéria: {materia}, Professor: {nome_professor}, Dias da Semana: {dias_da_semana}, Horários: {horarios}\n')

def cadastro_professor():
    nomep = input('Nome completo? ')
    formacao_academica = input('Formação acadêmica? ')
    cpfp = input('CPF: ')
    idadep = input('Idade: ')

    with open('professores.txt', 'a') as file:
        file.write(f'Nome: {nomep}, Formação Acadêmica: {formacao_academica}, CPF: {cpfp}, Idade: {idadep}\n')

def cadastro():
    idade = input('Idade? ')
    nome = input('Nome: ')
    data_de_nascimento = input('Data de nascimento: ')
    cpf = input('CPF: ')
    endereco = input('Endereço: ')

    with open('alunos.txt', 'a') as file:
        file.write(f'Nome: {nome}, Idade: {idade}, Data de Nascimento: {data_de_nascimento}, CPF: {cpf}, Endereço: {endereco}\n')

def menu():
    while True:
        print('Escolha: cadastro do aluno, consulta do aluno, cadastro professor,')
        print(' cadastro matéria, cadastro curso, cadastro de funcionário, deletar informacao de funcionario e sair')
        esco = input("Escolha o menu: ").lower().strip()

        if esco == 'cadastro do aluno':
            cadastro()
            print("Cadastro do aluno realizado com sucesso.")
        elif esco == 'cadastro professor':
            cadastro_professor()
            print("Cadastro do professor realizado com sucesso.")
        elif esco == 'cadastro matéria':
            cadastro_materia()
            print("Cadastro de matéria realizado com sucesso.")
        elif esco == 'cadastro curso':
            cadastro_do_curso()
            print("Cadastro de curso realizado com sucesso.")
        elif esco == "cadastro de funcionário":
            cadastro_de_funcionario()
            print("Cadastro de funcionário realizado com sucesso.")
        elif esco == 'deletar informacao do funcionario':
            deletar_informacao_do_arquivo()
            print('deletacao do funcionario sucesso!!!')



        elif esco == 'sair':
            break
        else:
            print("Opção inválida.")

menu()
