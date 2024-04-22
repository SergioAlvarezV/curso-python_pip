# Game Projec

Para correr el juego debes seguir las siguientes intrucciones en la terminal:

```sh
cd Game
python3 main.py
```


# App Projec

```sh
git clone
cd app/
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
python3 main.py
```


# Web-Server Projec

```sh
git clone
cd web-server
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
uvicorn main:app --reload
in the browser localhost:8000 or puerto desing
localhost:8000/contac is web-server
```


# Web-Server Projec whit Docker

```sh
git clone
cd web-server
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
run  program Docker
In cmd  docker-compose build
docker-compose up -d
docker-compose ps
In program Docker search web-server
In web-server copy or click in the ip
localhost:8000/contac is web-server
```
