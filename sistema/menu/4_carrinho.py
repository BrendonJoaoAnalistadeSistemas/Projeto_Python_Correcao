 import os 


os.system('cls')


print('-'*70)
print('Adicionar produtos para compra no carrinho')
print('='*70)

carrinho = []

while True:
       
    print('-'*70)
    print('opções para compra')
    print('='*70)
    print('1. adicionar item')
    print('2. Remover item')
    print('3.exibir itens e valor total')
    print('4. Limpar carrinho de compras')
    print('5. Sair')
    
carrinho = [] 

def exibiropçoes():
   print('\n\n')
   print('1. Adicionar item')
   print('2. Remover item')
   print('3. Exibir itens e o valor total')
   print('4. limpar carrinho de compras')
   print('5. Sair')

   def exibirprodutos(): 
      for p in produtos:
        print() 
        
   opcao = '1'
   os,system('cls')
   print('Carrinho de compras \n')

   while opcao != '5':
      exibiropcaoes()
      opcao = input('Digite a opção: ')

      if opcao == '1':
        
        os.system('cls')
        print('carrinho de compras \n')
 
def obeterNomeproduto(id):
        for p in produtos:
           if p['id'] == id:
               retona p ['nome']
        id = int(input('Digite o identificador do produto: '))
        quantidade = int(input('Digite a quantidade: '))
        carrinho.append(['id']: id,quantidade: quantidade)

        if opcao == '2':
          id = int(input('Digite o identificador do produto: '))
          temp = []
          for item in carrinho:
              if item['id'] !=id:
              temp.append(item)
        if opcao == '3':
           print('\n\n')
        somatorio = 0
        for item in carrinho:
                for produto in produtos:
                 if produto['id'] == itens['id']:
                    somatorio = somatorio + (produto['preco'] * item('quantidade'))
                    break
                    
               print(
                  'Nome:{0} - quantidade: {1}'.format(obeterprodutos(item['id'], item['quantidade'])))
                print('Preço total: {0}', format(somatorio))

    if opcao == '4':
       carrinho = []
    