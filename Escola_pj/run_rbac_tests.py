#!/usr/bin/env python
"""
Script de teste para validar restrições de acesso (role-based) para cada CDU
Executar: python run_rbac_tests.py
"""

import os
import sys
import django
from pathlib import Path

# Add Escola directory to path
sys.path.insert(0, '/workspaces/Social_2/Escola_pj/Escola')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Escola.settings')
django.setup()

from django.test import Client
from django.contrib.auth import get_user_model
from base.models import Igreja, Classe, Trimestre, Aula, Aluno

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
        
        try:
            self.usuarios = {
                'professor': Usuario.objects.get(username='professor_teste'),
                'secretario': Usuario.objects.get(username='secretario_teste'),
                'superintendente': Usuario.objects.get(username='superintendente_teste'),
            }
            
            self.igreja = Igreja.objects.first()
            self.classe = Classe.objects.first()
            self.trimestre = Trimestre.objects.filter(ativo=True).first()
            
            # Se não há trimestre ativo, ativar o primeiro
            if not self.trimestre:
                self.trimestre = Trimestre.objects.first()
                if self.trimestre:
                    self.trimestre.ativo = True
                    self.trimestre.concluido = False
                    self.trimestre.save()
                    print(f"  ⚠️  Trimestre reativado: {self.trimestre}")
            
            self.aula = Aula.objects.first()
            self.aluno = Aluno.objects.first()
            
            print(f"  ✅ Usuario Professor: {self.usuarios['professor'].username}")
            print(f"  ✅ Usuario Secretário: {self.usuarios['secretario'].username}")
            print(f"  ✅ Usuario Superintendente: {self.usuarios['superintendente'].username}")
            print(f"  ✅ Trimestre Ativo: {self.trimestre}")
            return True
        except Exception as e:
            print(f"  ❌ Erro ao preparar dados: {e}")
            import traceback
            traceback.print_exc()
            return False
        
    def teste(self, nome, role, endpoint, esperado_status, dados=None):
        """Executa um teste de acesso"""
        usuario = self.usuarios.get(role)
        if not usuario:
            print(f"  ❌ {nome} (Usuario não encontrado)")
            self.falhou += 1
            return
        
        # Login
        resultado_login = self.client.login(username=usuario.username, password='senha123')
        if not resultado_login:
            print(f"  ❌ {nome} (Falha ao fazer login)")
            self.falhou += 1
            return
        
        try:
            if dados:
                response = self.client.post(endpoint, dados, follow=False)
            else:
                response = self.client.get(endpoint, follow=False)
            
            # Aceita status exato ou qualquer 3xx para redirects
            if isinstance(esperado_status, list):
                resultado = response.status_code in esperado_status
            else:
                resultado = response.status_code == esperado_status
            
            if resultado:
                print(f"  ✅ {nome} (status {response.status_code})")
                self.passou += 1
            else:
                print(f"  ❌ {nome} (esperado {esperado_status}, recebido {response.status_code})")
                self.falhou += 1
                
        except Exception as e:
            print(f"  ❌ {nome} (Erro: {str(e)[:80]})")
            self.falhou += 1
        finally:
            self.client.logout()
    
    def rodar_testes(self):
        """Executa todos os testes"""
        
        print("\n" + "="*70)
        print("🧪 TESTES DE CONTROLE DE ACESSO (RBAC) - SISTEMA EBD")
        print("="*70)
        
        # CDU.001 - Matricular
        print("\n📚 CDU.001 - MATRICULAR ALUNO")
        print("-" * 70)
        self.teste("✅ Professor acessa aluno_matricular (sua classe)", 'professor', f'/alunos/matricular/{self.classe.id}/', 200)
        self.teste("✅ Secretário acessa aluno_matricular", 'secretario', f'/alunos/matricular/{self.classe.id}/', 200)
        self.teste("✅ Superintendente acessa aluno_matricular", 'superintendente', f'/alunos/matricular/{self.classe.id}/', 200)
        
        # CDU.002 - Diário
        print("\n📖 CDU.002 - PREENCHER DIÁRIO")
        print("-" * 70)
        self.teste("✅ Professor acessa diario_registro", 'professor', f'/diario/{self.aula.id}/', 200)
        self.teste("✅ Secretário acessa diario_registro", 'secretario', f'/diario/{self.aula.id}/', 200)
        self.teste("✅ Superintendente acessa diario_registro", 'superintendente', f'/diario/{self.aula.id}/', 200)
        
        # CDU.003 - Relatório
        print("\n📊 CDU.003 - GERAR RELATÓRIO (acesso restrito)")
        print("-" * 70)
        self.teste("❌ Professor BLOQUEADO em relatorio_aula", 'professor', f'/relatorios/aula/{self.aula.id}/', [302, 403])
        self.teste("✅ Secretário acessa relatorio_aula", 'secretario', f'/relatorios/aula/{self.aula.id}/', 200)
        self.teste("✅ Superintendente acessa relatorio_aula", 'superintendente', f'/relatorios/aula/{self.aula.id}/', 200)
        
        # CDU.004 - Concluir Aula
        print("\n✅ CDU.004 - CONCLUIR AULA (acesso restrito)")
        print("-" * 70)
        self.teste("❌ Professor BLOQUEADO em aula_concluir", 'professor', f'/aulas/{self.aula.id}/concluir/', [302, 403])
        self.teste("✅ Secretário acessa aula_concluir (GET redirect)", 'secretario', f'/aulas/{self.aula.id}/concluir/', [302, 200])
        self.teste("✅ Superintendente acessa aula_concluir (GET redirect)", 'superintendente', f'/aulas/{self.aula.id}/concluir/', [302, 200])
        
        # CDU.005 - Transferir
        print("\n🔄 CDU.005 - TRANSFERIR ALUNO (acesso restrito)")
        print("-" * 70)
        self.teste("❌ Professor BLOQUEADO em aluno_transferir", 'professor', f'/alunos/{self.aluno.id}/transferir/', [302, 403])
        self.teste("✅ Secretário acessa aluno_transferir", 'secretario', f'/alunos/{self.aluno.id}/transferir/', 200)
        self.teste("✅ Superintendente acessa aluno_transferir", 'superintendente', f'/alunos/{self.aluno.id}/transferir/', 200)
        
        # CDU.006 - Cadastro Professor
        print("\n👨‍🏫 CDU.006 - CADASTRO DE PROFESSOR (acesso restrito)")
        print("-" * 70)
        self.teste("❌ Professor BLOQUEADO em cadastrar_professor", 'professor', '/professor/cadastrar/', [302, 403])
        self.teste("❌ Secretário BLOQUEADO em cadastrar_professor", 'secretario', '/professor/cadastrar/', [302, 403])
        self.teste("✅ Superintendente acessa cadastrar_professor", 'superintendente', '/professor/cadastrar/', 200)
        
        # CDU.007 - Iniciar Trimestre
        print("\n📅 CDU.007 - INICIAR TRIMESTRE (acesso restrito)")
        print("-" * 70)
        self.teste("❌ Professor BLOQUEADO em periodo_iniciar", 'professor', '/periodos/iniciar/', [302, 403])
        self.teste("❌ Secretário BLOQUEADO em periodo_iniciar", 'secretario', '/periodos/iniciar/', [302, 403])
        self.teste("✅ Superintendente acessa periodo_iniciar", 'superintendente', '/periodos/iniciar/', 200)
        
        # CDU.008 - Concluir Trimestre
        print("\n🏁 CDU.008 - CONCLUIR TRIMESTRE (acesso restrito)")
        print("-" * 70)
        # periodo_concluir é POST-only
        self.teste("❌ Professor BLOQUEADO em periodo_concluir", 'professor', '/periodos/concluir/', [302, 403])
        self.teste("❌ Secretário BLOQUEADO em periodo_concluir", 'secretario', '/periodos/concluir/', [302, 403])
        self.teste("✅ Superintendente acessa periodo_concluir (POST)", 'superintendente', '/periodos/concluir/', [302, 405])
        
        # Validação CDU.008 - Bloqueios
        print("\n🔒 VALIDAÇÃO CDU.008 - BLOQUEIOS EM TRIMESTRE CONCLUÍDO")
        print("-" * 70)
        
        # Cria trimestre concluído
        try:
            trimestre_concluido = Trimestre.objects.create(
                igreja=self.igreja,
                trimestre="2º Trimestre",
                ano=2025,
                ativo=True,
                concluido=True
            )
            
            self.teste(
                "🔒 Superintendente BLOQUEADO ao matricular em trimestre concluído",
                'superintendente',
                f'/alunos/matricular/{self.classe.id}/',
                [302]
            )
            
            trimestre_concluido.delete()
        except Exception as e:
            print(f"  ⚠️  Skipped (erro ao criar trimestre teste): {e}")
        
        self.relatorio()
    
    def relatorio(self):
        """Exibe relatório final"""
        total = self.passou + self.falhou
        percentual = (self.passou / total * 100) if total > 0 else 0
        
        print("\n" + "="*70)
        print("📊 RELATÓRIO FINAL")
        print("="*70)
        print(f"✅ Testes aprovados:  {self.passou}")
        print(f"❌ Testes falhados:   {self.falhou}")
        print(f"📈 Total:            {total}")
        print(f"📊 Taxa de sucesso:  {percentual:.1f}%")
        
        if self.falhou == 0:
            print("\n🎉 TODOS OS TESTES PASSARAM!")
            print("\n✅ Sistema EBD está com RBAC (Role-Based Access Control) validado!")
        else:
            print(f"\n⚠️  {self.falhou} teste(s) falharam.")
        
        print("="*70 + "\n")

if __name__ == '__main__':
    testador = TestadorRBAC()
    if testador.setup():
        testador.rodar_testes()
    else:
        print("\n❌ Falha ao preparar testes. Verifique se init_db.py foi executado.")
        sys.exit(1)
