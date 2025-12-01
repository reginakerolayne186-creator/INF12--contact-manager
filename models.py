# models/user.py

class Pessoa:
    """Classe base para qualquer pessoa no sistema (Abstração)."""
    def __init__(self, nome, cidade):
        self._nome = nome  # Encapsulamento
        self._cidade = cidade # Encapsulamento

    def get_info_basica(self):
        """Retorna informações básicas do usuário."""
        return f"Nome: {self._nome}", f"Cidade: {self._cidade}"

class Usuario(Pessoa):
    """Representa um usuário logado (Herança)."""
    def __init__(self, nome, cidade, email, cpf):
        super().__init__(nome, cidade)
        self._email = email
        self._cpf = cpf

    def autenticar(self, senha_hash):
        # Lógica real de autenticação com hash de senha
        return True 

    def get_perfil_detalhes(self):
        """Retorna detalhes para a tela de perfil (Polimorfismo implícito)."""
        return {
            "usuario": "OrionWalker",
            "caracteristicas": "Curioso, Empático, Bem-humado",
            "personalidade": "Sonhador, Adora longas conversas, Busca profundidade"
        }