import json
import os
from flask import Flask, request, render_template, jsonify
from flask import url_for

app = Flask(__name__)

SalesDataValues={
        "Fuel": ["CNG","Diesel","Petrol"],
        "VEHICLE_SEGMENT": ["A","B","C"],
        "Power_steering": ["0","1"],
        "airbags": ["0","1"],
        "sunroof": ["0","1"],
        "Matt_finish": ["0","1"],
        "music_system": ["0","1"],
        "Customer_Gender": ["Male","Female"],
        "Customer_Income_group": ["0- $25K","$25-$70K",">$70K"],
        "Customer_Region": ["North","South","East","West"],
        "Customer_Marital_status": ["0","1"]
}

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/sales_details", methods = ['POST', 'GET'])
def sales_details():
    if request.method == 'GET':
        return f"The URL /sales_details is accessed directly. Try going to '/' to submit form"
    if request.method == 'POST':
        id = request.form['sales_id']
        # Opening JSON file
        f = open(os.path.join(app.static_folder,'Salesdata.json'))
        # returns JSON object as a dictionary
        salesdata = json.load(f)
        # Iterating through the json list
        for i in salesdata:
            if(i['sales_id']==id):
                temp=i
        # if ID is present in data return data else print invalid ID
        # if temp in locals():
        #     pass
        # else:
        #     displayErrorMsg="Invalid ID. Please enter a valid email id!"
        return render_template('sales_details', salesIDDetails=temp, salesUniqueValues=SalesDataValues)

@app.route("/editSalesDetails",methods=['POST', 'GET'])
def editSalesDetails():
    if request.method=='POST':
        id = request.form['sales_id']
        detail_name=request.form['detail_name']
        newValue=request.form['newValue']
        # Opening JSON file and load data
        f = open(os.path.join(app.static_folder,'Salesdata.json'))
        # returns JSON object as a dictionary
        salesdata = json.load(f)
        for i in salesdata:
            if(i['sales_id']==id):
                i[detail_name]=newValue
                break
        #write data to json file
        with open("static/Salesdata.json", "w") as f1:
            f1.write(json.dumps(salesdata))
    alertMsg="DB updated successfully"
    return jsonify({'data': alertMsg})


