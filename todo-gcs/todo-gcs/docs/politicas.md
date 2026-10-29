# Políticas de Gerência de Configuração

## Itens de configuração
| Item | Local |
|---|---|
| Código-fonte | `src/` |
| Testes | `tests/` |
| Documentação | `docs/`, `README.md`, `CONTRIBUTING.md` |
| Configuração | `.gitignore`, `requirements.txt` |
| Relatório final | `docs/relatorio.md` |

## Nomeação
- Arquivos e pastas: `snake_case`
- Branches: `tipo/descricao-curta`
- Tags: `vMAJOR.MINOR.PATCH`

## Versionamento
SemVer. Marcos previstos: v0.1.0 (estrutura), v1.0.0 (CRUD de tarefas),
v1.1.0 (filtro por status), v2.0.0 (persistência em arquivo, API alterada).

## Branching
`main` (estável, protegida) ← `develop` (integração, protegida) ← `feature/*`, `bugfix/*`.
Merge somente via Pull Request com 1 aprovação.

## Backup e recuperação
- Remoto no GitHub + clone local de cada integrante.
- A cada release: `git clone --mirror <url> backup-vX.Y.Z.git`.
- Recuperação: `git revert <hash>`, `git reflog`, `git checkout vX.Y.Z`.

## Papéis
| Papel | Responsabilidade |
|---|---|
| Gestor de Configuração | Repositório, proteção de branches, tags e releases |
| Desenvolvedor principal | Funcionalidades centrais |
| Desenvolvedor | Funcionalidades secundárias |
| Revisor de código | Revisão e aprovação de PRs |
