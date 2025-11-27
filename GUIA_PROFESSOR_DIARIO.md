# Como Preencher o Diário de Aula - Guia do Professor

## Passo a Passo para Preencher o Diário

### 1️⃣ Fazer Login
- Acesse: `http://localhost:8000/login/`
- **Usuário**: `professor1`
- **Senha**: `senha123`
- Clique em "Entrar"

### 2️⃣ Acessar o Painel do Professor
Após fazer login, você verá o **Painel do Professor** com 3 opções principais:

```
📚 Diário de Aula - Professor

┌─────────────────────────────────────────────────────────────┐
│ 📝 Minhas Aulas                                             │
│ Veja todas as aulas da sua classe e preencha o diário      │
│ [Listar Aulas]                                              │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ 👥 Alunos da Minha Classe                                   │
│ Visualize todos os alunos matriculados na sua classe       │
│ [Ver Alunos]                                                │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ ➕ Matricular Aluno                                          │
│ Adicione novos alunos à sua classe                         │
│ [Matricular]                                                │
└─────────────────────────────────────────────────────────────┘
```

### 3️⃣ Clique em "Listar Aulas"
Você verá uma tabela com todas as aulas da sua classe:

```
Data        │ Título da Aula      │ Trimestre  │ Status      │ Ações
────────────┼────────────────────┼───────────┼─────────────┼──────────
27/11/2025  │ Aula 1 - Graça      │ 1º/2025   │ ⏳ Pendente  │ 📝 Preencher Diário
28/11/2025  │ Aula 2 - Fé         │ 1º/2025   │ ⏳ Pendente  │ 📝 Preencher Diário
29/11/2025  │ Aula 3 - Esperança  │ 1º/2025   │ ⏳ Pendente  │ 📝 Preencher Diário
```

### 4️⃣ Clique em "📝 Preencher Diário"
Você será levado para a tela de preenchimento do diário:

```
PREENCHER DIÁRIO: Aula 1 - Graça

[Informações da Aula]
Aula: Aula 1 - Graça
Data prevista: 27/11/2025
Classe: Classe A - Adultos (Assembleia de Deus)
Trimestre: 1º Trimestre/2025

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PRESENÇA

☐ Ana Silva
☐ Bruno Santos
☐ Carla Oliveira

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INFORMAÇÕES DA AULA

Visitantes:         [0]
Bíblias:           [0]
Ofertas (R$):      [0.00]
Dízimos (R$):      [0.00]

Observações:
[Text area para observações]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[💾 Salvar Diário] [← Cancelar]
```

### 5️⃣ Preencha o Formulário

#### a) **Marque os Alunos Presentes**
- Clique nas checkboxes dos alunos que estavam presentes
- Deixe desmarcados os alunos que faltaram

#### b) **Preencha as Informações Adicionais**
- **Visitantes**: Número de pessoas que visitaram a aula
- **Bíblias**: Quantas bíblias foram usadas
- **Ofertas**: Valor em reais (ex: 50.00)
- **Dízimos**: Valor em reais (ex: 100.00)

#### c) **Observações** (opcional)
- Escreva qualquer observação relevante sobre a aula

### 6️⃣ Clique em "💾 Salvar Diário"
- Seus dados serão salvos
- Você será redirecionado para a lista de aulas
- Um aviso de sucesso aparecerá

### 7️⃣ Verificar o Diário Preenchido
- Quando retornar à lista de aulas, a aula que preencheu permanecerá com status "⏳ Pendente"
- Você pode editar clicando novamente em "📝 Preencher Diário"

---

## ⚠️ Informações Importantes

### Quando a Aula é Concluída
- Após o **Secretário ou Superintendente** concluir a aula, você **NÃO PODERÁ MAIS EDITAR** o diário
- O botão "📝 Preencher Diário" fica desabilitado
- Um cadeado 🔒 aparece indicando que a aula foi concluída

### Trimestre Inativo
- Se o trimestre for concluído, também não será possível editar diários
- Verifique com o Superintendente se precisa adicionar aulas em um novo trimestre

### O que Salva Automaticamente
Cada campo preenchido é registrado:
- ✅ Presença de cada aluno (Presente/Ausente)
- ✅ Total de presentes e ausentes
- ✅ Visitantes, Bíblias, Ofertas, Dízimos
- ✅ Data/Hora do preenchimento

---

## 📊 Exemplo de Diário Completo

```
PRESENÇA
☑ Ana Silva        → Presente
☑ Bruno Santos     → Presente
☐ Carla Oliveira   → Ausente

RESUMO
Alunos Presentes: 2
Alunos Ausentes: 1
Visitantes: 3
Bíblias: 2
Ofertas: R$ 50.00
Dízimos: R$ 100.00

OBSERVAÇÕES
Ótima aula! Todos participaram ativamente.
```

---

## 🆘 Troubleshooting

### Problema: "Nenhum aluno matriculado nesta classe"
**Solução**: Clique em "➕ Matricular" no painel para adicionar alunos

### Problema: "Nenhum trimestre ativo"
**Solução**: O Superintendente deve iniciar um novo trimestre em "Iniciar Trimestre"

### Problema: Não consigo editar depois de salvar
**Solução**: Verifique se a aula já foi concluída pelo Secretário/Superintendente

### Problema: Dados não estão salvando
**Solução**: 
- Verifique se todos os campos estão preenchidos corretamente
- Tente clicar em "💾 Salvar Diário" novamente
- Se persistir, contate o administrador

---

## 📝 Dicas Úteis

1. **Preencha no Dia da Aula**: Preenchas o diário enquanto se lembra dos detalhes
2. **Observe o Status**: Verifique se a aula está pendente antes de preencher
3. **Guarde a Senha**: Mantenha sua senha segura e não compartilhe
4. **Consulte Relatórios**: Acesse "Relatório de Aulas" para visualizar histórico

---

**Versão**: 1.0  
**Última atualização**: 27 de Novembro de 2025
