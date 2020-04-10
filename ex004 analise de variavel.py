"""
EXERCÍCIO 004: Dissecando uma Variável
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
e todas as informações possíveis sobre ele.
"""
v = input('Digite algo: ')
print('O tipo primitivo dessa variavel é: ', type(v))
print('Só tem espaços? ', v.isspace())
print('É um número? ', v.isnumeric())
print('É alfabetico? ', v.isalpha())
print('É alfanúmerico? ', v.isalnum())
print('está maiúsculo? ', v.isupper())
print('está em minúsculas', v.islower())
print('está capitalizada', v.istitle())