# db/session_manager.py
from models.user import Usuario

# Simulação de um usuário logado
USUARIO_TESTE = Usuario("Alex", "Rio Ner de Jeneio", "alex@teste.com", "123.456.789-00")

def get_logged_user():
    """Retorna o objeto do usuário logado (simulação de sessão)."""
    # Em um app real, isso buscaria o usuário na sessão ou DB
    return USUARIO_TESTE