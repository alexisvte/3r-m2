""".. (IN PROGRESS)
"""

import random

import pandas as pd


def create_data(
    repartition: list[float] = [0.55, 0.29, 0.42, 0.48, 0.59, 0.33, 0.16, 0.29]
) -> pd.DataFrame:
    """Description :

    Create a simulated dataset based on a real dataset.

    PS: see the .RMD in the parent folder.

    Example :

    >>> .. (IN PROGRESS)
    """
    df = []

    true_indices = {}

    true_percentage = repartition

    num_rows, num_columns = (100, 8)

    for j, percentage in zip(range(num_columns), true_percentage):
        true_indices[j] = random.sample(range(num_rows), int(num_rows * percentage))

    for i in range(num_rows):
        row = []

        for j in range(num_columns):
            if i in true_indices[j]:
                value = 1
            else:
                value = 0

            row.append(value)

        df.append(row)

    return pd.DataFrame(
        df,
        columns=[
            "Contract_Month-to-month",
            "Dependents_Yes",
            "MultipleLines_Yes",
            "Partner_Yes",
            "PaperlessBilling_Yes",
            "PaymentMethod_Electronic check",
            "SeniorCitizen_Yes",
            "TechSupport_Yes",
        ],
    )
