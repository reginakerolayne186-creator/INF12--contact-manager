# styles.py

# Cores
COR_BRILHO = '#ffaa00'
COR_DESTAQUE = '#ff4500'
COR_FUNDO_LOGIN = '#ff6600'
COR_FUNDO_PERFIL = '#2e0a0a'
COR_BTN_X = 'red'

# CSS Básico para Streamlit
def get_global_styles(current_page):
    """Retorna o bloco de estilos CSS global para a página atual."""
    return f"""
<style>
/* Fundo dinâmico baseado na página */
.stApp {{
    background-color: {COR_FUNDO_LOGIN if current_page == 'login' else COR_FUNDO_PERFIL}; 
    color: white;
}}
/* Estilos básicos de input */
div[data-testid="stTextInput"] input, div[data-testid*="stButton"] button {{
    border-radius: 5px;
}}
</style>
"""