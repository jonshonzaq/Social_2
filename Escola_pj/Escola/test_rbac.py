#!/usr/bin/env python
"""
Script de teste para validar restrições de acesso (role-based) para cada CDU
Execute: python manage.py shell < test_rbac.py

RBAC = Role-Based Access Control
"""

import os
import django
from django.test.client import Client
from django.contrib.auth import get_user_model

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Escola.settings')
django.setup()

from base.models import Igreja, Usuario, Classe, Professor, Trimestre, Aula, Aluno, Matricula

Usuario = get_user_model()

class TestadorRBAC:
    """Testa restrições de acesso por role"""
    
    def __init__(self):
        self.client = Client()
        self.passou = 0
        self.falhou = 0
        self.usuarios = {}
        
    def setup(self):
        """Prepara dados de teste"""
        print("\n📋 Preparando dados de teste...")
        
        # Busca usuários criados por init_db.py
        self.usuarios = {
            'professor': Usuario.objects.get(username='professor_teste'),
            'secretario': Usuario.objects.get(username='secretario_teste'),
            'superintendente': Usuario.objects.get(username='superintendente_teste'),
        }
        
        # Busca objetos
        self.igreja = Igreja.objects.first()
        self.classe = Classe.objects.first()
        self.trimestre = Trimestre.objects.filter(ativo=True).first()
        self.aula = Aula.objects.first()
        self.aluno = Aluno.objects.first()
        
        print(f"  ✅ Usuario Professor: {self.usuarios['professor'].username}")
        print(f"  ✅ Usuario Secretário: {self.usuarios['secretario'].username}")
        print(f"  ✅ Usuario Superintendente: {self.usuarios['superintendente'].username}")
        
    def teste(self, nome, role, endpoint, esperado_status, dados=None):
        """
        Executa um teste de acesso
        esperado_status: 200 (sucesso), 302 (redirect/forbidden), 404, etc
        """
        usuario = self.usuarios[role]
        self.client.login(username=usuario.username, password='senha123')
        
        try:
            if dados:
                response = self.client.post(endpoint, dados)
            else:
                response = self.client.get(endpoint)
            
            resultado = response.status_code == esperado_status
            
            if resultado:
                print(f"  ✅ {nome}")
                self.passou += 1
            else:
                print(f"  ❌ {nome} (esperado {esperado_status}, recebido {response.status_code})")
                self.falhou += 1
                
        except Exception as e:
            print(f"  ❌ {nome} (Erro: {str(e)})")
            self.falhou += 1
        finally:
            self.client.logout()
    
    def rodar_testes(self):
        """Executa todos os testes"""
        
        print("\n" + "="*60)
        print("🧪 TESTES DE CONTROLE DE ACESSO (RBAC)")
        print("="*60)
        
        # CDU.001 - Matricular Aluno
        print("\n📚 CDU.001 - MATRICULAR ALUNO")
        print("-" * 60)
        self.teste(
            "Professor pode acessar matricular (sua classe)",
            'professor',
            f'/alunos/matricular/{self.classe.id}/',
            200
        )
        self.teste(
            "Secretário pode acessar matricular (qualquer classe)",
            'secretario',
            f'/alunos/matricular/{self.classe.id}/',
            200
        )
        self.teste(
            "Superintendente pode acessar matricular (qualquer classe)",
            'superintendente',
            f'/alunos/matricular/{self.classe.id}/',
            200
        )
        
        # CDU.002 - Preencher Diário
        print("\n📖 CDU.002 - PREENCHER DIÁRIO")
        print("-" * 60)
        self.teste(
            "Professor pode acessar diario_registro",
            'professor',
            f'/aulas/{self.aula.id}/diario/',
            200
        )
        self.teste(
            "Secretário pode acessar diario_registro",
            'secretario',
            f'/aulas/{self.aula.id}/diario/',
            200
        )
        self.teste(
            "Superintendente pode acessar diario_registro",
            'superintendente',
            f'/aulas/{self.aula.id}/diario/',
            200
        )
        
        # CDU.003 - Gerar Relatório
        print("\n📊 CDU.003 - GERAR RELATÓRIO")
        print("-" * 60)
        self.teste(
            "Professor BLOQUEADO em relatorio_aula",
            'professor',
            f'/aulas/{self.aula.id}/relatorio/',
            302  # Redirect (forbidden)
        )
        self.teste(
            "Secretário pode acessar relatorio_aula",
            'secretario',
            f'/aulas/{self.aula.id}/relatorio/',
            200
        )
        self.teste(
            "Superintendente pode acessar relatorio_aula",
            'superintendente',
            f'/aulas/{self.aula.id}/relatorio/',
            200
        )
        
        # CDU.004 - Concluir Aula
        print("\n✅ CDU.004 - CONCLUIR AULA")
        print("-" * 60)
        self.teste(
            "Professor BLOQUEADO em aula_concluir",
            'professor',
            f'/aulas/{self.aula.id}/concluir/',
            302  # Redirect (forbidden)
        )
        self.teste(
            "Secretário pode concluir aula (POST)",
            'secretario',
            f'/aulas/{self.aula.id}/concluir/',
            302  # Redirect após conclusão
        )
        self.teste(
            "Superintendente pode concluir aula (POST)",
            'superintendente',
            f'/aulas/{self.aula.id}/concluir/',
            302  # Redirect após conclusão
        )
        
        # CDU.005 - Transferir Aluno
        print("\n🔄 CDU.005 - TRANSFERIR ALUNO")
        print("-" * 60)
        self.teste(
            "Professor BLOQUEADO em aluno_transferir",
            'professor',
            f'/alunos/{self.aluno.id}/transferir/',
            302  # Redirect (forbidden)
        )
        self.teste(
            "Secretário pode acessar aluno_transferir",
            'secretario',
            f'/alunos/{self.aluno.id}/transferir/',
            200
        )
        self.teste(
            "Superintendente pode acessar aluno_transferir",
            'superintendente',
            f'/alunos/{self.aluno.id}/transferir/',
            200
        )
        
        # CDU.006 - Cadastro de Professor
        print("\n👨‍🏫 CDU.006 - CADASTRO DE PROFESSOR")
        print("-" * 60)
        self.teste(
            "Professor BLOQUEADO em cadastrar_professor",
            'professor',
            '/professores/cadastrar/',
            302  # Redirect (forbidden)
        )
        self.teste(
            "Secretário BLOQUEADO em cadastrar_professor",
            'secretario',
            '/professores/cadastrar/',
            302  # Redirect (forbidden)
        )
        self.teste(
            "Superintendente pode acessar cadastrar_professor",
            'superintendente',
            '/professores/cadastrar/',
            200
        )
        
        # CDU.007 - Iniciar Trimestre
        print("\n📅 CDU.007 - INICIAR TRIMESTRE")
        print("-" * 60)
        self.teste(
            "Professor BLOQUEADO em periodo_iniciar",
            'professor',
            '/periodos/iniciar/',
            302  # Redirect (forbidden)
        )
        self.teste(
            "Secretário BLOQUEADO em periodo_iniciar",
            'secretario',
            '/periodos/iniciar/',
            302  # Redirect (forbidden)
        )
        self.teste(
            "Superintendente pode acessar periodo_iniciar",
            'superintendente',
            '/periodos/iniciar/',
            200
        )
        
        # CDU.008 - Concluir Trimestre
        print("\n🏁 CDU.008 - CONCLUIR TRIMESTRE")
        print("-" * 60)
        self.teste(
            "Professor BLOQUEADO em periodo_concluir",
            'professor',
            f'/periodos/{self.trimestre.id}/concluir/',
            302  # Redirect (forbidden)
        )
        self.teste(
            "Secretário BLOQUEADO em periodo_concluir",
            'secretario',
            f'/periodos/{self.trimestre.id}/concluir/',
            302  # Redirect (forbidden)
        )
        self.teste(
            "Superintendente pode acessar periodo_concluir (POST)",
            'superintendente',
            f'/periodos/{self.trimestre.id}/concluir/',
            302  # Redirect após conclusão
        )
        
        # Validação CDU.008 - Bloqueios após concluir trimestre
        print("\n🔒 VALIDAÇÃO CDU.008 - BLOQUEIOS APÓS CONCLUIR TRIMESTRE")
        print("-" * 60)
        
        # Cria novo trimestre para testar bloqueios
        trimestre_teste = Trimestre.objects.create(
            igreja=self.igreja,
            trimestre="2º Trimestre",
            ano=2025,
            ativo=True,
            concluido=True  # CONCLUÍDO
        )
        
        self.teste(
            "Superintendente BLOQUEADO ao matricular em trimestre concluído",
            'superintendente',
            f'/alunos/matricular/{self.classe.id}/',
            302  # Redirect com erro
        )
        
        self.teste(
            "Secretário BLOQUEADO ao transferir em trimestre concluído",
            'secretario',
            f'/alunos/{self.aluno.id}/transferir/',
            302  # Redirect com erro
        )
        
        # Limpa
        trimestre_teste.delete()
        
        # Resumo
        self.relatorio()
    
    def relatorio(self):
        """Exibe relatório final"""
        total = self.passou + self.falhou
        percentual = (self.passou / total * 100) if total > 0 else 0
        
        print("\n" + "="*60)
        print("📊 RELATÓRIO FINAL")
        print("="*60)
        print(f"✅ Testes aprovados: {self.passou}")
        print(f"❌ Testes falhados: {self.falhou}")
        print(f"📈 Total: {total}")
        print(f"📊 Taxa de sucesso: {percentual:.1f}%")
        
        if self.falhou == 0:
            print("\n🎉 TODOS OS TESTES PASSARAM!")
        else:
            print(f"\n⚠️  {self.falhou} teste(s) falharam. Revise as restrições de acesso.")
        
        print("="*60)

if __name__ == '__main__':
    testador = TestadorRBAC()
    testador.setup()
    testador.rodar_testes()
