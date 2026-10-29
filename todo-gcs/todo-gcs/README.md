# To-Do GCS

Aplicação de lista de tarefas em Python (linha de comando), desenvolvida para a
disciplina de Gerência de Configuração de Software (GCS).

## Equipe

| Integrante | Papel |
|---|---|
| Aluno A | Gestor de Configuração |
| Aluno B | Desenvolvedor principal |
| Aluno C | Desenvolvedor |
| Aluno D | Revisor de código |

## Como executar

```bash
python src/app.py
```

## Como testar

```bash
python -m unittest discover -s tests -v
```

## Estrutura

```
todo-gcs/
├── README.md
├── CONTRIBUTING.md
├── .gitignore
├── requirements.txt
├── src/app.py
├── tests/test_app.py
└── docs/politicas.md
```

## Políticas (resumo)

- Versionamento: SemVer (`vMAJOR.MINOR.PATCH`)
- Commits: Conventional Commits
- Branching: `main` (estável) ← `develop` ← `feature/*`, `bugfix/*`
- Detalhes em [CONTRIBUTING.md](CONTRIBUTING.md) e [docs/politicas.md](docs/politicas.md)
