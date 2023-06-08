#django functions
from django.shortcuts import render, redirect
from django.views import View

# My functions
from .forms import FormularioPresenca
from .models import RegistroPresenca

class RegistraPresenca(View):
    def get(self, request):
        form = FormularioPresenca()
        return render(request, 'registra_presenca.html', {'form': form})
    
    def post(self, request):
        form = FormularioPresenca(request.POST)
        
        if form.is_valid():
            nome_aluno = form.cleaned_data['nome_aluno']
            nome_professor = form.cleaned_data['nome_professor']
            curso_aluno = form.cleaned_data['curso']
            registro = RegistroPresenca(nome_aluno=nome_aluno, nome_professor=nome_professor, curso_aluno=curso_aluno)
            registro.save()
            return redirect('lista_alunos')
        else:
            return redirect('registra_presenca')
            
class ListagemAlunos(View):
    def get(self, request):
        alunos = list(RegistroPresenca.objects.all())
        
        return render(request, 'lista_alunos.html', {'dados': alunos})