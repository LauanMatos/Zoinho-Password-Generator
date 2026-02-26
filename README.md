# 👽 Zoinho Password Generator

Fiz esse gerador de senhas enquanto estudava Python. Ele roda no terminal, pergunta o que você quer e entrega uma senha com barra de progresso e tudo.

## O que ele faz

- Escolhe o tamanho da senha
- Põe maiúscula se quiser
- Põe número se quiser
- Põe símbolo se quiser
- Mostra uma barra de progresso enquanto gera
- Diz se a senha é fraca, média, forte ou muito forte
- Fica num loop até você pedir pra sair

## Como usar

```bash
git clone https://github.com/LauanMatos/Zoinho-Password-Generator.git
cd Zoinho-Password-Generator
python main.py
```

Depois é só responder as perguntas no terminal.

## O que eu aprendi fazendo isso

- Usar `input` pra pegar resposta do usuário
- Montar string com `if`
- Loop `for` pra repetir coisa
- `random.choice()` pra sortear caractere
- Separar código em arquivos (main, gerador, loading, medidor)
- Botar cor no terminal
- Fazer barra de progresso com `\r`
- Usar Git e subir pro GitHub

## Os arquivos

- `main.py` – o programa principal
- `gerador.py` – a lógica de gerar senha
- `loading.py` – a barra de progresso
- `medidor.py` – classifica a força
- `CHANGELOG.txt` – histórico de versão
- `LICENSE` – licença MIT

## Sobre mim

Sou Lauan, tô aprendendo Python e cibersegurança. Esse é meu primeiro projeto no GitHub.

<<<<<<< HEAD
## ⭐ Se chegou até aqui

Dá uma estrela se quiser, mas não precisa. Já tô feliz de ter conseguido fazer funcionar.
