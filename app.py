from flask import Flask, request, render_template

app = Flask(__name__)

def gerar_cabecalho():
    return "<h1>Avaliação contínua: Aula 030</h1>"

@app.route('/')
def index():
    return f"""
    {gerar_cabecalho()}
    <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/user/Thomas Luizon/PT3019438/IFSP">Identificação</a></li>
        <li><a href="/contextorequisicao">Contexto da requisição</a></li>
    </ul>
    """

@app.route('/user/<name>/<prontuario>/<instituicao>')
def user(name, prontuario, instituicao):
    return f"""
    {gerar_cabecalho()}
    <h2>Aluno: {name}</h2>
    <h2>Prontuário: {prontuario}</h2>
    <h2>Instituição: {instituicao}</h2>
    <p><a href="/">Voltar</a></p>
    """

@app.route('/contextorequisicao')
def contextorequisicao():
    user_agent = request.headers.get('User-Agent')
    remote_ip = request.remote_addr
    host = request.host
    return f"""
    {gerar_cabecalho()}
    <h2>Seu navegador é: {user_agent}</h2>
    <h2>O IP do computador remoto é: {remote_ip}</h2>
    <h2>O host da aplicação é: {host}</h2>
    <p><a href="/">Voltar</a></p>
    """

if __name__ == '__main__':
    app.run(debug=True)
