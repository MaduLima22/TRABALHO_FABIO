# EXPLICAÇÃO DO TRABALHO - APLICAÇÃO CRUD EM PYTHON

**ALUNO:** MARIA EDUARDA LIMA SILVEIRA  
**TURMA:** ADS 2° SEMESTRE 2025  
**PROFESSOR:** FÁBIO OLIVEIRA

---

# TRABALHO DE DESENVOLVIMENTO DE APLICAÇÃO CRUD EM PYTHON

## TEMA ESCOLHIDO: Gerenciador de Afazeres Semanais

---

## O QUE O SISTEMA FAZ:

Este sistema permite gerenciar uma rotina semanal de afazeres e tarefas de forma simples e organizada. O usuário pode:

- Adicionar novos afazeres indicando descrição, dia da semana e horário
- Visualizar todos os afazeres cadastrados, que aparecem ordenados automaticamente por dia da semana e horário
- Buscar um afazer específico pelo ID
- Atualizar informações de afazeres (descrição, dia, horário) com confirmação antes de fazer alterações
- Marcar afazeres como concluídos ou pendentes
- Deletar afazeres individuais que não são mais necessários
- Apagar todos os afazeres de uma vez com dupla confirmação de segurança
- Voltar ao menu principal a qualquer momento usando a opção "0"

O objetivo principal é ajudar na organização da rotina diária, permitindo visualizar rapidamente o que precisa ser feito em cada dia da semana.

---

## COMO O CRUD FOI APLICADO:

### CREATE (Criar):

**Função criar()** - Adiciona novos afazeres à lista, solicitando descrição, dia da semana e horário. O ID é gerado automaticamente usando `max([item['id'] for item in lista], default=0) + 1`, o que garante que cada afazer tenha um identificador único. O horário é formatado automaticamente no padrão HH:MM (por exemplo, se o usuário digitar apenas "8", o sistema converte para "08:00"). Também é possível cancelar a operação digitando "0" em qualquer etapa.

### READ (Ler):

**Função listar()** - Exibe todos os afazeres cadastrados com formatação organizada. A lista é ordenada automaticamente, primeiro por dia da semana (de segunda a domingo) e depois por horário (de 00:00 a 23:59). Cada afazer mostra se está concluído ou pendente.

**Função ler()** - Busca e retorna um afazer específico pelo ID, permitindo visualizar os detalhes de uma tarefa individual.

### UPDATE (Atualizar):

**Função atualizar()** - Permite modificar diferentes aspectos de um afazer:
- **Descrição**: O sistema mostra a descrição atual e pergunta se você tem certeza que quer alterá-la, evitando mudanças acidentais
- **Dia da semana**: Permite trocar o dia em que a tarefa deve ser realizada
- **Horário**: Aceita novo horário com formatação automática no padrão HH:MM
- **Status de conclusão**: Alterna entre concluído e pendente

Todas as operações de atualização permitem voltar ao menu digitando "0" a qualquer momento.

### DELETE (Deletar):

**Função deletar()** - Remove um afazer específico após pedir confirmação do usuário. Mostra qual tarefa será deletada e pede que o usuário digite "sim" para confirmar.

**Função deletar_todos()** - Remove todos os afazeres de uma vez. Por ser uma ação crítica, usa um sistema de segurança com dupla confirmação:
1. Mostra a quantidade de afazeres que serão deletados
2. Pede para digitar "DELETAR TUDO" como primeira confirmação
3. Pede para digitar "sim" como segunda confirmação
4. Avisa que a ação é permanente e não pode ser desfeita

Isso evita exclusões acidentais de todos os dados.

### PERSISTÊNCIA DE DADOS:

**Função carregar()** - Lê os dados do arquivo JSON quando o programa inicia, recuperando todos os afazeres salvos anteriormente.

**Função salvar()** - Grava os dados no arquivo JSON após qualquer modificação (criar, atualizar ou deletar). Isso garante que as informações não sejam perdidas quando o programa é fechado.

---

## NOVAS FUNCIONALIDADES IMPLEMENTADAS:

### 1. Ordenação Automática por Dia e Horário

Foi criada a função `ordenar_afazeres()` que organiza automaticamente todos os afazeres seguindo duas regras:
- Primeiro ordena por dia da semana (segunda-feira vem antes de terça, e assim por diante até domingo)
- Depois ordena por horário dentro de cada dia (00:00 vem antes de 23:59)

Essa ordenação é aplicada automaticamente sempre que o usuário lista os afazeres, facilitando a visualização da rotina semanal de forma cronológica.

### 2. Formatação Automática de Horário

A função `formatar_horario()` aceita diferentes formas de entrada e converte tudo para o padrão HH:MM:
- Se digitar apenas a hora (ex: "8"), converte para "08:00"
- Se digitar hora e minuto (ex: "14:30"), mantém no formato correto "14:30"
- Se já estiver formatado (ex: "08:30"), apenas valida e confirma

O sistema também valida se a hora está entre 0 e 23 e se os minutos estão entre 0 e 59. Essa formatação é aplicada tanto ao criar quanto ao atualizar afazeres.

### 3. Opção de Retornar ao Menu ("0 para voltar")

Em todas as operações do sistema, o usuário pode digitar "0" para cancelar e voltar ao menu principal:
- Ao adicionar novo afazer (em qualquer etapa: descrição, dia ou horário)
- Ao atualizar afazer (na escolha do ID ou no submenu de opções)
- Ao deletar afazer (na escolha do ID)
- Ao buscar afazer por ID

Isso dá mais controle para o usuário, permitindo cancelar operações sem salvar alterações indesejadas.

### 4. Confirmação antes de Alterar Descrição

