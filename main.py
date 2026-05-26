print("\n================================")
print("CROSS ASSET DEPENDENCY SYSTEM")
print("================================")

print("\nStarting Project Pipeline...\n")

# -----------------------------
# STEP 1 : DATA COLLECTION
# -----------------------------
print("STEP 1 : DATA COLLECTION\n")

exec(open(
    "src/data_collection.py"
).read())

# -----------------------------
# STEP 2 : PREPROCESSING
# -----------------------------
print("\nSTEP 2 : PREPROCESSING\n")

exec(open(
    "src/preprocessing.py"
).read())

# -----------------------------
# STEP 3 : FEATURE ENGINEERING
# -----------------------------
print("\nSTEP 3 : FEATURE ENGINEERING\n")

exec(open(
    "src/feature_engineering.py"
).read())

# -----------------------------
# STEP 4 : DEPENDENCY ANALYSIS
# -----------------------------
print("\nSTEP 4 : DEPENDENCY ANALYSIS\n")

exec(open(
    "src/dependency_analysis.py"
).read())

# -----------------------------
# STEP 5 : MODEL TRAINING
# -----------------------------
print("\nSTEP 5 : MODEL TRAINING\n")

exec(open(
    "src/model_training.py"
).read())

# -----------------------------
# STEP 6 : EVALUATION
# -----------------------------
print("\nSTEP 6 : EVALUATION\n")

exec(open(
    "src/evaluation.py"
).read())

# -----------------------------
# STEP 7 : ASSET RANKING
# -----------------------------
print("\nSTEP 7 : ASSET RANKING\n")

exec(open(
    "src/ranking.py"
).read())

# -----------------------------
# FINAL MESSAGE
# -----------------------------
print("\n================================")
print("PROJECT COMPLETED SUCCESSFULLY")
print("================================")

print("\nGenerated Outputs:")

print("1. stocks.csv")
print("2. returns.csv")
print("3. features.csv")
print("4. dependency_scores.csv")
print("5. stock_model.pkl")
print("6. evaluation.txt")
print("7. rankings.csv")
print("8. heatmap.png")
