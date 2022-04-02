
nome = 'Leandro'
idade = 23
altura = 1.70
e_maior = idade >= 18
peso = 80
imc = peso/(altura**2)

print(nome,'tem',idade,'anos de idade e seu imc e',imc)
print(f'{nome} tem {idade} anos de idade e seu imc e {imc:.2f}')
print('{n} tem {i} anos e seu imc e {im}'.format(n=nome,i=idade,im=imc))

