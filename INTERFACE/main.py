
from flask import Flask,render_template,request
#from link import *
from new import *
app = Flask(__name__)
@app.route('/')
def my_form():
    return render_template("home.html")

@app.route('/data',methods=["POST"])
def form_data():
    if request.method == "POST":
       c_name=request.form.get("company_name")
       start_time=request.form.get("start_time")
       end_time=request.form.get("end_time")
       start_time =reverse_date(start_time)
       end_time  =reverse_date(end_time)
       keyword=request.form.get("keyword")
       result=company_details(c_name,keyword,start_time,end_time)
       #return str(result)
       return render_template('home.html',result = result)
       #return str([start_time,end_time])



if __name__ == '__main__':
    app.run(debug=True)