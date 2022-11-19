a = int(input('Entre com um valor:  '))
b = int(input('Entre com um valor:  '))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
resultado = ('Soma: {sum}. \nSubtração: {sb}. '
             '\nMultiplicação: {mt}. '
             '\nDivisão: {dv}. '
             '\nResto: {rt}. '.format(sum= soma,
                                      sb= subtracao,
                                      mt= multiplicacao,
                                      dv= divisao,
                                      rt= resto))
print('O seu resultado é: \n' )

print(resultado)
