# 📚 Guia Prático - Preencher Diário como Professor

## TL;DR (Resumo Rápido)

```
1. Acesse: http://localhost:8000/login/
2. Login: professor1 / senha123
3. Clique: "📝 Listar Aulas"
4. Clique: "📝 Preencher Diário" em qualquer aula
5. Preencha: Presença dos alunos + dados adicionais
6. Clique: "💾 Salvar Diário"
```

---

## 🎯 Passos Detalhados

### Passo 1: Login na Plataforma

**URL**: `http://localhost:8000/login/`

```
┌─────────────────────────────────┐
│         E B D                   │
├─────────────────────────────────┤
│                                 │
│ Usuário                         │
│ [professor1____________]        │
│                                 │
│ Senha                           │
│ [senha123____________]          │
│                                 │
│ [         Entrar      ]         │
└─────────────────────────────────┘
```

**Credenciais**:
- Usuário: `professor1`
- Senha: `senha123`

Clique em **"Entrar"**

---

### Passo 2: Você Será Redirecionado para o Painel

O painel mostrará 3 cards com opções:

```
┌──────────────────────────────────────────────────────────┐
│                 📚 DIÁRIO DE AULA - PROFESSOR            │
│                                                           │
│ Bem-vindo! Aqui você pode visualizar suas aulas e        │
│ preencher o diário de cada uma.                          │
└──────────────────────────────────────────────────────────┘

┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│  📝          │  │  👥          │  │  ➕          │
│ Minhas Aulas │  │ Alunos da    │  │ Matricular   │
│              │  │ Minha Classe │  │ Aluno        │
│[Listar Aulas]│  │[Ver Alunos]  │  │[Matricular]  │
└──────────────┘  └──────────────┘  └──────────────┘
```

---

### Passo 3: Clique em "Listar Aulas"

Você verá uma tabela com TODAS as aulas da sua classe:

```
╔═══════════════╦════════════════════╦═══════════╦════════════╦══════════════╗
║ Data Prevista ║ Título da Aula     ║ Trimestre ║ Concluída? ║ Ações        ║
╠═══════════════╬════════════════════╬═══════════╬════════════╬══════════════╣
║ 27/11/2025    ║ Aula 1 - Graça     ║ 1º/2025   ║ Pendente   ║ 📝 Preencher ║
║ 28/11/2025    ║ Aula 2 - Fé        ║ 1º/2025   ║ Pendente   ║ 📝 Preencher ║
║ 29/11/2025    ║ Aula 3 - Esperança ║ 1º/2025   ║ Pendente   ║ 📝 Preencher ║
╚═══════════════╩════════════════════╩═══════════╩════════════╩══════════════╝
```

---

### Passo 4: Clique em "📝 Preencher Diário"

Para qualquer uma das aulas, clique no botão.

```
🔗 http://localhost:8000/diario/1/
```

---

### Passo 5: Você Verá o Formulário do Diário

O formulário tem 4 seções:

#### 📋 **Seção 1: Informações da Aula** (apenas leitura)

```
┌────────────────────────────────────────────┐
│ Aula: Aula 1 - Graça                       │
│ Data prevista: 27/11/2025                  │
│ Classe: Classe A - Adultos                 │
│ Igreja: Assembleia de Deus                 │
│ Trimestre: 1º Trimestre/2025              │
└────────────────────────────────────────────┘
```

---

#### 👥 **Seção 2: PRESENÇA DOS ALUNOS**

Marque (clique) nas checkboxes dos alunos presentes:

```
PRESENÇA

☐ Ana Silva
☑ Bruno Santos        ← Clicou aqui
☐ Carla Oliveira
```

---

#### 📊 **Seção 3: INFORMAÇÕES DA AULA**

Preencha os números:

```
INFORMAÇÕES DA AULA

Visitantes          [____2____]  ← Pessoas que visitaram
Bíblias            [____3____]  ← Quantas bíblias
Ofertas (R$)       [____50.00_]  ← Dinheiro ofertado
Dízimos (R$)       [____100.00]  ← Dinheiro dízimado
```

---

#### 📝 **Seção 4: OBSERVAÇÕES** (opcional)

Você pode deixar um comentário:

```
OBSERVAÇÕES

┌──────────────────────────────────────────┐
│ Aula excelente! Participação ativa de    │
│ todos. Bruno apresentou um testemunho    │
│ muito interessante.                      │
└──────────────────────────────────────────┘
```

---

### Passo 6: Clique em "💾 Salvar Diário"

```
┌──────────────────┐
│ 💾 Salvar Diário │  ← Clique aqui
└──────────────────┘
```

---

### Passo 7: Confirmação de Sucesso

Você verá uma mensagem verde:

```
┌────────────────────────────────────────────┐
│ ✅ Diário salvo com sucesso.               │
│    Você será redirecionado em alguns      │
│    segundos...                             │
└────────────────────────────────────────────┘
```

Você volta para a lista de aulas.

---

## 🔄 Editar um Diário Já Preenchido

