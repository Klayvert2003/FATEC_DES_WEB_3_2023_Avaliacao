from django import forms

class FormularioPresenca(forms.Form):
    nome_aluno = forms.CharField(label='Nome do Aluno', max_length=100)
    nome_professor = forms.ChoiceField(label='Nome do Professor', choices=[('Orlando', 'Orlando'), ('Tiago', 'Tiago'), ('Zenaide', 'Zenaide'), ('Nilton', 'Nilton')])
    curso = forms.ChoiceField(label='Nome do seu Curso', choices=[('DSM', 'DSM'), ('SI', 'SI'), ('GE', 'GE')])