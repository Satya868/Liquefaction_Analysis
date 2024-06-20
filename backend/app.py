from flask import Flask, render_template, request, jsonify
from main import satya

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/submit', methods = ['POST'])
def submit():
    if request.method == 'POST' or request.method == 'PUT':
        data = request.json

        cont = list(data.values())

        for i in range(len(cont)):
            cont[i] = float(cont[i])

        av = [[7.9,	96.3,	40,	0.21,	9,	9,	0.5,	16.01,	32,	1.5,	1.5,	0]]

        print("Below Line contain the modified data")
        print(cont)  
        
        fork = [cont]
        # fork = av
        result = satya(fork)

        result = result[0]
        print(result)

        return{
            "count" : result
        }
    else:
        return {
            # render_template('res.html', res = "Error hai bro !!!!")
            
            "error" : "Bro kuch error hai"  
        }
          


if __name__ == "__main__":
    app.run( debug = True)