Quando o usuário escolhe atualizar a descrição de um afazer, o sistema:
1. Mostra a descrição atual na tela
2. Pergunta se tem certeza que quer alterar (esperando resposta "sim" ou "não")
3. Só permite a alteração após confirmação positiva

Isso evita que o usuário altere informações importantes por engano.

### 5. Opção de Apagar Todos os Afazeres

Foi adicionada a opção "6" no menu principal que permite apagar todos os afazeres de uma vez. Como é uma ação que não pode ser desfeita, o sistema usa um esquema de segurança robusto:
- Avisa quantos afazeres existem e serão deletados
- Primeira confirmação: pede para digitar exatamente "DELETAR TUDO"
- Segunda confirmação: pede para digitar "sim"
- Ao final, mostra quantos afazeres foram deletados

Esse sistema de dupla confirmação praticamente elimina o risco de exclusões acidentais.

---

## ESTRUTURAS DE DADOS UTILIZADAS:

### Lista Python
Armazena todos os afazeres em uma variável chamada `lista_afazeres`. A lista permite adicionar, remover e iterar sobre os afazeres facilmente.

### Dicionário Python
Cada afazer individual é representado por um dicionário contendo cinco chaves:
- `id`: Número inteiro que identifica unicamente cada afazer
- `descricao`: Texto que descreve a tarefa a ser realizada
- `dia_semana`: String com o dia da semana ("Segunda-feira", "Terça-feira", etc.)
- `horario`: String no formato HH:MM representando a hora da tarefa
- `concluido`: Booleano (True ou False) indicando se a tarefa foi concluída

### Arquivo JSON
O arquivo "afazeres.json" é usado para armazenamento persistente. Toda vez que há uma mudança nos dados, o arquivo é atualizado, e quando o programa inicia, ele carrega os dados do arquivo.

---

## TRATAMENTO DE ERROS:

O sistema foi desenvolvido com validações robustas para lidar com diferentes situações de erro:

- **IDs inválidos**: Se o usuário digitar letras ou caracteres especiais quando o sistema espera um número, uma mensagem de erro é exibida
- **IDs inexistentes**: Se tentar buscar um afazer com ID que não existe, o sistema informa que não encontrou
- **Campos vazios**: Se o usuário deixar descrição ou horário em branco, o sistema pede para preencher
- **Opções de menu inválidas**: Se escolher uma opção que não existe no menu, mostra mensagem de erro
- **Horários inválidos**: Se digitar hora maior que 23 ou minutos maiores que 59, o sistema recusa e pede um horário válido
- **Dias da semana inválidos**: Se escolher um número fora do intervalo 1-7 para dia da semana, informa que é inválido
- **Confirmações de segurança**: O sistema verifica se o usuário digitou exatamente o texto esperado nas confirmações

---

## COMO USAR O SISTEMA:

### Passo 1: Executar o Programa

Abra o terminal ou prompt de comando na pasta do projeto e execute:
```
python app.py
```

### Passo 2: Navegar pelo Menu Principal

O menu oferece 7 opções:

- **Opção 1 - Listar todos os afazeres**: Mostra todos os afazeres ordenados por dia da semana e horário. É bom usar essa opção primeiro para ver quais tarefas já estão cadastradas.

- **Opção 2 - Criar novo afazer**: Adiciona uma nova tarefa. O sistema vai pedir a descrição, o dia da semana (escolhendo de 1 a 7) e o horário. Você pode digitar o horário de forma simples (ex: "8" ou "14:30") que o sistema formata automaticamente.

- **Opção 3 - Ler afazer por ID**: Permite ver os detalhes completos de uma tarefa específica. Basta informar o número do ID.

- **Opção 4 - Atualizar afazer**: Modifica um afazer existente. Primeiro escolhe qual afazer pelo ID, depois escolhe o que quer mudar (descrição, dia, horário ou status).

- **Opção 5 - Deletar afazer**: Remove uma tarefa específica. O sistema pede confirmação antes de deletar.

- **Opção 6 - Apagar todos os afazeres**: Remove todas as tarefas de uma vez. Use com cuidado pois essa ação não pode ser desfeita. O sistema pede duas confirmações para garantir que você realmente quer fazer isso.

- **Opção 0 - Sair**: Fecha o programa.

### Passo 3: Inserir Horários

Quando o sistema pedir um horário, você pode digitar de várias formas:
- Apenas a hora: digite "8" (o sistema converte para "08:00")
- Hora e minuto: digite "14:30" (o sistema aceita como está)
- Formatos já completos: digite "08:30" (o sistema mantém)

O sistema só aceita horas de 0 a 23 e minutos de 0 a 59.

### Passo 4: Usar a Opção de Voltar

Em qualquer momento durante uma operação (criar, atualizar, deletar, buscar), você pode digitar "0" para cancelar e voltar ao menu principal. Isso é útil se mudar de ideia no meio de uma operação.

### Passo 5: Persistência dos Dados

Todos os dados são salvos automaticamente no arquivo `afazeres.json`. Não é necessário fazer nenhuma ação especial para salvar. Quando você fechar o programa e abrir novamente, todas as tarefas estarão lá.

---

## RESUMO DAS MELHORIAS IMPLEMENTADAS:

Todas as funcionalidades abaixo foram adicionadas ao projeto base:

- Sistema de ordenação automática por dia da semana e horário
- Formatação automática de horários no padrão HH:MM
- Opção para voltar ao menu principal em todas as operações
- Confirmação antes de alterar informações críticas como descrição
- Opção para apagar todos os afazeres com sistema de segurança dupla
- Validação robusta de todos os dados inseridos pelo usuário
- Interface clara com mensagens informativas
- Sistema completo de persistência de dados em arquivo JSON

---

**Versão Final**: Fevereiro de 2026  
**Status**: Concluído com todas as funcionalidades solicitadas implementadas e testadas
