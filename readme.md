# PERSONALYTE: App de Relacionamento (Simulação)

##  Visão Geral do Projeto

O **PERSONALYTE** é uma simulação de um aplicativo de relacionamento focado em personalidade, implementado em Python utilizando a biblioteca Streamlit para garantir uma interface gráfica funcional no ambiente de desenvolvimento online (Replit).

O projeto foi estruturado utilizando princípios de **Programação Orientada a Objetos (POO)** para garantir a separação clara de responsabilidades entre a Interface (View), a Lógica de Negócio (Model) e a Persistência (Data).

---

## Princípios de POO e Arquitetura

Este projeto adota a separação de responsabilidades (MVC simplificado) e implementa os seguintes princípios de POO:

1.  **Encapsulamento:** As propriedades das classes de modelo (`_nome`, `_cidade`, `_cpf`, etc., na classe `Usuario`) são protegidas (prefixo `_`) e acessadas por métodos específicos (`get_info_basica`).
2.  **Herança:** A classe `Usuario` herda atributos e métodos da classe base `Pessoa`, reutilizando a lógica de informações básicas.
3.  **Abstração:** A classe `Pessoa` é uma abstração para qualquer entidade humana no sistema, e o arquivo `main.py` abstrai a complexidade do Streamlit, focando apenas em quais funções de `render` chamar.
4.  **Polimorfismo (Implícito):** Embora simples, o método `get_perfil_detalhes` na classe `Usuario` retorna detalhes específicos que seriam sobrescritos ou adaptados se houvesse outras subclasses de `Pessoa` (ex: `Administrador`).

---

## 📂 Estrutura de Pastas
Bibliotecas Utilizadas

| Nome da Biblioteca | Versão Mínima | Detalhe |
| :--- | :--- | :--- |
| **streamlit** | `1.0.0` | Utilizada para construir a interface gráfica web, garantindo o funcionamento no ambiente Replit. |
| **Pillow (PIL)** | `9.0.0` | Utilizada para carregar e exibir o arquivo de imagem PNG (`icone_personalidade.png`) no Streamlit. |

---

## 📸 Demonstração do Programa

As imagens a seguir demonstram as duas telas da aplicação funcionando em tempo real.

### 1. Tela de Login / Cadastro

Esta tela utiliza um gradiente de laranja e oferece campos para Email, Senha e CPF, com botões para navegação.



### 2. Tela de Perfil

Esta tela exibe o perfil do usuário logado, utilizando as cores Laranja, Amarelo e Vermelho, com o ícone central (coração/cérebro) e botões de ação (X e Coração).



---

## 💾 Histórico de Commits (Exemplo)

Para atender ao requisito de 5 commits, a seguinte sequência de commits deve ser seguida:

1.  `feat: Inicializa projeto com estrutura de pastas e .replit`
2.  `refactor(styles): Criação de styles.py e aplicação de cores globais`
3.  `feat(model): Implementa classes Usuario e Pessoa (Herança/Encapsulamento)`
4.  `feat(login): Implementa tela de Login/Cadastro em main.py com navegação`
5.  `feat(profile): Implementa tela de Perfil, usa classes de modelo e adiciona botões de ação`