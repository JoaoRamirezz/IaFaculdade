boloCenoura = ['farinha','trigo','ovo','cenoura','fermento']
boloMorango = ['farinha','trigo','ovo','morango','fermento']
boloChocolate = ['farinha','trigo','ovo','chocolate','fermento']
boloMaracuja = ['farinha','trigo','ovo','maracuja','fermento']

pudimDeLeite = ['leite condensado','leite','ovo']
pudimDePao = ['leite condensado','leite','ovo']

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


def AddReceitas(NomeReceita, Receita, Receitas):
    Receitas[NomeReceita] = Receita
    
    return Receitas
    
def VerificarSobremesa(ingredientes: list, Receitas) -> list:

    possiveis = []
    
    for nome in Receitas:
        receita = Receitas[nome]
        flag = True
        
        for ingrediente in ingredientes:
            if (not (ingrediente.strip().lower() in receita)):
                flag = False
                break
            
        if (flag):
            possiveis.append(nome)
    
    return possiveis
            
                
    
def Iniciar(doces):
    doces = AddReceitas("NomeReceita", ["Receita"], doces)
    
    
    escolha = int(input('O que deseja fazer?\n1) Adicionar uma receita no livro de receitas. \n2) Verificar uma receita. \nR: '))
    
    
    if escolha == 1:
        Receita = []
        NomeReceita = input('Insira o nome da receita: ')
        
        Qtt = int(input('Quantos igredientes possui sua receita? '))
        
        for i in range(Qtt):
            igrediente = input(f'Igrediente numero {i+1}: ')
            Receita.append(igrediente)
        
        AddReceitas(NomeReceita, Receita, doces)
        
        
        
    elif escolha == 2:
        lista = []
        numeroingredientes = int(input("Você deseja utilizar quantos ingredients?\nR: "))
        
        for i in range(numeroingredientes):
            ig = input(f"Ingrediente numero {i+1}: ")
            lista.append(ig)
        
        print(VerificarSobremesa(lista))
    


Iniciar(doces)