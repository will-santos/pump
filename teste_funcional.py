import unittest
from selenium import webdriver


class TesteCadastroUsuario(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_cadastrar_um_novo_usuario_valido(self):
        # Usuario entra na sessão de cadastro
        self.browser.get('http://localhost:5000/cadastro')
        # Então ele ve um formulario de cadastro

        # Ele também ve o botão cadastra esta desativado.
        # No formumalario tem um campo nome

        # Ele entra com seu nome 'Fuluno'
        # Depois logo em baixo ele ver o campo de email
        # Então ele preenche com com email 'fulano@gmail.com'
        # Em seguida ele ve o campo de senha e confirmação de senha
        # Ele preenche os dois com a senha 'Fulando123TESTE!'
        # Ele vê os campos ficarem verdes mostrando que senhas são validas
        # Em seguida o botão cadastra fica ativo
        # E ele preciona.

if __name__ == '__main__':
    unittest.main()
