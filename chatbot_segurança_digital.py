# Instalar biblioteca da Google Gemini
!pip install google-generativeai --quiet

# Importar e configurar API do Gemini
import google.generativeai as genai
import time

# Substitua pela sua chave de API do Google AI Studio: https://aistudio.google.com/app/apikey
API_KEY = "SUA_CHAVE_AQUI"
#Substitua a linha acima pela sua chave de API do Google AI Studio



pela sua chave da API do Google AI Studio
genai.configure(api_key=API_KEY)

# Inicializar modelo e histórico
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

# Lista de temas válidos para segurança digital
palavras_chave = [
    "senha", "phishing", "malware", "vpn", "segurança", "privacidade",
    "antivírus", "ransomware", "dados", "proteção", "hacker", "golpe",
    "email falso", "autenticação", "criptografia", "navegação segura",
    "engenharia social", "firewall", "invasão", "spam"
]

# Função para verificar se a pergunta é relevante
def eh_pergunta_valida(pergunta):
    return any(p in pergunta.lower() for p in palavras_chave)

# Função principal de interação
def conversar():
    print("🔐 Bem-vindo ao Assistente de Segurança Digital!")
    print("🧠 Estou aqui para esclarecer dúvidas sobre boas práticas digitais.\n")
    print("💬 Como posso ajudar?")

    while True:
        pergunta = input("\nVocê: ").strip()

        if pergunta.lower() in ["sair", "não", "nao", "obrigado", "obrigada", "n"]:
            print("\n🤖 Tudo bem! Se precisar, estarei à disposição. Cuide-se online! 👋")
            break

        if not eh_pergunta_valida(pergunta):
            print("\n⚠️ Este chatbot responde apenas a perguntas sobre **segurança digital**.")
            print("📝 Exemplos: Como criar uma senha forte? O que é phishing? Devo usar antivírus?")
            continue

        print("\n🤖 Analisando sua pergunta...")
        time.sleep(1)

        try:
            resposta = chat.send_message(pergunta)
            print(f"\n🔎 Resposta:\n{resposta.text}")
        except Exception as e:
            print("\n❌ Ocorreu um erro ao processar sua pergunta. Tente novamente.")
            print(f"Erro técnico: {e}")

        print("\n💬 Algo mais?")
        
# Executar chatbot
conversar()
