🔗 Versão Inicial do Projeto

Este sistema é uma evolução da primeira versão desenvolvida durante o processo de aprendizado e prototipação.

Repositório da versão inicial:
https://github.com/alexspereira27/Projeto_DEV)

# Sistema de Vendas - Bytenordeste

Um sistema de gestão de vendas e atendimentos desenvolvido em Python com interface gráfica moderna usando **CustomTkinter** e banco de dados **SQLite**.

## 🎯 Funcionalidades

### 1. **Autenticação de Usuários**
- Login seguro com autenticação em banco de dados
- Suporte para dois níveis de acesso:
  - **Vendedor**: Acesso restrito ao registro de atendimentos
  - **Supervisor**: Acesso completo incluindo visualização de relatórios

### 2. **Gerenciamento de Clientes**
- Busca de clientes por código
- Visualização de informações (nome, telefone, e-mail)
- Registro de novo atendimento para cliente existente

### 3. **Registro de Atendimentos**
- Tipo de atendimento: Telefone ou Visita
- Registrar compra ou motivo de não compra
- Campos dinamicamente adaptáveis:
  - **Se comprou**: Produto, Preço, Forma de Pagamento, Observação
  - **Se não comprou**: Motivo da recusa

### 4. **Relatórios e Exportação**
- Visualização do histórico completo de atendimentos (supervisor)
- Filtros por cliente e vendedor
- Exportação para **PDF** em formato de relatório profissional
- Tabela com todas as informações de atendimentos

### 5. **Interface Moderna**
- Tema escuro com cores personalizadas
- Design responsivo com CustomTkinter
- Elementos interativos com feedback visual

---

## 📋 Requisitos

- Python 3.8+
- Bibliotecas necessárias:

```bash
pip install customtkinter
pip install reportlab
```

---

## 🗂️ Estrutura do Projeto

```
versao-final/
├── app.py                      # App de login simples (exemplo inicial)
├── app_rap                     # App principal completo
├── banco clientes              # Script para criar/popular banco de clientes
├── banco vendedores            # Script para criar/popular banco de vendedores
├── login vendedores            # App de login para vendedores
├── clientes.db                 # Banco de dados de clientes (gerado)
├── vendedores.db               # Banco de dados de vendedores (gerado)
└── README.md                   # Este arquivo
```

---

## 🚀 Como Usar

### 1. **Inicializar os Bancos de Dados**

Execute os scripts de banco de dados para criar as tabelas e inserir dados iniciais:

```bash
# Criar banco de clientes
python "banco clientes"

# Criar banco de vendedores
python "banco vendedores"
```

### 2. **Executar o Sistema**

```bash
python app_rap
```

### 3. **Fazer Login**

**Supervisor:**
- Usuário: `kaio`
- Código: `2530`

**Vendedor:**
- Configure novos vendedores através dos scripts de banco de dados

---

## 🗄️ Estrutura do Banco de Dados

### Tabela: `clientes`
```
├── codigo (INTEGER) - Chave primária
├── nome (TEXT)
├── fone (INTEGER)
└── email (TEXT)
```

### Tabela: `vendedores`
```
├── nome (TEXT)
└── codigo (TEXT)
```

### Tabela: `supervisor`
```
├── nome (TEXT)
└── codigo (TEXT)
```

### Tabela: `historico_atendimentos`
```
├── id (INTEGER) - Chave primária
├── data_hora (TEXT)
├── codigo_cliente (INTEGER)
├── nome_cliente (TEXT)
├── vendedor (TEXT)
├── tipo_atendimento (TEXT)
├── comprou (TEXT)
├── produto (TEXT)
├── preco (TEXT)
├── pagamento (TEXT)
├── observacao (TEXT)
└── motivo (TEXT)
```

---

## 📊 Fluxo de Funcionamento

```
┌─────────────────┐
│  Tela de Login  │
└────────┬────────┘
         │
    ┌────▼────────────┐
    │ Validação BD    │
    └────┬────────────┘
         │
    ┌────▼──────────────────────┐
    │ Supervisor? ┌─ SIM ────────┐
    └────┬───────┘              │
         │ NÃO                  │
    ┌────▼──────────────────┐   │
    │ Sistema Vendedor      │   │
    │ - Buscar cliente      │   │
    │ - Registrar venda     │   │
    │ - Salvar atendimento  │   │
    └───────────────────────┘   │
                                │
                        ┌───────▼──────────────┐
                        │ Sistema Supervisor   │
                        │ - Ver Relatórios     │
                        │ - Filtrar dados      │
                        │ - Exportar PDF       │
                        └──────────────────────┘
```

---

## 🎨 Temas e Cores

- **Modo**: Escuro
- **Tema Principal**: Azul
- **Cores Especiais**:
  - Verde: Salvar e sucesso (`#27ae60`)
  - Vermelho: Exportar PDF (`#c0392b`)
  - Cinza: Navegação (`#34495e`)
  - Verde neon: Informações do vendedor (`#00ff88`)

---

## 💾 Exportação de PDF

O sistema gera relatórios em PDF com:
- Tabela formatada com todas as colunas
- Cabeçalho azul escuro
- Alternância de cores nas linhas
- Suporte a quebra de texto automática
- Tamanho de página: A4 Paisagem

**Arquivo gerado**: `relatorio_atendimentos.pdf`

---

## 🔒 Segurança

- Senhas de vendedor criptografadas com `show="*"` na interface
- Consultas paramétrizadas ao SQLite (proteção contra SQL Injection)
- Validações de entrada em todos os campos

---

## 📝 Exemplo de Uso

### Registrar um Atendimento

1. Faça login com credenciais de vendedor
2. Digite o código do cliente na busca
3. Clique em "Pesquisar" para carregar dados
4. Selecione o tipo de atendimento
5. Indique se houve compra:
   - **SIM**: Preencha produto, preço, pagamento e observação
   - **NÃO**: Preencha o motivo da recusa
6. Clique em "SALVAR ATENDIMENTO"

### Consultar Relatórios (Supervisor)

1. Faça login com credenciais de supervisor
2. Clique em "VER RELATÓRIOS"
3. Use os filtros para buscar por cliente ou vendedor
4. Clique em "EXPORTAR PDF" para gerar relatório

---

## 🛠️ Melhorias Futuras

- [ ] Autenticação com hash de senha
- [ ] Backup automático de banco de dados
- [ ] Gráficos de desempenho de vendas
- [ ] Sistema de comissões
- [ ] Notificações de follow-up
- [ ] Integração com email
- [ ] Estatísticas por período

---

## 📧 Contato

Desenvolvido por: **Byte Nordeste**
