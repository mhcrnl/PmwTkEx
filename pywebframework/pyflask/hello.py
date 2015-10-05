from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "SALUT Romania!"

if __name__=="__main__":
    app.debug = True #Daca codul s-a schimbat serverui reicarca codul
    app.run()
    
