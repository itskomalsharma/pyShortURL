import string
import random
import sqlite3
from flask import *

app=Flask(__name__)

@app.route("/")
def home():
    data = {
        "host":request.host_url
    }
    return render_template("design.html",data=data)
    
@app.route("/<code>")
def home_code(code):
    con = sqlite3.connect("url_shortner.sqlite")  
    myconn=con.cursor()
    myconn.execute("SELECT * FROM url WHERE random_code='"+code+"'")
    data = myconn.fetchone()
    return '<meta http-equiv = "refresh" content = "0; url = '+data[1]+'" />'
    
@app.route("/mydata",methods=['POST'])
def mydata():
    try:
        mycode = ''.join(random.choices(string.ascii_uppercase +string.digits, k = 6))
        con = sqlite3.connect("url_shortner.sqlite")  
        myconn=con.cursor()
        myconn.execute("insert into url (long_url,random_code) values('"+request.form['long_url']+"','"+mycode+"')")
        con.commit()
        return '{"status":true, "code":"'+request.host_url+mycode+'"}'
    except:
        return '{"status":false}'
    
    
if __name__=='__main__':
    app.run(debug = True)
