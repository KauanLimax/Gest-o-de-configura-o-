# Guia de Contribuição

## Fluxo de trabalho

1. Nunca faça push direto em `main` ou `develop`.
2. Atualize e crie sua branch a partir de `develop`:
   ```bash
   git checkout develop && git pull
   git checkout -b feature/nome-curto
   ```
3. Faça commits pequenos e padronizados (veja abaixo).
4. Envie a branch e abra um Pull Request para `develop`:
   ```bash
   git push -u origin feature/nome-curto
   ```
5. O revisor aprova (mínimo 1 aprovação) ou pede ajustes.
6. Após o merge, apague a branch.
7. Releases: o Gestor de Configuração mescla `develop` em `main` e cria a tag `vX.Y.Z`.

## Convenção de branches

| Prefixo | Uso | Exemplo |
|---|---|---|
| `feature/` | nova funcionalidade | `feature/remover-tarefa` |
| `bugfix/` | correção de bug | `bugfix/indice-invalido` |
| `docs/` | documentação | `docs/atualiza-readme` |
| `hotfix/` | correção urgente em `main` | `hotfix/erro-critico` |

## Convenção de commits (Conventional Commits)

Formato: `tipo(escopo): descrição curta no imperativo`

| Tipo | Quando usar |
|---|---|
| `feat` | nova funcionalidade |
| `fix` | correção de bug |
| `docs` | documentação |
| `test` | testes |
| `refactor` | refatoração sem mudar comportamento |
| `style` | formatação |
| `chore` | tarefas de manutenção/configuração |
| `merge` | resolução de conflitos |

Exemplos:
- `feat(tarefas): adiciona remoção de tarefa`
- `fix(app): corrige índice inválido ao concluir`
- `docs(readme): atualiza instruções de execução`

## Versionamento (SemVer)

- **MAJOR**: mudança incompatível (v2.0.0)
- **MINOR**: nova funcionalidade compatível (v1.1.0)
- **PATCH**: correção de bug (v1.0.1)

## Checklist do Pull Request

- [ ] Commits seguem a convenção
- [ ] Testes passam
- [ ] Branch atualizada com `develop`
- [ ] Revisor atribuído
