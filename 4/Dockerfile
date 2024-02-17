# Usa a imagem base do Python
FROM python:3.9-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos necessários para o contêiner
COPY app.py /app

# Instala o Flask (se necessário)
RUN pip install flask

# Expõe a porta 5000 para o exterior
EXPOSE 5000

# Define o comando padrão a ser executado quando o contêiner for iniciado
CMD ["python", "app.py"]
