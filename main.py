import os
import openai
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

# Configurar a API do Azure OpenAI
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_key = os.getenv("AZURE_OPENAI_KEY")
openai.api_type = "azure"
openai.api_version = os.getenv("AZURE_OPENAI_API_VERSION")

# Nome do deployment configurado no Azure
deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT")

def chat_with_openai(prompt):
    """Função que envia uma mensagem para a API do Azure OpenAI e retorna a resposta."""
    try:
        response = openai.ChatCompletion.create(
            engine=deployment_name,
            messages=[
                {"role": "system", "content": "Você é um assistente útil."},
                {"role": "user", "content": prompt}
            ]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Erro ao acessar a API: {str(e)}"

if __name__ == "__main__":
    print("Bem-vindo ao Chatbot com Azure OpenAI! Digite 'sair' para encerrar.")
    while True:
        user_input = input("Você: ")
        if user_input.lower() == "sair":
            break
        resposta = chat_with_openai(user_input)
        print("Chatbot:", resposta)
  
