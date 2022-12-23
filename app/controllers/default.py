from app import app

@app.route('/index')
@app.route("/")
def index():
    return "Hello World!"

# @app.route("/test", defaults={'name': None}) outro modo de não precisar passar o nome 
@app.route("/test", methods=['GET'])#methods limita a pagina a fazer apenas GET nesse caso
@app.route('/test/<name>')
def teste(name=None):
    if name: 
        return 'Olá, %s!' % name
    else: 
        return "Olá, usuário!"