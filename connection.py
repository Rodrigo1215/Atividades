from flaskext.mysql import MySQL
from flask import Flask, render_template, request

mysql = MySQL()
app = Flask(__name__)
app.url_map.strict_slashes = False


app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admin'
app.config['MYSQL_DATABASE_DB'] = 'teste'
app.config['MYSQL_DATABASE_HOST'] = '172.17.0.2'
mysql.init_app(app)

conexao = mysql.connect()
cursor = conexao.cursor()



@app.route('/')
def main():
    return render_template('connection.html')


@app.route("/adicionar_usuario", methods=['POST', 'GET'])
def incluir_usuario():
    cursor = conexao.cursor()
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    cursor.execute("""INSERT INTO tb_usuarios(nome, email, senha) VALUES(%s, %s, %s)""", (nome, email, senha))
    conexao.commit()
    cursor.close()
    conexao.close()
    return render_template('connection.html')
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)