from flask import Flask, redirect, url_for, request, render_template_string

app = Flask(__name__)

# Template HTML untuk form login
login_template = """
<html>
   <body>
      <form action="{{ url_for('login') }}" method="post">
         <p>Enter Name:</p>
         <p><input type="text" name="nm" /></p>
         <p><input type="submit" value="Submit" /></p>
      </form>   
   </body>
</html>
"""

# Template HTML untuk halaman sukses
success_template = """
<html>
   <body>
      <h1>Welcome {{ name }}!</h1>
   </body>
</html>
"""

@app.route('/success/<name>')
def success(name):
    return render_template_string(success_template, name=name)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        return render_template_string(login_template)

if __name__ == '__main__':
    app.run(debug=True)
