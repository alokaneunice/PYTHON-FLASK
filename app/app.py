from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def homepage():
    name = "Mrs Akinfolaju"
    return render_template("homepage.html", name=name)

@app.route("/about")
def about():
    return "Welcome to about us page!"

@app.route("/services")
def services():
    return "Welcome to our services page!"

@app.route("/maths")
def maths():
    a = 5
    b = 10
    c = a+b
    return render_template("maths.html", maths_result=c)

@app.route("/multiply")
def multiply():
    a = 14
    b = 15
    c = 20
    d = a*b*c
    return render_template("multiply.html", multiply_result=d)

@app.route("/division")
def division():
    a = 100
    b = 15
    c = a/b
    return "hurray!, you are correct. This is the result " + str (c)

if __name__ == '__main__':
   app.run(host='127.0.0.1', port=5001, debug =True)
   

#create a route to return contact us, showing email address and phone number and display on the website using python
@app.route("/contact")
def contact():
    email = "acheeunice@gmail.com"
    phone_number = "08067385754"
    return "Our contact details are : " + email + "," + phone_number

    
@app.route("/task")
def task():
    a = 91
    b = 81
    c = 71
    d = a+b+c
    f = d-50
    return "Yes, I got it! This is the final result" + str(f)

if __name__ == '__main__':
   app.run(host='127.0.0.1', port=5001, debug =True)