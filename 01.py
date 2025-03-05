# solicitando o nome do arquivo a ser gerado e o armazenando numa variável
nome_arquivo = input("Digite o nome do arquivo: ")

# solicitando os parâmetros a serem inseridos dentro do arquivo gerado e armazenando numa variávelD
# a função split serve para que a string seja dividida por espaços e organizada em lista ["algumaCoisa", "algoAqui"]
parametros = input("Digite os parâmetros separados por espaço: ").split()

# abrindo o arquivo gerado no modo 'escrever' (ele cria o arquivo, caso não exista)
# também garantindo que o padrão do teclado esteja com as codificações corretas do pt-br
with open(nome_arquivo, "w", encoding="utf-8") as f:
    # para cada parâmetro que foi adicionado na variável parâmetros, ele executará esse loop, assumindo o valor de cada item, um de cada vez
    for parametro in parametros:
        # função de escrever (write) cada parâmetro dentro de parâmetros, sendo acompanhado por uma quebra de linha, para que não fique desorganizado 
        f.write(parametro + "\n")

# imprimindo que os parâmetros foram salvos corretamente no arquivo digitado pelo usuário
print(f"Parâmetros salvos no arquivo {nome_arquivo}")