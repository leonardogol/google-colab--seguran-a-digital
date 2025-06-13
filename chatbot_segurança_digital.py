# Instale a biblioteca com: pip install -U google-generativeai
import google.generativeai as genai
import time

# Configuração da chave da API
API_KEY = input("Digite sua chave da API do Google AI Studio: ").strip()
genai.configure(api_key=API_KEY)

# Inicializa o modelo com comportamento controlado
model = genai.GenerativeModel(
    model_name="models/gemini-1.5-flash",
    generation_config={
        "temperature": 0.4,
        "max_output_tokens": 300,
    },
    system_instruction=(
        "Você é um assistente objetivo, profissional e claro, especializado em segurança digital. "
        "Suas respostas devem ser curtas, úteis e baseadas em boas práticas. Não utilize emojis nem linguagem informal. "
        "Explique conceitos como phishing, senhas fortes, proteção de dados, VPN, etc., de forma acessível a qualquer idade."
    )
)

chat = model.start_chat(history=[])

PALAVRAS_CHAVE = [
    "senha", "phishing", "malware", "vpn", "segurança", "privacidade",
    "antivírus", "ransomware", "dados", "proteção", "hacker", "golpe",
    "email falso", "autenticação", "criptografia", "navegação segura",
    "engenharia social", "firewall", "invasão", "spam"
]

def eh_pergunta_valida(pergunta):
    return any(p in pergunta.lower() for p in PALAVRAS_CHAVE)

def conversar():
    print("\nAssistente de Segurança Digital")
    print("Este chatbot responde exclusivamente dúvidas sobre segurança digital.\n")

    while True:
        pergunta = input("Você: ").strip()

        if pergunta.lower() in ["sair", "n", "não", "nao", "obrigado", "obrigada"]:
            print("Sessão encerrada.")
            break

        if not eh_pergunta_valida(pergunta):
            print("Esta pergunta não está relacionada à segurança digital.")
            print("Por favor, envie uma nova pergunta sobre privacidade, golpes digitais, senhas ou proteção de dados.\n")
            continue

        print("Processando...\n")
        time.sleep(1)

        try:
            resposta = chat.send_message(pergunta)
            texto = resposta.text.strip()
            # Exibir só a primeira linha da resposta para manter curto
            print(texto.split("\n")[0] + "\n")
        except Exception as e:
            print("Erro ao processar sua pergunta.")
            print(f"Detalhes técnicos: {e}\n")

if __name__ == "__main__":
    conversar()


