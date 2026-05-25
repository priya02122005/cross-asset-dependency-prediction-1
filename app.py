from flask import Flask, render_template
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# About Page
@app.route("/about")
def about():
    return render_template("about.html")


# Prediction Page
@app.route("/predict")
def predict():

    # Load features
    df = pd.read_csv(
        "data/features.csv",
        index_col=0
    )

    # Create target
    df["target"] = df["AAPL"].shift(-1)

    df.dropna(inplace=True)

    # Features and target
    X = df.drop(columns=["target"])
    y = df["target"]

    # Train model
    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    model.fit(X, y)

    # Predict next return
    prediction = model.predict(
        X.tail(1)
    )[0]

    return render_template(
        "predict.html",
        prediction=round(prediction, 5)
    )


# Results Page
@app.route("/results")
def results():

    # Load returns
    df = pd.read_csv(
        "data/returns.csv",
        index_col=0
    )

    # Latest returns
    latest_returns = df.iloc[-1]

    # Rank stocks
    ranked = latest_returns.sort_values(
        ascending=False
    )

    outperformers = ranked.head()

    underperformers = ranked.tail()

    return render_template(
        "results.html",
        outperformers=outperformers,
        underperformers=underperformers
    )


if __name__ == "__main__":
    app.run(debug=True)