from flask import Flask, request, render_template, redirect, session, url_for
import ibm_db

app = Flask(__name__)
app.secret_key = "testing"

conn = ibm_db.connect("DATABASE=bludb; HOSTNAME=fbd88901-ebdb-4a4f-a32e-9822b9fb237b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud; PORT=32731; SECURITY=SSL; SSLServerCertificate=DigiCertGlobalRootCA.crt; UID=rfh77431;PWD=1WClhcJWgdCoeAk5",'','')

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        reg_type = request.form["type"]
        email = request.form["email"]
        psw = request.form["psw"]
        session["user_name"] = email
        if(reg_type == "register"):
            name = request.form["name"]
            conf_psw = request.form["conf_pass"]
            session["user_name"] = name

            if(psw == conf_psw):
                id = 1
                sql="INSERT INTO USER(USERID,NAME,EMAIL,PASSWORD) VALUES(?,?,?,?)"
                stmt=ibm_db.prepare(conn,sql)
                ibm_db.bind_param(stmt,1,id)
                ibm_db.bind_param(stmt,2,name)
                ibm_db.bind_param(stmt,3,email)
                ibm_db.bind_param(stmt,4,psw)
                ibm_db.execute(stmt)
                
                return render_template("index.html", user=name)

            else:

                return render_template("index.html")

    else:
        user = ""
        if "user_name" in session:
            user = session["user_name"]
        return render_template("index.html", user=user)

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password']
        sql="SELECT * FROM USER WHERE email=? AND password=?"
        stmt=ibm_db.prepare(conn,sql)
        ibm_db.bind_param(stmt,1,email)
        ibm_db.bind_param(stmt,2,password)
        ibm_db.execute(stmt)
        account=ibm_db.fetch_assoc(stmt)
        print(account)
        if account:
            return redirect(url_for('dashboard'))
        else:
            return redirect(url_for('login'))
    elif request.method=='GET':
        return render_template('index.html')



@app.route('/expense')
def expense():
    return render_template("expense.html") 
   
@app.route('/logout')
def logout():
    session.pop("user_name", None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)