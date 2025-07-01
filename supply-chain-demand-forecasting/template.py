# template.py

from flask import Flask, request, jsonify
import pandas as pd
import io
from prophet import Prophet

app = Flask(__name__)

@app.route("/forecast/prophet", methods=["POST"])
def forecast_prophet():
    file = request.files['file']
    sku = request.args.get("sku")
    period = int(request.args.get("period", 12))

    df = pd.read_csv(io.BytesIO(file.read()))
    df = df[df['SKU'] == sku][['date', 'Number of products sold']]
    df.columns = ['ds', 'y']
    df['ds'] = pd.to_datetime(df['ds'])

    model = Prophet()
    model.fit(df)

    future = model.make_future_dataframe(periods=period, freq='W')
    forecast = model.predict(future)

    result = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].rename(columns={"ds": "date"})
    return jsonify({"forecast": result.to_dict(orient='records')})

if __name__ == "__main__":
    app.run(debug=True)
