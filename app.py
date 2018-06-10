
from flask import Flask,render_template,request
import requests

api_key = "b5f16ff0404cba8c193ec81e93ffbab0"

url = "http://data.fixer.io/api/latest?access_key=" + api_key

app = Flask(__name__)
@app.route("/",methods= ["GET","POST"])
def index():
    if request.method == "POST":
        firstCurrency = request.form.get("firstCurrency") #USD
        secondCurrency = request.form.get("secondCurrency") #TRY

        amount = request.form.get("amount") #15
        response = requests.get(url)
        app.logger.info(response)

        infos = response.json()

        firstValue = infos["rates"][firstCurrency] #1.177027
        secondValue = infos["rates"][secondCurrency] #5.259542

        result = (secondValue / firstValue) * float(amount) #4.46849732

        currencyInfo = dict()
        currencyInfo["firstCurrency"] = firstCurrency
        currencyInfo["secondCurrency"] = secondCurrency
        currencyInfo["amount"] = amount
        currencyInfo["result"] = result

        return render_template("index.html",info= currencyInfo)

    else:
        return render_template("index.html")
if __name__ == "__main__":
    app.run(debug= True)
