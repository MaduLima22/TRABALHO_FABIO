import json
import os

# ========== FUNÇÕES CRUD ==========

def carregar():
    """Carrega os dados do arquivo JSON"""
    if os.path.exists("afazeres.json"):
        try:
            with open("afazeres.json", "r", encoding="utf-8") as arquivo:
                return json.load(arquivo)
        except:
            return []
    return []

def salvar(lista):
    """Salva a lista no arquivo JSON"""
    with open("afazeres.json", "w", encoding="utf-8") as arquivo:
        json.dump(lista, arquivo, indent=2, ensure_ascii=False)
    print("✓ Dados salvos com sucesso!")

def ordenar_afazeres(lista):
    """Ordena a lista por dia da semana e horário"""
    # Mapeamento de dias da semana para ordenação
    ordem_dias = {
        "Segunda-feira": 1,
        "Terça-feira": 2,
        "Quarta-feira": 3,
        "Quinta-feira": 4,
        "Sexta-feira": 5,
        "Sábado": 6,
        "Domingo": 7
    }
    
    # Ordena primeiro por dia da semana, depois por horário
    return sorted(lista, key=lambda x: (ordem_dias.get(x['dia_semana'], 999), x['horario']))

def listar(lista):
    """Lista todos os afazeres ordenados por dia da semana e horário"""
    if len(lista) == 0:
        print("\n📋 Nenhum afazer cadastrado ainda.")
        return

    # Ordena a lista antes de exibir
    lista_ordenada = ordenar_afazeres(lista)

    print("\n" + "="*60)
    print("📋 SEUS AFAZERES SEMANAIS (Ordenados por Dia e Horário)")
    print("="*60)
    for item in lista_ordenada:
        status = "✓" if item["concluido"] else "○"
        print(f"[{status}] ID: {item['id']} | Dia: {item['dia_semana']}")
        print(f"    Tarefa: {item['descricao']}")
        print(f"    Horário: {item['horario']}")
        print("-"*60)

def criar(lista):
    """Cria um novo afazer"""
    print("\n➕ ADICIONAR NOVO AFAZER")
    print("-"*40)

    # Solicita descrição
    descricao = input("Descrição da tarefa (0 para voltar): ").strip()
    if descricao == "0":
        print("❌ Operação cancelada. Voltando ao menu...")
        return
    if not descricao:
        print("❌ A descrição não pode estar vazia!")
        return

    # Solicita dia da semana
    print("\nDias disponíveis:")
    print("1-Segunda  2-Terça  3-Quarta  4-Quinta")
    print("5-Sexta  6-Sábado  7-Domingo")

    dias = {
        "1": "Segunda-feira", "2": "Terça-feira", 
        "3": "Quarta-feira", "4": "Quinta-feira",
        "5": "Sexta-feira", "6": "Sábado", "7": "Domingo"
    }

    opcao_dia = input("Escolha o dia (1-7, ou 0 para voltar): ").strip()
    if opcao_dia == "0":
        print("❌ Operação cancelada. Voltando ao menu...")
        return
    if opcao_dia not in dias:
        print("❌ Opção de dia inválida!")
        return

    # Solicita horário
    horario = input("Horário (ex: 08:00, ou 0 para voltar): ").strip()
    if horario == "0":
        print("❌ Operação cancelada. Voltando ao menu...")
        return
    if not horario:
        print("❌ O horário não pode estar vazio!")
        return

    # Gera ID automático
    novo_id = max([item['id'] for item in lista], default=0) + 1

    # Cria o novo item
    novo_item = {
        "id": novo_id,
        "descricao": descricao,
        "dia_semana": dias[opcao_dia],
        "horario": horario,
        "concluido": False
    }

    lista.append(novo_item)
    salvar(lista)
    print(f"\n✓ Afazer '{descricao}' adicionado com ID {novo_id}!")

def ler(lista, id_busca):
    """Busca e retorna um afazer pelo ID"""
    for item in lista:
        if item["id"] == id_busca:
            return item
    return None

