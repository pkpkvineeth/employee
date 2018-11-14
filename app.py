from flask import Flask,render_template
from emp import employee
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')
@app.route('/employeeDetails')
def employeee():
    employ=employee()
    return render_template('employee.html',employeeDetails=employ)

if(__name__=='__main__'):
    app.run(debug=True)