from flask import Flask
import time

app = Flask(__name__)

def seconds_since_epoch():
    epoch = time.time()
    return int(epoch)

@app.route("/")
def seconds():
    return str(seconds_since_epoch())
    
def minutes_since_epoch():
    epoch = time.time() 


    def hours_since_epoch():
        epoch = time.time()
        return int(epoch // 3600)

    @app.route("/hours")
    def hours():
        return str(hours_since_epoch())
