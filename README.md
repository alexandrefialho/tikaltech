# Tikal Tech - Find Index

[![Python](https://img.shields.io/badge/python-3.7.3-blue.svg)]()

Primeiramente iremos baixar o python na máquina.

MacOS: https://www.python.org/ftp/python/3.7.3/python-3.7.3-macosx10.9.pkg 

Windows: https://www.python.org/ftp/python/3.7.3/python-3.7.3-amd64.exe

Após a instalação do python ser concluida, precisaremos instalar o Virtualenv para que possamos criar ambientes virtuals para encapsular as dependências do projeto.

Em seu terminal, execute o seguinte comando:

```
pip install virtualenv
```

Após a instalação do Virtualenv ser concluída, vá até a raiz do projeto tikaltech e execute o seguinte comando:

```
virtualenv venv
```

Em seguida, iremos acessar esse ambiente virtual que acabamos de criar, então em seu terminal execute o seguinte comando:

```
source venv/bin/activate
```

Pronto agora estamos dentro de um ambiente virtual seguro para que possamos instalar as dependências do projeto, para isso iremos executar o seguinte comando:

```
pip install -r requirements.txt
```

Após isso, estamos preparados para executar o projeto, então vamos lá, em seu terminal execute o seguinte comando:

```
python manage.py runserver
```

Esse comando ira criar uma instancia do projeto dentro da sua maquina apontando pra port
