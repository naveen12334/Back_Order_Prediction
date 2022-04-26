from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("pred_back.pkl", "rb"))



@app.route("/")
@cross_origin()
def home():
    return render_template("home1.html")

@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        national_inv= int(request.form['national_inv'])
        lead_time=int(request.form['lead_time'])
        in_transit_qty= float(request.form['in_transit_qty'])
        forecast_3_month= int(request.form['forecast_3_month'])
        sales_1_month = int(request.form['sales_1_month'])
        min_bank= int(request.form['min_bank'])
        potential_issue= float(request.form['potential_issue'])
        pieces_past_due= float(request.form['pieces_past_due'])
        perf_6_month_avg= int(request.form['perf_6_month_avg'])
        local_bo_qty=float(request.form['local_bo_qty'])
        deck_risk=int(request.form['deck_risk'])
        oe_constraint=float(request.form['oe_constraint'])
        ppap_risk=int(request.form['ppap_risk'])
        stop_auto_buy=int(request.form['stop_auto_buy'])
        rev_stop=float(request.form['rev_stop'])


    prediction=model.predict([[
            national_inv,
            lead_time,
            in_transit_qty,
            forecast_3_month,
            sales_1_month,
            min_bank,
            potential_issue,
            pieces_past_due,
            perf_6_month_avg,
            local_bo_qty,
            deck_risk,
            oe_constraint,
            ppap_risk,
            stop_auto_buy,
            rev_stop

        ]])
    output=prediction
    

    return render_template('home1.html',prediction_text="Product Bacordered {}".format(output))


    return render_template("home1.html")




if __name__ == "__main__":
    app.run(debug=True)