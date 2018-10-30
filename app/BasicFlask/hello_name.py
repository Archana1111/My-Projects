from flask import Flask
app=Flask(__name__)

@app.route("/string/<name>")
def hello_str(name):
    return "Hello %s" %name

@app.route("/integer/<int:i>") 
def hello_int(i):
    return "Hello %d" %i

@app.route("/float/<float:f>") 
def hello_float(f):
    return "Hello %f" %f

@app.route("/name/<str1><str2>")
def concat(str1,str2):
    c=str1+str2
    return "Hello %s" %c

if __name__=="__main__":
    app.run()