1. Vá para "📝 Listar Aulas"
2. Clique novamente em "📝 Preencher Diário" na mesma aula
3. Os dados anteriores aparecerão nos campos
4. Modifique o que desejar
5. Clique em "💾 Salvar Diário" novamente

---

## ❌ Quando Você NÃO PODE Editar

**Cenário 1**: Aula foi concluída
```
╔═══════════════════════════════════════════════╗
║ Status: 🔒 Concluída                         ║
║                                               ║
║ Botão desabilitado:                          ║
║ [📝 Preencher/Editar Diário] (desabilitado) ║
╚═══════════════════════════════════════════════╝
```

**Cenário 2**: Trimestre foi concluído
```
Mensagem de erro:
"O trimestre foi concluído; não é possível 
editar o diário."
```

⚠️ **Nesse caso**: Contate o Superintendente para iniciar um novo trimestre

---

## 📊 O Que É Salvo Automaticamente

Quando você clica em "💾 Salvar Diário", o sistema salva:

✅ **Presença de cada aluno** (Presente/Ausente)
✅ **Total de presentes** (calculado automaticamente)
✅ **Total de ausentes** (calculado automaticamente)
✅ **Visitantes** (número digitado)
✅ **Bíblias** (número digitado)
✅ **Ofertas** (valor em reais)
✅ **Dízimos** (valor em reais)
✅ **Observações** (texto livre)
✅ **Data/Hora** (automática)

---

## 💡 Dicas Importantes

### 📌 Dica 1: Preencha Logo Após a Aula
Enquanto você se lembra de todos os detalhes, presenças dos alunos, ofertas etc.

### 📌 Dica 2: Guarde a Senha
Sua senha é pessoal e intransferível. Não compartilhe!

### 📌 Dica 3: Valores em Reais
- Use ponto (.) como separador decimal
- Exemplo: `50.00` (cinquenta reais)
- Exemplo: `100.50` (cem reais e cinquenta centavos)

### 📌 Dica 4: Observações São Opcionais
Você pode deixar em branco se não tiver nada a adicionar.

### 📌 Dica 5: Verifique o Status
Sempre veja se a aula está "Pendente" antes de preencher.

---

## 🎯 Fluxo Completo (Visual)

```
┌─ LOGIN ──────────────────────────────────────┐
│                                               │
│ professor1 / senha123                        │
│                                               │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌─ PAINEL DO PROFESSOR ────────────────────────┐
│                                               │
│ [📝 Listar Aulas] [👥 Ver Alunos] [➕ Novo] │
│                                               │
└──────────────────┬──────────────────────────┘
                   │
          Clica em "Listar Aulas"
                   │
                   ▼
┌─ LISTA DE AULAS ─────────────────────────────┐
│                                               │
│ ╔════════════════════════════════════════╗  │
│ ║ Aula 1 - Graça      [📝 Preencher]    ║  │
│ ║ Aula 2 - Fé         [📝 Preencher]    ║  │
│ ║ Aula 3 - Esperança  [📝 Preencher]    ║  │
│ ╚════════════════════════════════════════╝  │
│                                               │
└──────────────────┬──────────────────────────┘
                   │
          Clica em "Preencher"
                   │
                   ▼
┌─ FORMULÁRIO DO DIÁRIO ───────────────────────┐
│                                               │
│ ✓ Informações da Aula                        │
│ ☐ Ana Silva                                  │
│ ☑ Bruno Santos                               │
│ ☐ Carla Oliveira                             │
│ Visitantes: [2]                              │
│ Bíblias: [3]                                 │
│ Ofertas: [50.00]                             │
│ Dízimos: [100.00]                            │
│ Observações: [......]                        │
│                                               │
│ [💾 Salvar] [← Cancelar]                     │
│                                               │
└──────────────────┬──────────────────────────┘
                   │
          Clica em "Salvar"
                   │
                   ▼
┌─ SUCESSO ────────────────────────────────────┐
│                                               │
│ ✅ Diário salvo com sucesso!                │
│                                               │
│ Redirecionando...                            │
│                                               │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌─ VOLTA PARA LISTA DE AULAS ──────────────────┐
│                                               │
│ (Você pode editar novamente se necessário)   │
│                                               │
└──────────────────────────────────────────────┘
```

---

## 🚀 Começar Agora!

1. Abra seu navegador
2. Acesse: **`http://localhost:8000/login/`**
3. Digite: `professor1` e `senha123`
4. Clique em "Entrar"
5. Siga os passos acima
6. Pronto! Seu diário foi salvo! 🎉

---

## 📞 Precisa de Ajuda?

### Problema: "Nenhum aluno matriculado"
👉 Clique em "➕ Matricular" para adicionar alunos

### Problema: "Nenhum trimestre ativo"
👉 O Superintendente precisa iniciar um trimestre novo

### Problema: Não consigo editar depois de salvar
👉 Verifique se a aula já foi concluída pelo Secretário

### Problema: Senha não funciona
👉 Use exatamente: `professor1` / `senha123`

---

**Versão**: 1.0  
**Data**: 27 de Novembro de 2025  
**Status**: ✅ Testado e Funcionando
