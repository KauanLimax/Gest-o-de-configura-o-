# Roteiro de comandos

## 1. Setup (Gestor A)
```bash
git clone https://github.com/<org>/todo-gcs.git && cd todo-gcs
# copie os arquivos do projeto para a pasta
git add . && git commit -m "chore: estrutura inicial do projeto"
git push
git checkout -b develop && git push -u origin develop
git tag -a v0.1.0 -m "Estrutura inicial" && git push origin v0.1.0
```
GitHub: *Settings → Branches* (proteger `main` e `develop`: exigir PR e 1 aprovação)
e *Settings → Collaborators* (adicionar colegas).

## 2. Fluxo normal (cada dev)
```bash
git checkout develop && git pull
git checkout -b feature/<nome>
git add . && git commit -m "feat(escopo): descrição"
git push -u origin feature/<nome>
# abrir PR para develop -> revisor aprova -> merge
```

Sugestão de tarefas:
- B: `feature/remover-tarefa` -> `feat(tarefas): melhora remoção`
- C: `feature/filtro-status` -> `feat(tarefas): adiciona filtro por status`
- D: revisa; faz `test(app): adiciona testes de filtro`

## 3. Conflito 1 - código (`src/app.py`)
Alunos B e C partem do mesmo `develop` e editam a MESMA linha:

Aluno B (`feature/saudacao-formal`):
```python
    return "Olá! Bem-vindo ao To-Do GCS"
```
```bash
git commit -am "feat(app): torna saudação formal" && git push -u origin feature/saudacao-formal
```
Aluno C (`feature/saudacao-curta`):
```python
    return "To-Do: pronto para usar"
```
```bash
git commit -am "feat(app): encurta saudação" && git push -u origin feature/saudacao-curta
```
O PR de B é mesclado primeiro. O PR de C acusa conflito. Aluno C resolve:
```bash
git checkout feature/saudacao-curta
git fetch origin
git merge origin/develop        # CONFLICT (content) in src/app.py
```
Edite o arquivo, remova `<<<<<<<`, `=======`, `>>>>>>>` e deixe, por exemplo:
```python
    return "Olá! To-Do GCS: pronto para usar"
```
```bash
python -m unittest discover -s tests
git add src/app.py
git commit -m "merge: resolve conflito de saudação em app.py"
git push
```

## 4. Conflito 2 - documentação (`README.md`)
B e C editam a mesma linha da seção "Como executar" em branches `docs/*`
diferentes; repita o processo de merge e resolução acima.

## 5. Releases (Gestor A)
```bash
git checkout main && git pull && git merge develop && git push
git tag -a v1.0.0 -m "Primeira versão estável: CRUD de tarefas" && git push origin v1.0.0
# depois de novas features
git tag -a v1.1.0 -m "Filtro por status"
# depois de mudança incompatível
git tag -a v2.0.0 -m "Persistência em arquivo (API alterada)"
git push origin --tags
```
GitHub: *Releases → Draft a new release* para cada tag.

## 6. Recuperação (demonstração)
```bash
git revert <hash>               # desfaz um commit com novo commit
git reflog                      # localiza commits "perdidos"
git checkout v1.0.0             # volta a uma versão estável
git clone --mirror <url> backup.git
```

## 7. Prints obrigatórios
- Proteção de branch; PR com conflito; marcadores no editor; commit de resolução
- `git log --oneline --graph --all --decorate`
- Página de Releases com as tags
