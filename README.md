# 📦 Supply Chain Demand Forecasting

Forecast future product demand using historical sales and external factors to optimize inventory, reduce stockouts, and improve operational planning.

![MLflow](https://img.shields.io/badge/MLflow-Enabled-blue)
![DVC](https://img.shields.io/badge/DVC-Tracked-brightgreen)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-orange)
![Python](https://img.shields.io/badge/Python-3.10+-blue)

---

## 🚀 Objective

Build an end-to-end time series forecasting system that:
- Ingests and preprocesses historical supply chain data
- Experiments with ARIMA, Prophet, and LSTM models
- Captures seasonality, trend, holidays, and volatility
- Provides forecasts via an interactive Streamlit frontend
- Tracks experiments using MLflow via DAGsHub
- Versions data, models, and pipelines using DVC

---

## 📊 Dataset

The dataset includes features such as:

- Product type, SKU, Price, Availability  
- Number of products sold, Revenue generated  
- Customer demographics, Stock levels, Lead times  
- Order quantities, Shipping info (times, carriers, costs)  
- Supplier info (name, location, lead time)  
- Production volumes, costs, inspection results  
- Transportation modes, routes, and costs

📁 Example file path: `Notebooks/supply_chain_dataset.csv`

---

## 🧠 Models Used

- [x] Prophet  
- [x] ARIMA (coming soon)  
- [ ] LSTM (coming soon)

### ✅ Evaluation Metrics
- RMSE, MAE, MAPE
- Residual diagnostics (ACF/PACF)
- Forecast plots with uncertainty intervals

---

## ⚙️ Tech Stack

| Layer         | Tools                            |
|---------------|----------------------------------|
| Language      | Python 3.10+                     |
| Backend       | Flask                            |
| Frontend      | Streamlit                        |
| Time-Series   | Prophet, ARIMA, LSTM             |
| Visualization | Plotly, Matplotlib               |
| Tracking      | MLflow + DAGsHub                 |
| Versioning    | Git + DVC                        |
| Deployment    | Docker                           |

---

## 📁 Project Structure

```bash
.
├── Notebooks/                   # Jupyter experiments
├── data/                        # Raw & processed data
├── src/                         # Pipeline code
├── app.py                       # Streamlit UI
├── Dockerfile                   # Container setup
├── requirements.txt             # Python packages
├── dvc.yaml                     # DVC pipeline config
├── mlruns/                      # MLflow tracking
└── README.md                    # This file
