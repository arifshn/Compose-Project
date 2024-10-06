#Bazı temel bileşenleri framework den içe aktarıyorum 
from flask import Flask, render_template, request
#Python ile yazılmış web uygulamalarında  web çatısı olarak çalışır
app = Flask(__name__)
#Fonksiyonları tanımlıyorum 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    return render_template('success.html', name=name, email=email)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
