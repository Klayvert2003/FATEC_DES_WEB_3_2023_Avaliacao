import time
import random
from django.test import TestCase, LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

class TesteRegistrarPresenca(LiveServerTestCase):
    def __init__(self, *args, **kwargs):
        self.address = kwargs.pop('address', 'http://127.0.0.1:8000')
        super().__init__(*args, **kwargs)

    def test_register_user(self):
        sc = webdriver.Chrome()
        sc.get(self.address)
        sc.maximize_window()
        time.sleep(3)
        
        alunos = ['Klayvert Ryan Alves', 'Zézinho da Silva', 'Paulo dos Santos']
        professores = ['Orlando', 'Tiago', 'Zenaide', 'Nilton']
        cursos = ['DSM', 'SI', 'GE']
        
        for aluno in alunos:
            input_aluno = sc.find_element(By.XPATH, '//input[@name="nome_aluno"]')
            input_aluno.send_keys(aluno)
            time.sleep(3)
        
            sc.find_element(By.XPATH, '//select[@name="nome_professor"]').click()
            sc.find_element(By.XPATH, f'//option[text()="{random.choice(professores)}"]').click()
            time.sleep(3)
            
            sc.find_element(By.XPATH, '//select[@id="id_curso"]').click()
            sc.find_element(By.XPATH, F'//option[text()="{random.choice(cursos)}"]').click()
            time.sleep(3)
        
            sc.find_element(By.XPATH, '//button[text()="Registrar Presença"]').click()
            time.sleep(3)
            sc.find_element(By.XPATH, '//a[text()="Registro de Presença"]').click()
            time.sleep(0.5)
            
class TesteRegistraPresenca(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_200_response_Index(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template_Index(self):
        self.assertTemplateUsed(self.resp, 'registra_presenca.html')
        
class TesteListaAlunos(TestCase):
    def setUp(self):
        self.resp = self.client.get('/lista_alunos')

    def test_200_response_Index(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template_Index(self):
        self.assertTemplateUsed(self.resp, 'lista_alunos.html')