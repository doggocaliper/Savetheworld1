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

@app.route("/reportabully.html")
def reportabully():
  return render_template('reportabully.html')

# @app.route("/<name>")
# def user(name):
#   return f"Hello {name}"

@app.route("/index.html")
def admin():
  return redirect(url_for("homepage"))
  
if __name__ == "__name__":
  app.run()



app.run(host='0.0.0.0', port=81)
