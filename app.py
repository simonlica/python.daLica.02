
import os 

restaurante=[] 

def finalizar_app():
    os.system('clear')
    print ('Finalizando app\n')

def chamar_name_do_app():
     print ('Restaurante Expresso\n') 

def opcao_invalida():
    print('Opção invalida\n')
    input('Digite uma tecla para voltar ao menu principal: ')
    main() 

def exibir_opcoes():
    print('1-cadastrar um restaurante')
    print('2-listar restaurantes')
    print('3-ativar um restaurante')
    print('4-sair do programa') 


def cadastrar_novo_restaurante():
     os.system('clear')
     nome_do_restaurante=input('Digite o nome do novo restaurante: ')
     restaurante.append(nome_do_restaurante)
     print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso')
     input("Digite uma tecla para voltar ao menu principal: ")

def escolher_opcoes(): 
    try:
        opcao_digitada=int(input('Escolha uma opção: '))
        print('Você sleecionou a opção: ',opcao_digitada,'\n')
        if(opcao_digitada==1):
            print('Você escolheu cadastrar um restaurante\n')
            cadastrar_novo_restaurante()
        elif (opcao_digitada==2):
            print('Você escolheu listar os restaurantes do app\n')
        elif (opcao_digitada==3):
            print('Você escolheu ativar um restaurante\n')
        elif (opcao_digitada==4):
            print('Você escolheu sair do programa\n')
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida() 

def main():
    os.system('clear') 

    chamar_name_do_app() 

    exibir_opcoes() 

    escolher_opcoes() 

if(__name__=='__main__'):
    main()



