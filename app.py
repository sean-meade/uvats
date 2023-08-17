from flask import Flask, render_template, request
from uvats.uvats import solve_uvats

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')

    u = request.form.get('u')
    v = request.form.get('v')
    a = request.form.get('a')
    t = request.form.get('t')
    s = request.form.get('s')

    solve_uvats(u, v, a, t, s)

    return render_template('index.html')

if __name__ == '__main__':
    app.run()