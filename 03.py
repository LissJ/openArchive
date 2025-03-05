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

# solicitando o nome dos arquivos a serem abertos, definindo a quantidade pela variável 'num' (que armazena o valor colocado dentro de 'config.txt')
# a função split serve para que a string seja dividida por espaços e organizada em lista ["algumaCoisa", "algoAqui"]
arquivos = input(f"Digite os nomes de {num} arquivos separados por espaço: ").split()

# verificando se a quantidade de arquivos inseridos está diferente do valor definido dentro da variável 'num' (config.txt)
if len(arquivos) != num:
    # caso seja diferente, o script é encerrado e uma mensagem de erro é exibida
    exit("Erro: Quantidade incorreta de arquivos!")

# abrindo (ou criando) um arquivo chamado 'resultado.txt', no modo escrever (write) com a codificação correta do teclado pt-br
with open("resultado.txt", "w", encoding="utf-8") as resultado:
    # para cada nome adicionado na lista arquivos, será executado o seguinte loop
    for nome in arquivos:
        # abrindo o arquivo a partir do nome inserido na variável arquivos, no modo ler (read) com a codificação correta do teclado pt-br
        with open(nome, "r", encoding="utf-8") as f:
            # depois de ler todo o arquivo aberto, ele retornará o conteúdo como uma string
            # essa string será escrita no arquivo 'resultado.txt', sendo acompanhada por uma quebra de linha, para que não fique desorganizado 
            resultado.write(f.read() + "\n")

# exibindo uma mensagem de sucesso
print("Arquivos combinados em 'resultado.txt'")