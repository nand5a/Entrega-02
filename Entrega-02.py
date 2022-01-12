print("\n Bem-vindo ao menu de gerenciamento!\n")
esc = int(input('Digite 1 para criar um ônibus: '))

a = True
b = False
ListaOnibus = []
ListaMotoristas = []
ListaFiscais = []

while a == True:

    while b == True:
        print('\n O que deseja fazer agora?\
        \n 1 - Criar um ônibus \
        \n 2 - Mostrar ônibus \
        \n 3 - Alterar dados do motorista\
        \n 4 - Alterar dados do fiscal\
        \n 5 - Alterar rota do ônibus\
        \n 6 - Deletar ônibus \n')

        esc = int(input('Escolha uma das opções para continuar: '))
        
        b = False

    class Onibus:

        def __init__(self, nome, parada, motorista, fiscal):
            self.nome = nome
            self.parada = parada
            self.motorista = motorista
            self.fiscal = fiscal
        
        def __str__(self):
            return f" Nome do ônibus: {self.nome} \
                \n Rota: {self.parada} \
                \n Motorista: {self.motorista} \
                \n Fiscal: {self.fiscal}" 

    if (esc == 1): 
        #Criar um ônibus com ponto de parada, motorista e fiscal, 
        #assigna motorista e fiscal ao ônibus e adicona ponto de parada. 

        nome = str(input('Nome do ônibus: '))
        parada = str(input('Parada do ônibus:'))
        motorista = str(input('Nome do motorista: '))
        fiscal = str(input('Nome do fiscal: '))
            
        onb = Onibus(nome, parada, motorista, fiscal)

        ListaOnibus.append(onb)     

        print('\n Ônibus criado!')

        b = True

    if (esc == 2): 
    #Mostra o ônibus, sua rota, seu motorista e seu fiscal

        print('\n Informações do ônibus', onb.nome, ':\n')
    
        for item in ListaOnibus:
            print(item) 

        tamanho = len(ListaOnibus)

        if tamanho == 0:
            print('Não há nenhum ônibus cadastrado.')

        b = True      

    class Motorista:
        def __init__(self, nomeMot, idade, cpf):
            self.nomeMot = nomeMot
            self.idade = idade
            self.cpf = cpf

        def __str__(self):
                return f" Nome do motorista: {self.nomeMot} \
                    \n Idade: {self.idade} \
                    \n CPF: {self.cpf} "
    
    if (esc == 3): 
        #Altera dados do Motorista
        
        onb = Onibus(nome, parada, motorista, fiscal)    

        print('\n O motirsta do ônibus', onb.nome, 'é o: ', onb.motorista)

        print('\n')
        nomeMot = onb.motorista
        idade = str(input('Idade do motorista:'))
        cpf = str(input('CPF: '))
        print('\n')

        mot = Motorista(nomeMot, idade, cpf)

        ListaMotoristas.append(mot)  

        for item in ListaMotoristas:
            print(item) 

        print('\n Os dados do motorista', onb.motorista, 'foram alterados!')  

        b = True 

    class Fiscal:
        def __init__(self, nomeFis, idade, cpf):
            self.nomeFis = nomeFis
            self.idade = idade
            self.cpf = cpf

        def __str__(self):
                return f" Nome do fiscal: {self.nomeFis} \
                    \n Idade: {self.idade} \
                    \n CPF: {self.cpf} "

    if (esc == 4): 
        #Altera dados do Fiscal

        onb = Onibus(nome, parada, motorista, fiscal)    

        print('O fiscal do ônibus:', onb.nome, 'é o: ', onb.fiscal)

        print('\n')
        nomeFis = onb.fiscal
        idade = str(input('Idade do fiscal:'))
        cpf = str(input('CPF: '))
        print('\n')

        fis = Fiscal(nomeFis, idade, cpf)

        ListaFiscais.append(fis)  

        for item in ListaFiscais:
            print(item)

        print('\n Os dados do fiscal foram alterados!')

        b = True 

    if (esc == 5):
    #Altera rota do ônibus

        onb = Onibus(nome, parada, motorista, fiscal)    

        print('\n O ponto de parada do ônibus', onb.nome, 'é: ', onb.parada)

        print('\n')        
        onb.parada = str(input('Nova parada:'))
        print('\n')

        print('Local de parada atualizado para: ', onb.parada, '.')

        b = True

    if (esc == 6):
        #Deleta ônibus

        ListaOnibus.clear()

        print('O ônibus foi deletado')

        b = True

