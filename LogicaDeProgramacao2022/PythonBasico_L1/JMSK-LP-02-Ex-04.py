largura=int(input('Digite a largura do terreno: '))
profundidade=int(input('Digite a profundidade do terreno: '))
hectare=(largura*profundidade)/10000
print('Seu terreno tem a dimensão de {}x{} e sua área é de {} hectares.'.format(largura,profundidade,hectare))