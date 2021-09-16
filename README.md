# Pokedex

Projeto para construir uma réplica da Pokedex da primeira geração do Pokemon

![pokedex 1 ger](https://user-images.githubusercontent.com/30854324/131939630-de23eadc-da62-4577-b4be-698927776ee4.png)


# Dev Environment

## Conda Environments

[Conda cheatsheet](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)

### Criando env a partir de um `environment.yml`:

```
conda env create -f environment.yml
```

### Atualizando um env a partir de um `environment.yml`:

1. Entrar no diretório do `environment.yml`

2. Ativar o env:

```
conda activate {nome_env}
```

3. Atualizar:

Devido a um bug no comando `conda env update`, caso o env possua uma dependência que não consta no `environment.yml`,
ela não será removida. Portanto, para garantirmos que **apenas as dependências do `.yml` sejam incluídas, usamos o
comando:**

```
conda env create --force
```

### Listando todos os envs:

```
conda env list
```

### Ativando um env:

```
conda activate {nome_env}
```

# Dependências Externas

Dependências externas deverão ser salvas na pasta `./lib`. Elas não serão salvas no GitHub para manter o tamanho do
projeto reduzido.

Em compensação, cada dependência será descrita a seguir, para elas poderem ser replicadas.

### MicroPython

[Local para download e tutorial de instalação.](https://www.raspberrypi.org/documentation/microcontrollers/micropython.html)

Para instalar, ligue o Raspberry Pi Pico segurando o `BOOT SEL` e cole o arquivo `*.uf2` baixado para dentro da placa.

Implementação enxuta de Python 3, que executa em hardwares como o Raspberry Pi Pico, através de um prompt REPL.

A comunicação se dá através de comunicação USB serial e ele conta com um filesystem FAT e bibliotecas dedicadas ao
controle de baixo nível de microcontroladores.

### Circuit Python

CircuitPython é semelhante ao MicroPython, porém com mais funcionalidades, como poder acessar os arquivos armazenados
dentro do Raspberry Pi Pico diretamente via USB, como se fosse um pen-drive.

Essa instalação consta em duas partes: driver e bundle

#### Driver:

[Local para download](https://circuitpython.org/board/raspberry_pi_pico/)

Para instalar o driver, ligue o Raspberry Pi Pico segurando o `BOOT SEL` e cole o arquivo `*.uf2` baixado para dentro da
placa.

#### Bundle:

[Local para download e instruções de instalação](https://circuitpython.org/libraries)

Para ter acesso a diversos módulos Python dentro do CircuitPython, é preciso baixar um bundle.

Baixe o bundle, descompacte o arquivo, navegue até a pasta `lib` e escolha quais dependências quer utilizar.

Para carregar as dependências no Raspberry Pi Pico, basta colar os módulos desejados dentro da pasta `lib` da placa.

**Usar esse ao invés do MicroPython.**

### Thonny

[Local para download](https://thonny.org/) e
[tutorial de conexão com Raspberry Pi Pico](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico)

IDE para Python e com capacidade de se comunicar diretamente com o Raspberry Pi Pico, via USB.
