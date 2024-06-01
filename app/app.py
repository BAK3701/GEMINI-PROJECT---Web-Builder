from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)


@app.route('/',methods=['POST','GET'])

def index():
    if request.method == 'POST':
        pass
        
    else:
        return render_template('index.html')
    
if __name__ == "__main__":
    app.run(debug=True)