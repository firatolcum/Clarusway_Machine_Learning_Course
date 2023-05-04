import pandas as pd
penguins = pd.read_csv("penguins_cleaned.csv")

# Ordinal Feature Encoding
df = penguins.copy()
target = "species"
encode = ["sex", "island"]

for col in encode:
    dummy = pd.get_dummies(df[col], prefix=col)
    df = pd.concat([df, dummy], axis=1)
    del df[col]

target_mapper = {"Adelie" : 0, "Chinstrap" : 1, "Gentoo" : 2}
def target_encode(val):
    return target_mapper[val]

df["species"] = df["species"].apply(target_encode)

# Seperating X and Y
X = df.drop("species", axis=1)
y = df["species"]

# Build Random Forest Model
from sklearn.ensemble import RandomForestClassifier
rf_model = RandomForestClassifier()
rf_model.fit(X, y)

# Saving the Model
import pickle
pickle.dump(rf_model, open("penguins_model.pkl", "wb"))