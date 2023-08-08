FIAT = {'MOBI': '58.990', 'ARGO': '69.990', 'CRONOS': '71.790'}
while True:
    produto = input('Digite o nome do produto ou fim para terminar: ')
    if produto == 'fim':
        break
    if produto in FIAT:
        print(f'Preço: R${FIAT[produto]:.2f}')
    else:
        print('Produto não encontrado')
