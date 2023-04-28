
import base64
from cryptography.fernet import Fernet 

def find_by_id(mensagens, id_msg):
    if len(mensagens) > 0: #valida se possui mensagens na lista
        for textos in mensagens:
            if textos['id_msg'] == id_msg:  #valida se existe a mensagem com esse identificador
                return True

    return False

def adicionar(mensagens):
    if len(mensagens) > 0:
        id_msg = len(mensagens)+1
    else:
        id_msg = 1

    cripto_mensagem = input('Digite a mensagem: \n> ').strip()

    mensagem = {
        'id_msg': id_msg,
        'remetente': input('Digite o nome do Remetente: \n> ').strip(),
        'destinatario': input('Digite o nome do Destinatário: \n> ').strip(),
        'mensagem': encriptar(cripto_mensagem),
        'chave': Fernet.generate_key() 
    }

    mensagens.append(mensagem)
    print('A mensagem enviada para {} foi criptografada com sucesso !!!\n' .format(mensagem['destinatario']))
    print('Chave para descriptografar: {}' .format(str(mensagem['chave'].decode())))

def encriptar(msg):
    msg = msg.encode('ascii') # Codificar usando a tabela ascii
    mensagemb64 = base64.b64encode(msg) # Criptografar cirando uma hash de base64
    return mensagemb64

def listar(mensagens):
    if len(mensagens) > 0:
        for i, textos in enumerate(mensagens):
            print('Id {}: '.format(textos['id_msg']))
            print('\tRemetente: {}' .format(textos['remetente']))
            print('\tDestinatário: {}' .format(textos['destinatario']))
            print('\tMensagem: {}' .format(textos['mensagem']))
            print('\n===========================================\n')
        print('Quantidade de Mensagens enviadas: {}\n' .format(len(mensagens)))
    else:
        print('Não existe nenhuma mensagem enviada.\n')

def descriptografar(mensagens):
    print(' \n ===== Descriptografar Mensagem ===== \n')
    if len(mensagens) > 0:
        id_msg = int(input('Digite o id da mensagem: \n> '))
        if find_by_id(mensagens, id_msg):
            for textos in mensagens:
                if textos['id_msg'] == id_msg:
                    print('Remetente: {}' .format(textos['remetente']))
                    print('Destinatário: {}' .format(textos['destinatario']))
                    print('Mensagem: {}' .format(textos['mensagem']))
                    
                    print('\n========================================\n')
                    chave = input('Digite a chave: \n> ').strip()
                    chave = chave.encode()
                    if textos['chave'] == chave:
                        mensagemdescript = textos['mensagem']
                        mensagemdescript = base64.b64decode(mensagemdescript)
                        mensagemdescript = mensagemdescript.decode('ascii')

                        print('A mensagem enviada foi: {}' .format(mensagemdescript))
                        break
                    else:
                        print('Chave Inválida.')
        else: 
            print('Não existe mensagem com esse id.')   

opcao = None
mensagens = []
while opcao != 'sair':
    print(' \n ===== Cripto Mensagens ===== \n')
    print(' 1 - Criptografar Mensagem')
    print(' 2 - Listar Mensagens')
    print(' 3 - Descriptografar Mensagem')
    print('Digite "sair" para finalizar o programa de mensagens.')

    opcao = input('\n> ')
    opcao = opcao.lower()

    if opcao == '1':
        adicionar(mensagens)
    elif opcao == '2':
        listar(mensagens)
    elif opcao == '3':
        descriptografar(mensagens)