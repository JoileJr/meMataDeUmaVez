# Como Criar um Ambiente Virtual no Python

Um ambiente virtual permite isolar dependências de projetos Python. Siga os passos abaixo para criar o seu:

## 1. Instale o `virtualenv` (opcional)

```bash
pip install virtualenv
```

## 2. Crie o Ambiente Virtual

No terminal, navegue até a pasta do seu projeto e execute:

```bash
python -m venv nome_do_ambiente
```

Substitua `nome_do_ambiente` pelo nome desejado (ex: `venv`).

## 3. Ative o Ambiente Virtual

- **Windows:**
    ```bash
    nome_do_ambiente\Scripts\activate
    ```
    
## 4. Instale Dependências

Com o ambiente ativado, instale pacotes normalmente usando `pip`.

## 5. Desative o Ambiente Virtual

Quando terminar, execute:

```bash
deactivate
```

Pronto! Agora você pode gerenciar dependências de forma isolada em seus projetos Python.