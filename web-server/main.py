import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return[1,2,3]

@app.get('/contac', response_class=HTMLResponse)
def get_list():
    return """
        <title>Web-server</title>
        <h1>Hola soy una pagina</h1>
        <p>soy un parrafo</p>
     """ 

@app.get('/Soffi-web', response_class=HTMLResponse)
def get_list():
    return """
        <title>Sofi-Web</title>
        <h1>Hola Sofi Bienvenida a Soffi-Web</h1>
        <p>Soffi-Web es una pagina creada para ti</p>
     """

def run():
    store.get_catergories()

if __name__ == '__main__':
    run()