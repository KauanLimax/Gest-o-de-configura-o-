import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import app  # noqa: E402


class TestApp(unittest.TestCase):
    def setUp(self):
        app.tarefas.clear()

    def test_adicionar(self):
        i = app.adicionar("Estudar GCS")
        self.assertEqual(i, 0)
        self.assertEqual(len(app.listar()), 1)

    def test_adicionar_vazio(self):
        with self.assertRaises(ValueError):
            app.adicionar("   ")

    def test_concluir(self):
        app.adicionar("Tarefa")
        app.concluir(0)
        self.assertTrue(app.listar()[0]["concluida"])

    def test_remover(self):
        app.adicionar("Tarefa")
        app.remover(0)
        self.assertEqual(app.listar(), [])

    def test_indice_invalido(self):
        with self.assertRaises(IndexError):
            app.concluir(5)


if __name__ == "__main__":
    unittest.main()
