#!/usr/bin/env python
"""
Script de Administração do Sistema EBD
Execute: python admin_script.py

Permite gerenciar dados via Django shell
"""

import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Escola.settings')
django.setup()

from base.models import Igreja, Usuario, Classe, Professor, Trimestre, Aluno, Matricula

def print_menu():
    print("\n" + "="*50)
    print("     ADMINISTRAÇÃO DO SISTEMA EBD")
    print("="*50)
    print("1. Listar Igrejas")
    print("2. Listar Usuários")
    print("3. Listar Classes")
    print("4. Listar Alunos")
    print("5. Listar Trimestres")
    print("6. Listar Matrículas")
    print("7. Criar Trimestre")
    print("8. Ativar Trimestre")
    print("9. Criar Aluno")
    print("10. Resetar Banco (⚠️  PERIGOSO)")
    print("0. Sair")
    print("="*50)

def listar_igrejas():
    print("\n📍 IGREJAS:")
    igrejas = Igreja.objects.all()
    if not igrejas:
        print("  Nenhuma igreja encontrada")
        return
    for i in igrejas:
        print(f"  - {i.nome} (ID: {i.id})")

def listar_usuarios():
    print("\n👥 USUÁRIOS:")
    usuarios = Usuario.objects.all()
    if not usuarios:
        print("  Nenhum usuário encontrado")
        return
    for u in usuarios:
        print(f"  - {u.username} ({u.get_role_display()}) | Email: {u.email}")

def listar_classes():
    print("\n🏫 CLASSES:")
    classes = Classe.objects.all()
    if not classes:
        print("  Nenhuma classe encontrada")
        return
    for c in classes:
        professores = Professor.objects.filter(classe=c)
        prof_nomes = ", ".join([p.usuario.username for p in professores]) if professores else "N/A"
        print(f"  - {c.nome} | Professores: {prof_nomes} | Igreja: {c.igreja.nome}")

def listar_alunos():
    print("\n👨‍🎓 ALUNOS:")
    alunos = Aluno.objects.all()
    if not alunos:
        print("  Nenhum aluno encontrado")
        return
    for a in alunos:
        print(f"  - {a.nome} | Nascimento: {a.data_nascimento} | Igreja: {a.igreja.nome}")

def listar_trimestres():
    print("\n📅 TRIMESTRES:")
    trimestres = Trimestre.objects.all().order_by('-ano', '-trimestre')
    if not trimestres:
        print("  Nenhum trimestre encontrado")
        return
    for t in trimestres:
        status = "✅ ATIVO" if t.ativo else "❌ Inativo"
        concluido = "✓ Concluído" if t.concluido else "⏳ Em andamento"
        print(f"  - {t.trimestre}º/{t.ano} | {status} | {concluido} (ID: {t.id})")

def listar_matriculas():
    print("\n📝 MATRÍCULAS:")
    matriculas = Matricula.objects.all().select_related('aluno', 'classe', 'trimestre')
    if not matriculas:
        print("  Nenhuma matrícula encontrada")
        return
    for m in matriculas:
        status = "✅ Ativa" if m.ativa else "❌ Inativa"
        print(f"  - {m.aluno.nome} → {m.classe.nome} ({m.trimestre.trimestre}º/{m.trimestre.ano}) {status}")

def criar_trimestre():
    print("\n➕ CRIAR TRIMESTRE")
    try:
        trimestre = int(input("Trimestre (1-4): "))
        ano = int(input("Ano (ex: 2024): "))
        
        if Trimestre.objects.filter(trimestre=trimestre, ano=ano).exists():
            print("❌ Este trimestre já existe!")
            return
        
        t = Trimestre.objects.create(trimestre=trimestre, ano=ano, ativo=False)
        print(f"✅ Trimestre criado: {t.trimestre}º/{t.ano}")
    except Exception as e:
        print(f"❌ Erro: {e}")

def ativar_trimestre():
    print("\n🔄 ATIVAR TRIMESTRE")
    listar_trimestres()
    try:
        trimestre_id = int(input("\nID do trimestre a ativar: "))
        trimestre = Trimestre.objects.get(id=trimestre_id)
        
        # Desativar outros
        Trimestre.objects.exclude(id=trimestre_id).update(ativo=False)
        
        # Ativar selecionado
        trimestre.ativo = True
        trimestre.save()
        print(f"✅ Trimestre {trimestre.trimestre}º/{trimestre.ano} agora é ATIVO")
    except Exception as e:
        print(f"❌ Erro: {e}")

def criar_aluno():
    print("\n➕ CRIAR ALUNO")
    try:
        listar_igrejas()
        igreja_id = int(input("\nID da Igreja: "))
        
        igreja = Igreja.objects.get(id=igreja_id)
        nome = input("Nome do aluno: ")
        data_nasc = input("Data de nascimento (YYYY-MM-DD): ")
        
        aluno = Aluno.objects.create(
            igreja=igreja,
            nome=nome,
            data_nascimento=data_nasc
        )
        print(f"✅ Aluno criado: {aluno.nome}")
    except Exception as e:
        print(f"❌ Erro: {e}")

def resetar_banco():
    print("\n⚠️  RESETAR BANCO DE DADOS")
    confirmacao = input("Tem CERTEZA? Digite 'SIM' para confirmar: ")
    
    if confirmacao.upper() == 'SIM':
        try:
            print("Deletando dados...")
            # Manter Igreja
            Igreja.objects.all().delete()
            Usuario.objects.all().delete()
            Classe.objects.all().delete()
            Aluno.objects.all().delete()
            Trimestre.objects.all().delete()
            Matricula.objects.all().delete()
            
            # Recriar Igreja padrão
            Igreja.objects.create(nome="Assembleia")
            print("✅ Banco resetado com sucesso!")
        except Exception as e:
            print(f"❌ Erro: {e}")
    else:
        print("❌ Cancelado")

def main():
    while True:
        print_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            listar_igrejas()
        elif opcao == '2':
            listar_usuarios()
        elif opcao == '3':
            listar_classes()
        elif opcao == '4':
            listar_alunos()
        elif opcao == '5':
            listar_trimestres()
        elif opcao == '6':
            listar_matriculas()
        elif opcao == '7':
            criar_trimestre()
        elif opcao == '8':
            ativar_trimestre()
        elif opcao == '9':
            criar_aluno()
        elif opcao == '10':
            resetar_banco()
        elif opcao == '0':
            print("\nAté logo! 👋")
            break
        else:
            print("❌ Opção inválida")

if __name__ == '__main__':
    main()