def atualizar(lista):
    """Atualiza um afazer existente"""
    print("\n✏️ ATUALIZAR AFAZER")
    print("-"*40)

    id_input = input("Digite o ID do afazer (0 para voltar): ").strip()
    if id_input == "0":
        print("❌ Operação cancelada. Voltando ao menu...")
        return
    
    try:
        id_busca = int(id_input)
    except ValueError:
        print("❌ ID inválido! Digite apenas números.")
        return

    item = ler(lista, id_busca)

    if item is None:
        print(f"❌ Afazer com ID {id_busca} não encontrado!")
        return

    print(f"\n📝 Afazer encontrado: {item['descricao']}")
    print("\nO que deseja atualizar?")
    print("1 - Descrição")
    print("2 - Dia da semana")
    print("3 - Horário")
    print("4 - Marcar como concluído/pendente")
    print("0 - Voltar ao menu")

    opcao = input("Escolha (0-4): ").strip()

    if opcao == "0":
        print("❌ Operação cancelada. Voltando ao menu...")
        return

    elif opcao == "1":
        print(f"\n📄 Descrição atual: {item['descricao']}")
        confirma = input("Deseja alterar a descrição? (sim/não): ").strip().lower()
        
        if confirma == "sim":
            nova_desc = input("Nova descrição: ").strip()
            if nova_desc:
                item["descricao"] = nova_desc
                print("✓ Descrição atualizada!")
            else:
                print("❌ Descrição não pode estar vazia!")
                return
        else:
            print("❌ Alteração cancelada.")
            return

    elif opcao == "2":
        print("\nDias disponíveis:")
        print("1-Segunda  2-Terça  3-Quarta  4-Quinta")
        print("5-Sexta  6-Sábado  7-Domingo")

        dias = {
            "1": "Segunda-feira", "2": "Terça-feira", 
            "3": "Quarta-feira", "4": "Quinta-feira",
            "5": "Sexta-feira", "6": "Sábado", "7": "Domingo"
        }

        opcao_dia = input("Novo dia (1-7, ou 0 para cancelar): ").strip()
        if opcao_dia == "0":
            print("❌ Operação cancelada.")
            return
        if opcao_dia in dias:
            item["dia_semana"] = dias[opcao_dia]
            print("✓ Dia atualizado!")
        else:
            print("❌ Opção inválida!")
            return

    elif opcao == "3":
        novo_horario = input("Novo horário (ou 0 para cancelar): ").strip()
        if novo_horario == "0":
            print("❌ Operação cancelada.")
            return
        if novo_horario:
            item["horario"] = novo_horario
            print("✓ Horário atualizado!")
        else:
            print("❌ Horário não pode estar vazio!")
            return

    elif opcao == "4":
        item["concluido"] = not item["concluido"]
        status = "concluído" if item["concluido"] else "pendente"
        print(f"✓ Status alterado para: {status}!")

    else:
        print("❌ Opção inválida!")
        return

    salvar(lista)

def deletar(lista):
    """Remove um afazer da lista"""
    print("\n🗑️ DELETAR AFAZER")
    print("-"*40)

    id_input = input("Digite o ID do afazer para deletar (0 para voltar): ").strip()
    if id_input == "0":
        print("❌ Operação cancelada. Voltando ao menu...")
        return
    
    try:
        id_busca = int(id_input)
    except ValueError:
        print("❌ ID inválido! Digite apenas números.")
        return

    item = ler(lista, id_busca)

    if item is None:
        print(f"❌ Afazer com ID {id_busca} não encontrado!")
        return

    print(f"\n⚠️ Tem certeza que deseja deletar: '{item['descricao']}'?")
    confirma = input("Digite 'sim' para confirmar: ").strip().lower()

    if confirma == "sim":
        lista.remove(item)
        salvar(lista)
        print("✓ Afazer deletado com sucesso!")
    else:
        print("❌ Operação cancelada.")

# ========== MENU PRINCIPAL ==========

def menu():
    """Exibe o menu e gerencia as opções"""
    lista_afazeres = carregar()

    while True:
        print("\n" + "="*60)
        print("📅 GERENCIADOR DE AFAZERES SEMANAIS")
        print("="*60)
        print("1 - Listar todos os afazeres")
        print("2 - Criar novo afazer")
        print("3 - Ler afazer por ID")
        print("4 - Atualizar afazer")
        print("5 - Deletar afazer")
        print("0 - Sair")
        print("="*60)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            listar(lista_afazeres)

        elif opcao == "2":
            criar(lista_afazeres)

        elif opcao == "3":
            id_input = input("\nDigite o ID (0 para voltar): ").strip()
            if id_input == "0":
                continue
            
            try:
                id_busca = int(id_input)
                item = ler(lista_afazeres, id_busca)
                if item:
                    print("\n" + "="*60)
                    status = "✓ Concluído" if item["concluido"] else "○ Pendente"
                    print(f"ID: {item['id']}")
                    print(f"Tarefa: {item['descricao']}")
                    print(f"Dia: {item['dia_semana']}")
                    print(f"Horário: {item['horario']}")
                    print(f"Status: {status}")
                    print("="*60)
                else:
                    print(f"❌ Afazer com ID {id_busca} não encontrado!")
            except ValueError:
                print("❌ ID inválido!")

        elif opcao == "4":
            atualizar(lista_afazeres)

        elif opcao == "5":
            deletar(lista_afazeres)

        elif opcao == "0":
            print("\n👋 Até logo! Boa sorte com seus afazeres!")
            break

        else:
            print("❌ Opção inválida! Tente novamente.")

# ========== EXECUÇÃO ==========

if __name__ == "__main__":
    menu()
