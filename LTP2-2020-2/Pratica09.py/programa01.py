
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/ola')
def ola():
    return 'Ola mundo!\nMeu nome é Gabriel Vieira!'

@app.route('/pagina')
def primeira_pagina():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Page Title</title>
        </head>
        <body>
            <h1>This is a Heading</h1>
            <p>This is a paragraph.</p>
        </body>
    </html>
    """

@app.route('/pagina2')
def segunda_pagina():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Meu Site um Pouco Melhor</title>
        </head>
        <body>
            <h1>Informações</h1>
            <p>Este texto é sobre informações gerais.</p>
            <p>Mias detalhes serão apresentados no futuro!</p>
            <iframe width="560" height="315" src="https://www.youtube.com/embed/b3nEaIPNx6Y" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"allowfullscreen></iframe>
            <img class="rg_i Q4LuWd" src="data:image/jpeg;base64,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" data-deferred="1" jsname="Q4LuWd" width="200" height="200" alt="Violino 4/4 Classic Series VE441 Envernizado EAGLE - Sonkey" data-iml="2885.765000246465" data-atf="true">
        </body>
    </html>
"""

@app.route('/eu')
def terceira_pagina():
    return """
    <!DOCTYPE html>
    <html>
        <body>

            <button onclick="myFunction()" type="button">Get the number of available audio tracks</button>
        <br><br>

        <video id="myVideo" width="320" height="176" controls>
  <source src="mov_bbb.mp4" type="video/mp4">
  <source src="mov_bbb.ogg" type="video/ogg">
  Your browser does not support HTML5 video.
</video>

<script>
var vid = document.getElementById("myVideo");
function myFunction() {
  alert(vid.audioTracks.length);
}
</script>

<p>Video courtesy of <a href="https://www.bigbuckbunny.org/" target="_blank">Big Buck Bunny</a>.</p>

</body>
</html>
"""
@app.route('/ola2')
def rodar_pagina_html():
    return render_template('ola.html')

@app.route('/cv')
def mostrar_curriculo():
    return render_template('cv.html')
