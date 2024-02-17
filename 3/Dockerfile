#Primeiro, usaremos uma imagem leve, como a que foi descrita no exemplo 1, "Alpine Linux"
FROM alpine:latest

# Criando um diretorio dentro do conteiner
RUN mkdir /app

# Define o diretorio de trabalho
WORKDIR /app

# Configura um volume para esse diretorio
VOLUME /app

# Define o comando padrao a ser executado quando o conteiner for iniciado
CMD ["sh"]

#para rodar no terminal usamos os seguintes comandos:

#docker build -t meu-container .
# que constroi a imagem

#docker run -it -v /home/maria/redes5p/3/app meu-container
#que é o local onde o meu diretorio esta localizado e faz executar o arquivo
