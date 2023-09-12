# .. (IN PROGRESS)

import pandas as pd

from pathlib import Path

data = Path(__file__).parent / "df.csv"

df = pd.read_csv(data, index_col=0)

for i in df.index:
    if df.loc[i, "tenure"] == 0:
        df.drop(i, inplace=True)

df = df.astype({"tenure": "float64"})

for i in df.index:
    if df.loc[i, "SeniorCitizen"] == 0:
        df.loc[i, "SeniorCitizen"] = "No"

    else:
        df.loc[i, "SeniorCitizen"] = "Yes"

unchange_cols = ["tenure", "Churn_bool"]

encode_cols = [
    "Contract",
    "MultipleLines",
    "TechSupport",
    "SeniorCitizen",
    "Partner",
    "Dependents",
    "PaperlessBilling",
    "PaymentMethod",
]

data = df[unchange_cols + encode_cols]

encoded_pd = pd.get_dummies(
    data, columns=encode_cols, prefix=encode_cols, drop_first=False
)

survival_pd = encoded_pd[
    [
        "Churn_bool",
        "tenure",
        "SeniorCitizen_Yes",
        "Partner_Yes",
        "Dependents_Yes",
        "PaperlessBilling_Yes",
        "PaymentMethod_Electronic check",
        "Contract_Month-to-month",
        "MultipleLines_Yes",
        "TechSupport_Yes",
    ]
]
