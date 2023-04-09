""".. (IN PROGRESS)
"""
import joblib

import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd

from pathlib import Path
from shiny import ui

from data.__init__ import df
from data.data import create_data

loaded_model = joblib.load(Path(__file__).parent / "saved_model.sav")


def data_portfolio(
    model,
    repartition: list[float] = [0.55, 0.29, 0.42, 0.48, 0.59, 0.33, 0.16, 0.29],
    other: list[float] = [
        50.0,
        25.0,
        0.13,
    ],
):
    """Description :

    Initialize the portfolio value and create the figure.

    Example :

    >>> .. (IN PROGRESS)
    """
    data = create_data(repartition=repartition)

    data.insert(0, "revenue", loaded_model.predict(data.values))

    survival = model.predict_survival_function(
        data[data.columns.difference(["tenure", "Churn_bool"])]
    )

    portfolio, portfoliobis = {}, {}

    for j in survival.index:
        portfolio_time, portfoliobis_time = [], []

        for i in data.index:
            portfolio_time.append(
                (data.loc[i, "revenue"] - other[1])
                * survival.loc[j, i]  # other[0]
                / (1 + (other[2] / 100)) ** j
            )  # GL,

            portfoliobis_time.append(
                (data.loc[i, "revenue"] - other[1])
                / (1 + (other[2] / 100)) ** j  # other[0]
            )  # JS,

        portfolio[j], portfoliobis[j] = (portfolio_time, portfoliobis_time)

    for i, ibis in zip(portfolio.keys(), portfoliobis.keys()):
        # portfolio[i], portfoliobis[ibis] = (
        #     np.sum(portfolio[i]),
        #     np.sum(portfoliobis[ibis])
        # )
        if i == 1:
            portfolio[i], portfoliobis[ibis] = (
                np.sum(portfolio[i]) - (other[0] * 100),
                np.sum(portfoliobis[ibis]) - (other[0] * 100),
            )

        else:
            portfolio[i], portfoliobis[ibis] = (
                np.sum(portfolio[i]) + portfolio[i - 1],
                np.sum(portfoliobis[ibis]) + portfoliobis[ibis - 1],
            )

    X, Xbis = (
        [int(x) for x in list(portfolio.keys())],
        [int(x) for x in list(portfoliobis.keys())],
    )

    return (
        X,
        Xbis,
        portfolio,
        portfoliobis,
        data,
    )


def create_figure(
    X: list[int],
    Xbis: list[int],
    portfolio: dict[int:float],
    portfoliobis: dict[int:float],
    data: pd.DataFrame,
):
    """Description :

    Initialize the portfolio value and create the figure.

    Example :

    >>> .. (IN PROGRESS)
    """
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=Xbis,
            y=list(portfoliobis.values()),
            mode="lines",
            line=dict(width=2, color="#344A58", dash="dash"),
            name="CLV_JS",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=X,
            y=list(portfolio.values()),
            mode="lines",
            line=dict(width=2, color="#238694"),
            name="CLV_GL",
        )
    )

    fig.update_traces(
        mode="lines",
        hovertemplate=None,
        line=dict(width=5),
        marker=dict(size=15),
    )

    fig.update_layout(template="presentation", hovermode="x", height=550)

    return (go.FigureWidget(fig), data)


def create_table(model, other: list[float], variable: str):
    """Description :

    Initialize the portfolio value and create the figure.

    Example :

    >>> .. (IN PROGRESS)
    """
    test = [0.01, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

    variables = {
        "Contract_Month-to-month": 0.55,
        "Dependents_Yes": 0.29,
        "MultipleLines_Yes": 0.42,
        "Partner_Yes": 0.48,
        "PaperlessBilling_Yes": 0.59,
        "PaymentMethod_Electronic check": 0.33,
        "SeniorCitizen_Yes": 0.16,
        "TechSupport_Yes": 0.29,
    }

    table = []

    with ui.Progress(min=1, max=len(test)) as p:
        p.set(message="Calculation in progress")

        for i, j in zip(test, range(len(test))):
            p.set(j, message="Computing")

            result = {}

            variables[variable] = i

            result[variable + " - proportion"] = i

            CLV_GL, CLV_JS = (
                round(
                    data_portfolio(
                        model=model, repartition=list(variables.values()), other=other
                    )[2][72],
                    2,
                ),
                round(
                    data_portfolio(
                        model=model, repartition=list(variables.values()), other=other
                    )[3][72],
                    2,
                ),
            )

            result["CLV_GL"], result["CLV_JS"], result["\u0394"], result[" "] = (
                CLV_GL,
                CLV_JS,
                round(CLV_JS - CLV_GL, 2),
                round(((CLV_JS - CLV_GL) / CLV_JS) * 100, 2),
            )

            table.append(result)

    return pd.DataFrame(table)
