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



def VerificarSobremesa(Lista):

    global doces
    docespossiveis = []
    
    for ig in Lista:
        for doce in doces:
            for ig2 in doces[doce]:
                if ig != ig2:
                    print(ig + '/' + ig2 + 'DIFERENTE')
                    break
            docespossiveis.append(doces)
        
                
    
    
    # for ingrediente in Lista:
    #     for doce in doces:
    #         for ingredienteDoce in doce:
    #             if ingrediente == ingredienteDoce:
    #                 docespossiveis.append(doce[-1])
                    
    
    
    print(docespossiveis)
                
    
    
    
lista = []

numeroingredientes = int(input("Você deseja utilizar quantos ingredients?\nR: "))

for i in range(numeroingredientes):
    ig = input(f"Ingrediente numero {i+1}: ")
    lista.append(ig)
    
VerificarSobremesa(lista)