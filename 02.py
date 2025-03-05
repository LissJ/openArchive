# abrindo o arquivo (já existente) chamado 'config.txt' no modo leitura (read) com a codificação correta do teclado pt-br
with open("config.txt", "r", encoding="utf-8") as f:
    # lendo todo o arquivo com a função read e armazenando como string
    # removendo todos os espaços em branco ou quebra de linha com o strip, no início ou no final da string lida
    # a função do split esta servindo como um divisor, utilizando o '=' como um delimitador, criando uma lista de duas partes
        # tipo, se estiver 'num=3' no config.txt, ele vai ler como
            # ["num", "5"]
        # a parte do [1] pega a segunda informação da lista (pois sabemos que o primeiro item sempre será 0)
    # o int converte a string para um valor numérico inteiro, e também o armazena na variável 'num'
    num = int(f.read().strip().split("=")[1])

# solicitando os parâmetros para o usuário de acordo com o número lido no arquivo
# e o split armazena os parãmetros em formato de lista dentro da variável 'parametros'
parametros = input(f"{num} parâmetros: ").split()
# verificando se a quantidade de parâmetros adicionada pelo usuário corresponde com a quantidade lida no 'config.txt'
if len(parametros) != num:
    # caso seja diferente, o script é encerrado e uma mensagem de erro é exibida
    exit("Erro: Número incorreto!")

# caso o número de parâmetros inseridos estejam corretos, uma mensagem é exibida, seguido da lista do mesmo
print("Parâmetros aceitos:", parametros)