def get_response(user_input):
    user_input = user_input.lower()
    if "oi" in user_input or "olá" in user_input or "ola" in user_input:
        return "Oi! Como posso te ajudar?"
    elif "ajuda" in user_input:
        return "Claro, estou aqui para te ajudar. Pergunte algo!"
    elif "2º via" in user_input:
        return "clario digite o codigo"
    elif "tchau" in user_input:
        return "Até logo!"
    elif "documentos" in user_input:
        return "Quais documentos você precisa"
    else:
        return "Desculpe, não entendi. Pode reformular?"
