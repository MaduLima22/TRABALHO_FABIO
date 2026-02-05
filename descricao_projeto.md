# TRABALHO DE DESENVOLVIMENTO DE APLICAÇÃO CRUD EM PYTHON

## TEMA ESCOLHIDO: Gerenciador de Afazeres Semanais

---

## O QUE O SISTEMA FAZ:

Este sistema permite gerenciar uma rotina semanal de afazeres/tarefas de forma simples e organizada. O usuário pode:

• **Adicionar novos afazeres** indicando descrição, dia da semana e horário
• **Visualizar todos os afazeres cadastrados** - ordenados automaticamente por dia da semana e horário
• **Buscar um afazer específico** pelo ID
• **Atualizar informações de afazeres** (descrição, dia, horário) com confirmação antes de alterações
• **Marcar afazeres como concluídos ou pendentes**
• **Deletar afazeres individuais** que não são mais necessários
• **Apagar todos os afazeres de uma vez** com dupla confirmação de segurança
• **Voltar ao menu principal** a qualquer momento usando a opção "0"

O objetivo é ajudar na organização da rotina diária, permitindo visualizar rapidamente o que precisa ser feito em cada dia da semana.

---

## COMO O CRUD FOI APLICADO:

### ✓ CREATE (Criar):
- **Função criar()** - Adiciona novos afazeres à lista, solicitando descrição, dia da semana e horário
- O ID é gerado automaticamente usando `max([item['id'] for item in lista], default=0) + 1`
- O horário é formatado automaticamente no padrão HH:MM (ex: 8 vira 08:00)
- Permite cancelar a operação digitando "0" em qualquer etapa

### ✓ READ (Ler):
- **Função listar()** - Exibe todos os afazeres cadastrados com formatação organizada
  - Ordenação automática: primeiro por dia da semana (seg-dom), depois por horário
  - Indicação de status (✓ Concluído / ○ Pendente)
- **Função ler()** - Busca e retorna um afazer específico pelo ID

### ✓ UPDATE (Atualizar):
- **Função atualizar()** - Permite modificar:
  - Descrição (com exibição da descrição atual e confirmação antes de alterar)
  - Dia da semana
  - Horário (com formatação automática HH:MM)
  - Status de conclusão
- Permite voltar ao menu a qualquer momento digitando "0"

### ✓ DELETE (Deletar):
- **Função deletar()** - Remove um afazer específico após confirmação
- **Função deletar_todos()** - Remove todos os afazeres com dupla confirmação de segurança:
  - 1ª confirmação: digitar "DELETAR TUDO"
  - 2ª confirmação: digitar "sim"
  - Mostra quantidade de afazeres sendo deletados
  - Avisa que a ação é permanente e não pode ser desfeita

### ✓ PERSISTÊNCIA:
- **Função carregar()** - Lê os dados do arquivo JSON ao iniciar
- **Função salvar()** - Grava os dados no arquivo JSON após modificações

---

## NOVAS FUNCIONALIDADES IMPLEMENTADAS:

### 1. Ordenação Automática por Dia e Horário
- Nova função `ordenar_afazeres()` que organiza todos os afazeres por:
  - Dia da semana (Segunda → Domingo)
  - Horário (00:00 → 23:59)
- Aplicada automaticamente ao listar afazeres

### 2. Formatação Automática de Horário
- Nova função `formatar_horario()` que aceita:
  - Apenas hora: `8` → `08:00`
  - Hora com minutos: `14:30` → `14:30`
  - Formatos já corretos: `08:30` → `08:30`
- Validação: horas de 0-23 e minutos de 0-59
- Aplicada ao criar e atualizar afazeres

### 3. Opção de Retornar ao Menu ("0 para voltar")
- Implementada em todas as operações:
  - Ao adicionar novo afazer (em cada etapa: descrição, dia, horário)
  - Ao atualizar afazer (escolha do ID e submenu de opções)
  - Ao deletar afazer (escolha do ID)
  - Ao buscar afazer por ID
- Permite cancelar operações sem salvar alterações

### 4. Confirmação antes de Alterar Descrição
- Ao atualizar descrição, o sistema:
  - Exibe a descrição atual
  - Pergunta se deseja alterar (sim/não)
  - Só confirma após resposta positiva

### 5. Opção de Apagar Todos os Afazeres
- Nova opção "6" no menu principal
- Sistema de segurança com dupla confirmação:
  - Aviso da quantidade de afazeres a deletar
  - Primeira confirmação: digitar "DELETAR TUDO"
  - Segunda confirmação: digitar "sim"
  - Confirmação final mostrando quantidade deletada
- Evita exclusões acidentais

---

## ESTRUTURAS DE DADOS UTILIZADAS:

• **LISTA**: Armazena todos os afazeres (lista_afazeres)
• **DICIONÁRIO**: Cada afazer é representado com as chaves:
  - `id`: Identificador único (inteiro)
  - `descricao`: Texto descrevendo a tarefa
  - `dia_semana`: Dia da semana (string)
  - `horario`: Horário no formato HH:MM (string)
  - `concluido`: Status (booleano)
• **ARQUIVO JSON**: Arquivo "afazeres.json" para armazenamento persistente

---

## TRATAMENTO DE ERROS:

O sistema implementa validação robusta para:

• IDs inválidos (não numéricos)
• IDs inexistentes
• Campos obrigatórios vazios (descrição e horário)
• Opções de menu inválidas
• Horários inválidos (horas > 23 ou minutos > 59)
• Dias da semana inválidos
• Confirmações de segurança (deletar todos)

---

## COMO USAR:

### Passo a Passo:

1. **Execute o arquivo app.py**
   ```
   python app.py
   ```

2. **Interact com o menu principal:**
   - Opção **1**: Ver todos os afazeres (ordenados por dia e horário)
   - Opção **2**: Adicionar novo afazer (com formatação automática de horário)
   - Opção **3**: Buscar afazer por ID
   - Opção **4**: Editar afazer (com confirmação em alterações críticas)
   - Opção **5**: Excluir afazer individual
   - Opção **6**: Apagar todos os afazeres (com dupla confirmação)
   - Opção **0**: Sair do programa

3. **Formato de Entrada para Horário:**
   - Digite apenas a hora: `8` (será convertido para `08:00`)
   - Digite hora e minuto: `14:30` (será formatado se necessário)
   - Sistema aceita horas de 0 a 23 e minutos de 0 a 59

4. **Para Voltar ao Menu:**
   - Digite `0` em qualquer campo de entrada durante operações
   - Operação será cancelada e você retornará ao menu principal

5. **Dados Persistentes:**
   - Os dados são salvos automaticamente no arquivo `afazeres.json`
   - Todas as alterações são registradas permanentemente

---

## RESUMO DAS MELHORIAS:

✅ Sistema de ordenação automática por dia da semana e horário  
✅ Formatação automática de horários no padrão HH:MM  
✅ Opção para voltar ao menu em todas as operações  
✅ Confirmação antes de alterar informações críticas  
✅ Opção para apagar todos os afazeres com segurança dupla  
✅ Validação robusta de entrada de dados  
✅ Interface amigável com emojis informativos  
✅ Sistema de persistência de dados em JSON  

---

**Versão Final**: Fevereiro de 2026  
**Status**: ✓ Concluído com todas as funcionalidades solicitadas
