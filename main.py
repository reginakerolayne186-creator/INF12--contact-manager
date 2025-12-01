# main.py

import streamlit as st
from PIL import Image
from db.session_manager import get_logged_user
from styles import COR_BRILHO, COR_DESTAQUE, COR_BTN_X, get_global_styles

# --- 1. Controle de Estado ---
if 'page' not in st.session_state:
    st.session_state.page = 'login'

def go_to_profile():
    st.session_state.page = 'profile'

def go_to_login():
    st.session_state.page = 'login'

# Aplica estilos globais
st.markdown(get_global_styles(st.session_state.page), unsafe_allow_html=True)


# --- 2. Renderização da Tela de Login/Cadastro ---
def render_login_page():
    st.markdown('<h1 style="color: white; text-align: center;">PERSONALYTE</h1>', unsafe_allow_html=True)
    st.markdown("Bem-vindo ao PERSONALITY...")

    # Card de Login/Cadastro
    st.markdown(f'<div style="background: linear-gradient(to top, #ff6600, #ff8c00); padding: 30px; border-radius: 15px;">', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.button("Criar Conta", key="top_criar", use_container_width=True)
    with col2:
        if st.button("Entrar", key="top_entrar", use_container_width=True):
            go_to_profile()

    st.text_input("", placeholder="Email")
    st.text_input("", placeholder="Senha", type="password")
    st.text_input("", placeholder="CPF")

    if st.button("Criar Conta", key="bottom_criar", use_container_width=True):
        # Simulação de cadastro bem-sucedido
        st.success("Conta Criada! Indo para o Perfil.")
        go_to_profile()

    st.markdown('<p style="text-align: center; font-size: 0.9em;">Já tenho uma conta. Entrar.</p>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


# --- 3. Renderização da Tela de Perfil ---
def render_profile_page():
    # Obtém dados do usuário (Lógica de Negócio)
    user = get_logged_user()
    info_basica = user.get_info_basica()
    detalhes = user.get_perfil_detalhes()

    # Título e Contador
    st.markdown(f'<div style="color: {COR_BRILHO}; font-size: 2.5em; font-weight: bold;">PERSONALYTE</div>', unsafe_allow_html=True)
    st.markdown("18 • Conecte-se além das aparências")
    st.markdown(f'<div style="position: absolute; top: 10px; right: 20px; color:{COR_BRILHO}; font-size: 20px;">3</div>', unsafe_allow_html=True)

    # Card Principal
    st.markdown(f'<div style="background-color: {COR_DESTAQUE}; padding: 20px; border-radius: 10px; margin-top: 30px; text-align: center;">', unsafe_allow_html=True)

    # Ícone
    try:
        icone = Image.open("icone_personalidade.png")
        st.image(icone, width=150)
    except FileNotFoundError:
        st.markdown('<div style="height:150px; color:white; font-size:40px;">[ÍCONE]</div>', unsafe_allow_html=True)

    st.markdown(f'<p style="font-size: 1.5em; font-weight: bold;">{detalhes["usuario"]}</p>', unsafe_allow_html=True)

    # Detalhes do Perfil
    st.markdown(f"""
        <ul style="list-style-type: none; text-align: left;">
            <li>• {info_basica[0]}</li>
            <li>• {info_basica[1]}</li>
            <li>• Características: {detalhes["caracteristicas"]}</li>
            <li>• Personalidade: {detalhes["personalidade"]}</li>
        </ul>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # Botões de Ação
    col_x, col_center, col_heart = st.columns([1, 1, 1])

    with col_x:
        st.markdown(f'<style>div[data-testid="stButton"] button:nth-of-type(1) {{background-color: {COR_BTN_X}; height: 80px; width: 80px; border-radius: 50%; font-size: 30px;}}</style>', unsafe_allow_html=True)
        st.button("X", key="reject")

    with col_heart:
        st.markdown(f'<style>div[data-testid="stButton"] button:nth-of-type(2) {{background-color: {COR_BRILHO}; height: 80px; width: 80px; border-radius: 50%; font-size: 30px;}}</style>', unsafe_allow_html=True)
        st.button("❤️", key="like")

    st.button("<< Logout", on_click=go_to_login)

# --- LOOP PRINCIPAL ---
if st.session_state.page == 'login':
    render_login_page()
elif st.session_state.page == 'profile':
    render_profile_page()