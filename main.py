#View - o que vai para o usuario

usuario_digitado = input("Informe o seu usuário: ")
senha_digitado = input("Informe sua senha: ")

#Model - O que vem do banco de dados
usuario_BD = 'joao'
senha_BD = '123'


#Controller - a validacao
if usuario_digitado == usuario_BD  and senha_digitado == senha_BD:
    print('pode entrar')
else:
    print('Usuário ou senha invalido')
