# 🤖 Chatbot com API Flask + Interface PyQt5

Este é um projeto simples de chatbot com:

- **Backend em Flask** que processa mensagens e responde.
- **Interface gráfica moderna com PyQt5**, que se comunica com a API.
- Lógica de chatbot básica embutida, podendo ser estendida facilmente.

📁 Estrutura atualizada do projeto
java
Copy
Edit
chatbot_project/
├── app.py
├── gui.py
├── chatbot_logic.py
├── database.py         👈 Novo arquivo (manipula SQLite)
└── chat_history.db     👈 Gerado automaticamente

## 🚀 Como executar o projeto

### 1. Clone o repositório

bash
git clone https://github.com/seu-usuario/chatbot-pyqt-flask.git
cd chatbot-pyqt-flask

2. Crie e ative um ambiente virtual (opcional, mas recomendado)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate    # Linux/macOS
venv\Scripts\activate       # Windows
3. Instale as dependências
bash
Copy
Edit
pip install -r requirements.txt
4. Inicie o servidor Flask (backend)
bash
Copy
Edit
python app.py
Deixe esse terminal aberto — o Flask precisa estar em execução para o chatbot funcionar.

5. Execute a interface gráfica (frontend)
Em outro terminal:

bash
Copy
Edit
python gui.py
🧠 Arquivos principais
Arquivo	Descrição
app.py	API Flask que recebe mensagens e responde
chatbot_logic.py	Lógica simples de resposta do bot
gui.py	Interface gráfica moderna com PyQt5
requirements.txt	Lista de dependências Python

✅ Exemplos de comandos
text
Copy
Edit
Você: oi
Bot: Oi! Como posso te ajudar?

Você: ajuda
Bot: Claro, estou aqui para te ajudar. Pergunte algo!

Você: tchau
Bot: Até logo!
📦 Requisitos
Python 3.7+

PyQt5

Flask

requests

✨ Possibilidades de melhoria
Integração com ChatGPT (OpenAI API)

Armazenamento de histórico em SQLite

Modo escuro

Suporte a múltiplos usuários

📃 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.