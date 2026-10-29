# Relatório Final - Gerência de Configuração de Software

**Projeto:** To-Do GCS
**Grupo:** Aluno A, Aluno B, Aluno C, Aluno D
**Repositório:** https://github.com/<org>/todo-gcs

## 1. Estrutura do repositório e política de branching
Estrutura de pastas:
```
todo-gcs/
├── README.md  CONTRIBUTING.md  .gitignore  requirements.txt
├── src/app.py
├── tests/test_app.py
└── docs/
```
Adotamos Git Flow simplificado: `main` guarda versões estáveis etiquetadas;
`develop` integra o trabalho; `feature/*` e `bugfix/*` são branches curtas criadas
a partir de `develop` e apagadas após o merge. Todo merge ocorre via Pull Request
com ao menos 1 aprovação do revisor. Convenções: Conventional Commits e SemVer.

*[Inserir diagrama de branches e print da proteção de branch]*

## 2. Dificuldades e soluções adotadas
| Dificuldade | Solução |
|---|---|
| Criar branch sem atualizar `develop` | Regra no CONTRIBUTING: sempre `git pull` antes de ramificar |
| Mensagens de commit fora do padrão | Revisor passou a checar o formato no PR |
| Dúvida ao interpretar marcadores de conflito | Primeira resolução feita em conjunto e documentada |
| Branches antigas acumuladas | Apagar a branch após o merge |
| *[acrescentar dificuldades reais do grupo]* | |

## 3. Exemplo de conflito e resolução
- **Arquivo:** `src/app.py`, função `mensagem_boas_vindas()`
- **Causa:** B e C alteraram a mesma linha em branches paralelas; o PR de B foi mesclado primeiro.
- **Trecho conflitante:**
```
<<<<<<< HEAD
    return "To-Do: pronto para usar"
=======
    return "Olá! Bem-vindo ao To-Do GCS"
>>>>>>> origin/develop
```
- **Resolução:** combinamos as duas versões em `"Olá! To-Do GCS: pronto para usar"`,
  removemos os marcadores, rodamos os testes e fizemos o commit
  `merge: resolve conflito de saudação em app.py`.

*[Inserir prints: PR com conflito, editor com marcadores, commit de resolução]*

## 4. Histórico de commits e versões
*[Inserir print de `git log --oneline --graph --all --decorate`]*

| Tag | Descrição |
|---|---|
| v0.1.0 | Estrutura inicial |
| v1.0.0 | Primeira versão estável (CRUD de tarefas) |
| v1.1.0 | Filtro por status |
| v2.0.0 | Persistência em arquivo (API alterada) |

*[Inserir print da página de Releases]*

## 5. Conclusões sobre a importância do GCS
O GCS permitiu que quatro pessoas trabalhassem em paralelo sem sobrescrever o
trabalho umas das outras. As convenções de commit tornaram cada mudança rastreável
(quem, quando e por quê). As tags possibilitam retornar a qualquer versão estável, e
a revisão por Pull Request elevou a qualidade do código. O conflito simulado mostrou
que divergências são normais e resolvíveis quando existe processo definido. Sem GCS,
o projeto ficaria sujeito a perda de trabalho, versões ambíguas e falta de
responsabilização.
