boloCenoura = ['farinha','trigo','ovo','cenoura','fermento','bolo de cenoura']
boloMorango = ['farinha','trigo','ovo','morango','fermento','bolo de morango']
boloChocolate = ['farinha','trigo','ovo','chocolate','fermento','bolo de chocolate']
boloMaracuja = ['farinha','trigo','ovo','maracuja','fermento','bolo de maracuja']

pudimDeLeite = ['leite condensado','leite','ovo','pudim de leite']
pudimDePao = ['leite condensado','leite','ovo','pão','pudim de pão']

TortaLimao = ['maizena','leite condensado','limão','glace','torta de limão']
TortaBanana = ['maizena','leite condensado','banana','glace','torta de banana']

brigadeiro = ['chocolate','leite condensado','manteiga','brigadeiro']
beijinho = ['baunilha','leite condensado','manteiga','coco','beijinho']


doces = [boloCenoura,boloMorango,boloChocolate,boloMaracuja,pudimDeLeite,pudimDePao,TortaLimao,TortaBanana,brigadeiro,beijinho]



def VerificarSobremesa(Lista):

    global doces
    docespossiveis = []
    
    for ingrediente in Lista:
        for doce in doces:
            for ingredienteDoce in doce:
                if ingrediente == ingredienteDoce:
                    docespossiveis.append(doce[-1])
                    
    
    
    print(docespossiveis)
                
    
    
    
lista = []

numeroingredientes = int(input("Você deseja utilizar quantos ingredients?\nR: "))

for i in range(numeroingredientes):
    ig = input(f"Ingrediente numero {i+1}: ")
    lista.append(ig)
    
VerificarSobremesa(lista)