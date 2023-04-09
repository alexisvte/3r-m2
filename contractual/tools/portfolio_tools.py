""".. (IN PROGRESS)
"""

import lifelines

from data.__init__ import survival_pd


def model(model_name: str = "Weibull", penalizer: float = 0.01):
    """Description :

    Run the model.

    Example :

    >>> .. (IN PROGRESS)
    """
    if model_name == "Weibull":
        aft = lifelines.WeibullAFTFitter(penalizer=penalizer)

    elif model_name == "Log-Normal":
        aft = lifelines.LogNormalAFTFitter(penalizer=penalizer)

    else:
        aft = lifelines.LogLogisticAFTFitter(penalizer=penalizer)

    return aft.fit(survival_pd, duration_col="tenure", event_col="Churn_bool")
