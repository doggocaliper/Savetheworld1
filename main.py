from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def homepage():
  return render_template('index.html')

@app.route("/adoption.html")
def adoption():
  return render_template('adoption.html')
  
@app.route("/confession.html", methods=['POST', 'GET'])
def confess():
    if request.method == 'POST':
        confession = request.form['confession']
        with open('data.txt', 'a') as file:
          file.write(confession + ' \n')
        return redirect(url_for('confess', confession = confession))
#    else:
#      user = request.args.get('confession')
#      return redirect(url_for('confess', confession = confession))
    return render_template('confession.html')

@app.route("/whatnext.html")
def whatnext():
  return render_template('whatnext.html')

@app.route("/reportabully.html", methods=['POST', 'GET'])
def reportabully():
    if request.method == 'POST':
        name = str(request.form.get('name'))
        name1 = str(request.form.get('name1'))
        description = str(request.form.get('description'))
        detail = str(request.form.get('detail'))
        with open('reports.txt', 'a') as file:
          file.write('Name of reportee: ' + name + ' \nName of bully: ' + name1 + ' \nDescription of bully: ' + description + ' \nDetail of assault: ' + detail + ' \n')
        return redirect(url_for('reportabully', name = name, name1 = name1, description = description, detail = detail))
    return render_template('reportabully.html')

@app.route('/confessionlist.html')
def confessions():
    with open('data.txt', 'r') as file:
        confessions = file.readlines()
    return render_template('confessionlist.html', confessions=confessions)

# @app.route("/<name>")
# def user(name):
#   return f"Hello {name}"

@app.route("/index.html")
def admin():
  return redirect(url_for("homepage"))
  
if __name__ == "__name__":
  app.run()



app.run(host='0.0.0.0', port=81)
