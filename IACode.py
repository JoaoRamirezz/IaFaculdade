boloCenoura = ['farinha','trigo','ovo','cenoura','fermento']
boloMorango = ['farinha','trigo','ovo','morango','fermento']
boloChocolate = ['farinha','trigo','ovo','chocolate','fermento']
boloMaracuja = ['farinha','trigo','ovo','maracuja','fermento']




pudimDeLeite = ['leite condensado','leite','ovo']
pudimDePao = ['leite condensado','leite','pão']




TortaLimao = ['maizena','leite condensado','limão','glace']
TortaBanana = ['maizena','leite condensado','banana','glace']




brigadeiro = ['chocolate','leite condensado','manteiga']
beijinho = ['baunilha','leite condensado','manteiga','coco']





doces = {'bolo de cenoura' : boloCenoura , 'bolo de morango' : boloMorango, 
         'bolo de chocolate' : boloChocolate, 'bolo de maracuja' : boloMaracuja,
         'pudim de leite' : pudimDeLeite, 'pudim de pão' : pudimDePao,
         'torta de limão' : TortaLimao, 'torta de banana' : TortaBanana,
         'brigadeiro' : brigadeiro, 'beijinho' : beijinho
         }

salgados = {
    }


def AddReceitas(NomeReceita, Receita, Receitas):
    Receitas[NomeReceita] = Receita
    
    return Receitas
    
def VerificareReceita(ingredientes, Receitas):
    possiveis = []
    
    for nome in Receitas:
        receita = Receitas[nome].copy()
        
        for ingrediente in ingredientes:
            ig = ingrediente.strip().lower()
            if ( ig in receita):
                receita.remove(ig)
                
        if len(receita) == 0:
            possiveis.append(nome)
            print(f"adicionei: {nome} - {ingredientes}")
    
    return possiveis
            
                
    
def Iniciar():
    
    
    escolha = int(input('O que deseja fazer?\n1) Adicionar uma receita no livro de receitas. \n2) Verificar uma receita. \nR: '))
    
    
    if escolha == 1:
        
        tipo = int(input("Qual o tipo da sua receita?\n1) Salgado \n2) Doce\nR: "))
        
 
        Receita = []
        NomeReceita = input('Insira o nome da receita: ')
        
        while True:
            igrediente = input('Insira um igrediente: ')
            
            if igrediente == '':
                break
            else:
                Receita.append(igrediente)
                
        
        if tipo == 1:
            AddReceitas(NomeReceita, Receita, salgados)
        elif tipo == 2:
            AddReceitas(NomeReceita, Receita, doces)
        
        
        
        
        
    elif escolha == 2:
        lista = []
        
        tipo = int(input("Qual o tipo da sua receita?\n1) Salgado \n2) Doce\nR: "))
        
        while True:
            ig = input("Insira um igrediente: ")
            if ig == '':
                break
            else: 
                lista.append(ig)
        
        
        
        if tipo == 1:
            print('\nPossiveis receitas: ',VerificareReceita(lista, salgados))
        elif tipo == 2:
            print('\nPossiveis receitas: ',VerificareReceita(lista, doces))


while True:
    escolha = int(input('Deseja realizar uma ação?\n1) Sim\n2) Não\nR: '))
    
    if escolha == 1:
        Iniciar()
    elif escolha == 2:
        print("Obrigado por utilizar nosso algoritmo!")
        
        break
    else:
        print("Escolha uma opção valida!")