import banco
#Controller - a validacao
def validar_login(usuario_digitado, senha_digitado):
    usuario_BD = banco.model_usuario()
    senha_BD = banco.model_senha()
    if usuario_digitado == usuario_BD  and senha_digitado == senha_BD:
        print('pode entrar')
    else:
        print('Usuário ou senha invalido')
