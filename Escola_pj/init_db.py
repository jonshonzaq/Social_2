#!/usr/bin/env python
"""
Script para inicializar o banco de dados com dados de teste
Inclui campo revistas nos diarios
"""

import os
import django
from datetime import datetime, timedelta

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Escola.settings')
django.setup()

from base.models import Igreja, Usuario, Classe, Professor, Trimestre, Aula, Aluno, Matricula, Diario, Presenca

def criar_dados_teste():
    """Cria dados de teste completos com revistas nos diarios"""
    
    print("🔄 Deletando dados antigos...")
    Igreja.objects.all().delete()
    Usuario.objects.all().delete()
    Classe.objects.all().delete()
    Professor.objects.all().delete()
    Trimestre.objects.all().delete()
    Aula.objects.all().delete()
    Aluno.objects.all().delete()
    Matricula.objects.all().delete()
    Diario.objects.all().delete()
    Presenca.objects.all().delete()
    
    print("✅ Dados antigos deletados")
    
    # 1. Criar Igreja
    print("\n📍 Criando Igreja...")
    igreja = Igreja.objects.create(nome="Assembleia de Deus")
    print(f"  ✅ Igreja criada: {igreja.nome}")
    
    # 2. Criar Usuários
    print("\n👥 Criando Usuários...")
    
    # Professor
    prof_user = Usuario.objects.create_user(
        username='professor_teste',
        email='professor@ebd.com',
        password='senha123',
        role='professor',
        igreja=igreja
    )
    print(f"  ✅ Professor: {prof_user.username}")
    
    # Secretário
    sec_user = Usuario.objects.create_user(
        username='secretario_teste',
        email='secretario@ebd.com',
        password='senha123',
        role='secretario',
        igreja=igreja
    )
    print(f"  ✅ Secretário: {sec_user.username}")
    
    # Superintendente
    super_user = Usuario.objects.create_user(
        username='superintendente_teste',
        email='super@ebd.com',
        password='senha123',
        role='superintendente',
        igreja=igreja
    )
    print(f"  ✅ Superintendente: {super_user.username}")
    
    # 3. Criar Classes
    print("\n🏫 Criando Classes...")
    
    classe1 = Classe.objects.create(nome="Classe Infantil", igreja=igreja)
    classe2 = Classe.objects.create(nome="Classe Adolescente", igreja=igreja)
    classe3 = Classe.objects.create(nome="Classe Adulta", igreja=igreja)
    print(f"  ✅ Classe 1: {classe1.nome}")
    print(f"  ✅ Classe 2: {classe2.nome}")
    print(f"  ✅ Classe 3: {classe3.nome}")
    
    # 4. Criar Professores
    print("\n👨‍🏫 Vinculando Professor à Classe...")
    prof = Professor.objects.create(usuario=prof_user, classe=classe1)
    print(f"  ✅ Professor {prof_user.username} vinculado à {classe1.nome}")
    
    # 5. Criar Trimestre Ativo
    print("\n📅 Criando Trimestre Ativo...")
    today = datetime.now()
    trimestre = Trimestre.objects.create(
        igreja=igreja,
        trimestre="1º Trimestre",
        ano=today.year,
        ativo=True,
        concluido=False
    )
    print(f"  ✅ Trimestre: {trimestre.trimestre}/{trimestre.ano} (ATIVO)")
    
    # 6. Criar Aulas
    print("\n📖 Criando Aulas...")
    aulas = []
    for i, classe in enumerate([classe1, classe2, classe3]):
        for j in range(3):
            data_aula = today + timedelta(days=j*7)
            aula = Aula.objects.create(
                trimestre=trimestre,
                classe=classe,
                titulo=f"Aula {j+1} - {classe.nome}",
                data_prevista=data_aula.date(),
                concluida=False
            )
            aulas.append(aula)
            print(f"  ✅ Aula: {aula.titulo} ({aula.data_prevista})")
    
    # 7. Criar Alunos
    print("\n👨‍🎓 Criando Alunos...")
    alunos = []
    nomes_alunos = ["João Silva", "Maria Santos", "Pedro Oliveira", "Ana Costa", "Lucas Ferreira"]
    
    for nome in nomes_alunos:
        aluno = Aluno.objects.create(
            igreja=igreja,
            nome=nome,
            data_nascimento="2010-05-15"
        )
        alunos.append(aluno)
        print(f"  ✅ Aluno: {nome}")
    
    # 8. Criar Matrículas
    print("\n📝 Criando Matrículas...")
    for aluno in alunos[:2]:
        matricula = Matricula.objects.create(
            aluno=aluno,
            trimestre=trimestre,
            classe=classe1,
            ativa=True
        )
        print(f"  ✅ {aluno.nome} → {classe1.nome}")
    
    for aluno in alunos[2:4]:
        matricula = Matricula.objects.create(
            aluno=aluno,
            trimestre=trimestre,
            classe=classe2,
            ativa=True
        )
        print(f"  ✅ {aluno.nome} → {classe2.nome}")
    
    # 9. Criar Diarios com Revistas
    print("\n📓 Criando Diarios com Revistas...")
    for aula in aulas[:3]:
        diario = Diario.objects.create(
            aula=aula,
            alunos_presentes=2,
            alunos_ausentes=1,
            visitantes=1,
            biblias=3,
            revistas=2,  # Campo revistas
            ofertas=25.50,
            dizimos=50.00,
            observacoes="Aula ministrada normalmente"
        )
        print(f"  ✅ Diario da aula '{aula.titulo}' com {diario.revistas} revistas")
    
    # 10. Criar Presenças
    print("\n✅ Criando Presenças...")
    matriculas_aula1 = Matricula.objects.filter(classe=classe1, trimestre=trimestre)
    diario_aula1 = Diario.objects.filter(aula=aulas[0]).first()
    
    if diario_aula1:
        for matricula in matriculas_aula1:
            presenca = Presenca.objects.create(
                aluno=matricula.aluno,
                diario=diario_aula1,
                status='P'  # Presente
            )
            print(f"  ✅ Presença: {matricula.aluno.nome} - Presente")
    
    print("\n" + "="*50)
    print("✅ BANCO DE DADOS INICIALIZADO COM SUCESSO!")
    print("="*50)
    print("\n📊 Resumo:")
    print(f"  - Igreja: {Igreja.objects.count()}")
    print(f"  - Usuários: {Usuario.objects.count()}")
    print(f"  - Classes: {Classe.objects.count()}")
    print(f"  - Professores: {Professor.objects.count()}")
    print(f"  - Alunos: {Aluno.objects.count()}")
    print(f"  - Trimestres: {Trimestre.objects.count()}")
    print(f"  - Aulas: {Aula.objects.count()}")
    print(f"  - Matrículas: {Matricula.objects.count()}")
    print(f"  - Diarios: {Diario.objects.count()}")
    print(f"  - Presenças: {Presenca.objects.count()}")
    print("\n🔐 Credenciais de Teste:")
    print(f"  Professor: professor_teste / senha123")
    print(f"  Secretário: secretario_teste / senha123")
    print(f"  Superintendente: superintendente_teste / senha123")

if __name__ == '__main__':
    try:
        criar_dados_teste()
    except Exception as e:
        print(f"\n❌ Erro: {e}")
        import traceback
        traceback.print_exc()
