from django.shortcuts import render
from .models import Igreja, Usuario, Classe, Trimestre, Aula, Professor, Diario, Aluno, Presenca, Matricula

def IgrejaViewSet(request):
    return render(request, 'base/home.html')

## Controle de Acesso
'''
class UsuarioViewSet(request):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ClasseViewSet(request):
    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer

class TrimestreViewSet(request):
    queryset = Trimestre.objects.all()
    serializer_class = TrimestreSerializer

class AulaViewSet(request):
    queryset = Aula.objects.all()
    serializer_class = AulaSerializer

class ProfessorViewSet(request):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class DiarioViewSet(request):
    queryset = Diario.objects.all()
    serializer_class = DiarioSerializer

class AlunoViewSet(request):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class PresencaViewSet(request):
    queryset = Presenca.objects.all()
    serializer_class = PresencaSerializer

class MatriculaViewSet(request):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

# Create your views here.
'''