from flask import Flask,request,jsonify
app=Flask(__name__)
exchange_rates={
	"USD":1.00,
	"INR":87.20,
	"GBP":0.74,
	"EUR":0.86,
	"JPY":147.50,
	"CAD":1.37,
	"AED":3.67,
	"CNY":7.18,
	"SGD":1.28
}
@app.route("/convert")
def convert():
	from_currency=request.args.get("from").upper()
	to_currency=request.args.get("to").upper()
	amount=float(request.args.get("amount"))
	if from_currency not in exchange_rates or to_currency not in exchange_rates:
		return jsonify({"error":"Invalid Currency"}),400
	usd=amount/exchange_rates[from_currency]
	converte=usd*exchange_rates[to_currency]

	return jsonify({
		"from":from_currency,
		"to":to_currency,
		"amount":amount,
		"converte_amount":round(converte,2)
	})

if __name__=="__main__":
	app.run(debug=True)

