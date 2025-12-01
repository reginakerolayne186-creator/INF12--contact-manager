# ui.py
from models import Contact, BusinessContact
import persistence

def list_contacts(contacts):
    if not contacts:
        print("Nenhum contato cadastrado.")
        return
    for i, c in enumerate(contacts, start=1):
        print(f"{i}. {c.display()}")

def add_contact(contacts):
    kind = input("Tipo (p)essoal ou (c)omercial? [p/c]: ").strip().lower()
    name = input("Nome: ").strip()
    phone = input("Telefone: ").strip()
    email = input("Email (opcional): ").strip()
    if kind == "c":
        company = input("Empresa: ").strip()
        contact = BusinessContact(name, phone, company, email)
    else:
        contact = Contact(name, phone, email)
    contacts.append(contact)
    persistence.save_contacts(persistence.objects_to_dicts(contacts))
    print("Contato adicionado!")

def remove_contact(contacts):
    list_contacts(contacts)
    if not contacts:
        return
    try:
        idx = int(input("Digite o número do contato para remover: "))
        if 1 <= idx <= len(contacts):
            removed = contacts.pop(idx - 1)
            persistence.save_contacts(persistence.objects_to_dicts(contacts))
            print(f"Removido: {removed.display()}")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida.")

def menu_loop():
    raw = persistence.load_contacts()
    contacts = persistence.dicts_to_objects(raw)
    while True:
        print("\n=== Contact Manager ===")
        print("1. Listar contatos")
        print("2. Adicionar contato")
        print("3. Remover contato")
        print("4. Sair")
        choice = input("Escolha: ").strip()
        if choice == "1":
            list_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            remove_contact(contacts)
        elif choice == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")
