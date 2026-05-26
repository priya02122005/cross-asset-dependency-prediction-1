from flask import Flask, render_template, request

import pandas as pd

from sklearn.ensemble import RandomForestRegressor

from sklearn.model_selection import train_test_split

app = Flask(__name__)

# HOME PAGE

@app.route("/")
def home():

    return render_template(
        "index.html"
    )


# ABOUT PAGE

@app.route("/about")
def about():

    return render_template(
        "about.html"
    )


# PREDICTION PAGE

@app.route(
    "/predict",
    methods=["GET", "POST"]
)
def predict():

    prediction = None

    signal = None

    confidence = None

    if request.method == "POST":

        stock = request.form["stock"].upper()

        # LOAD FEATURES

        df = pd.read_csv(
            "data/features.csv",
            index_col=0
        )

        # CHECK STOCK EXISTS

        if stock in df.columns:

            # TARGET

            df["target"] = (
                df[stock].shift(-1)
            )

            df.dropna(inplace=True)

            # FEATURES

            X = df.drop(
                columns=["target"]
            )

            y = df["target"]

            # TRAIN TEST SPLIT

            X_train, X_test, y_train, y_test = train_test_split(
                X,
                y,
                test_size=0.2,
                random_state=42
            )

            # FAST MODEL

            model = RandomForestRegressor(
                n_estimators=20,
                random_state=42
            )

            model.fit(
                X_train,
                y_train
            )

            # PREDICTION

            prediction = model.predict(
                X.tail(1)
            )[0]

            prediction = round(
                prediction,
                5
            )

            # SIGNAL

            if prediction > 0:

                signal = "BUY 📈"

            else:

                signal = "SELL 📉"

            # CONFIDENCE

            confidence = round(
                abs(prediction) * 100,
                2
            )

    return render_template(
        "predict.html",
        prediction=prediction,
        signal=signal,
        confidence=confidence
    )


# RESULTS PAGE

@app.route("/results")
def results():

    df = pd.read_csv(
        "data/returns.csv",
        index_col=0
    )

    latest_returns = df.iloc[-1]

    ranked = latest_returns.sort_values(
        ascending=False
    )

    outperformers = ranked.head(3)

    underperformers = ranked.tail(3)

    return render_template(
        "results.html",
        outperformers=outperformers,
        underperformers=underperformers
    )


# RUN APP

if __name__ == "__main__":

    app.run(debug=True)
