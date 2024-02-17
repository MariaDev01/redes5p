#Crie um Dockerfile para uma aplicacao Python basica;
# usei a versao 3.9-slim por ser a mais indicada pela internet
FROM python:3.9-slim

WORKDIR /app

COPY hello.py /app


#instala o que eu preciso

# Define o comando padrão a ser executado quando o contêiner for iniciado
CMD ["python", "hello.py"]

#baixar o que eu preciso no terminalno terminal:
#docker build -t python-app-image . 

#rodar o que eu preciso no terninal
#docker run python-app-image