""".. (IN PROGRESS)
"""

from shiny.ui import modal_show, modal, modal_button, p
from htmltools import TagList, tags

about_text = TagList(
    tags.p(
        """
        This application gives a visual of the customer portfolio value over time."""
        + " The formula consists of the CLV minus the acquisition costs."
        + " The formula of Jain and Singh from 2002 (CLV_JS) does not depend on the portfolio survival function"
        + " (AFT model depending on customer's characteristics) unlike the formula of Gupta and Lehman from 2004 (CLV_GL).",
        style="""
        text-align: justify;
        word-break: break-word;
        hyphens: auto;
        """,
    ),
    tags.p(
        """
        However, the revenue function (linear regression model depending on customer's characteristics) of both formulas"""
        + "  are different from one customer to another where costs and acquisition costs are constant.",
        style="""
        text-align: justify;
        word-break: break-word;
        hyphens: auto;
        """,
    ),
)

dataset_information = TagList(
    tags.strong(tags.h3("Dataset Information")),
    tags.p(
        """
        The Telco dataset where each row represents a customer and each column contains customer's attributes."""
        + " One indicates the churn, another the tenure and the others the customer's characteristics"
        + " (personnal like gender, economical like revenue and technical like support).",
        style="""
        text-align: justify;
        word-break: break-word;
        hyphens: auto;
        """,
    ),
    tags.ul(
        tags.li(
            tags.a(
                "Dataset Telco Customer Churn",
                href=(
                    "https://www.kaggle.com/datasets/"
                    + "blastchar/telco-customer-churn"
                ),
            )
        ),
        tags.li(
            tags.a(
                "Another more complete dataset",
                href=(
                    "https://www.kaggle.com/datasets/yeanzc/"
                    + "telco-customer-churn-ibm-dataset"
                ),
            )
        ),
    ),
    tags.p(
        """
        We have simulated a dataset based on the Telco dataset to choose randomly"""
        + " which variable are TRUE or FALSE (1 or 0) for each customer.",
        style="""
        text-align: justify;
        word-break: break-word;
        hyphens: auto;
        """,
    ),
    tags.li(
        tags.a(
            "Contract_Month-to-month",
            style="""
            font-family: "Courier New";
            """,
        )
    ),
    tags.li(
        tags.a(
            "Dependents_Yes",
            style="""
            font-family: "Courier New";
            """,
        )
    ),
    tags.li(
        tags.a(
            "MultipleLines_Yes",
            style="""
            font-family: "Courier New";
            """,
        )
    ),
    tags.li(
        tags.a(
            "Partner_Yes",
            style="""
            font-family: "Courier New";
            """,
        )
    ),
    tags.li(
        tags.a(
            "PaperlessBilling_Yes",
            style="""
            font-family: "Courier New";
            """,
        )
    ),
    tags.li(
        tags.a(
            "PaymentMethod_Electronic check",
            style="""
            font-family: "Courier New";
            """,
        )
    ),
    tags.li(
        tags.a(
            "SeniorCitizen_Yes",
            style="""
            font-family: "Courier New";
            """,
        )
    ),
    tags.li(
        tags.a(
            "TechSupport_Yes",
            style="""
            font-family: "Courier New";
            """,
        )
    ),
    tags.br(),
)

missing_note = TagList(
    tags.p(
        tags.strong("Note: "),
        """
        selected characteristics above are variable on a simulated dataset based on the Telco dataset.""",
        style="""
        font-size: 14px;
        text-align: justify;
        word-break: break-word;
        hyphens: auto;
        """,
    ),
)


def info():
    """Description :

    Create the general information modal.

    Example :

    >>> .. (IN PROGRESS)
    """
    modal_show(
        modal(
            tags.strong(tags.h2("Portfolio Value App")),
            tags.strong(
                """
                How does the value of a customer portfolio evolve with customer's characteristics?""",
                style="""
                font-size: 16px;
                text-align: justify;
                word-break: break-word;
                hyphens: auto;
                """,
            ),
            tags.hr(),
            about_text,
            dataset_information,
            missing_note,
            size="l",
            easy_close=True,
            footer=modal_button("Close", id="close", class_="all-button"),
        )
    )


def info_model(model_name: str = "Weibull"):
    """Description :

    Create the model information modal.

    model_name: string,
        The model law name.

    Example :

    >>> .. (IN PROGRESS)
    """
    if model_name == "Weibull":
        url = tags.a(
            "Wikipedia/Weibull_distribution",
            href=("https://en.wikipedia.org/wiki/" + "Weibull_distribution"),
            style="""
            font-size: 10px;
            """,
        )

        name, text = (
            "Weibull distribution",
            """
            The Weibull distribution is a continuous probability distribution."""
            + " It is named after Swedish mathematician Waloddi Weibull, who described it in detail in 1951,"
            + " although it was first identified by Maurice René Fréchet and first applied by "
            + " Rosin & Rammler (1933) to describe a particle size distribution.",
        )

        images = "static/img/w.jpg"

    elif model_name == "Log-Normal":
        url = tags.a(
            "Wikipedia/Log-normal_distribution",
            href=("https://en.wikipedia.org/wiki/" + "Log-normal_distribution"),
            style="""
            font-size: 10px;
            """,
        )

        name, text = (
            "Log-Normal distribution",
            """
            In probability theory, a log-normal distribution is a continuous probability distribution"""
            + " of a random variable whose logarithm is normally distributed."
            + " A random variable which is log-normally distributed takes only positive real values."
            + " It is a convenient and useful model for measurements in exact and engineering sciences, as well as medicine,"
            + " economics and other topics.",
        )

        images = ""

    else:
        url = tags.a(
            "Wikipedia/Log-logistic_distribution",
            href=("https://en.wikipedia.org/wiki/" + "Log-logistic_distribution"),
            style="""
            font-size: 10px;
            """,
        )

        name, text = (
            "Log-Logistic distribution",
            """
            In probability and statistics, the log-logistic distribution (known as the Fisk distribution in economics)"""
            + " is a continuous probability distribution for a non-negative random variable."
            + " It is used in survival analysis as a parametric model for events whose rate increases initially and decreases later,"
            + " as, for example, mortality rate from cancer following diagnosis or treatment.",
        )

        images = "static/img/ll.jpg"

    modal_show(
        modal(
            tags.strong(tags.h3(name)),
            tags.br(),
            tags.p(
                text,
                style="""
                font-size: 14px;
                text-align: justify;
                word-break: break-word;
                hyphens: auto;
                """,
            ),
            tags.ul(url),
            tags.img(
                class_="fit-picture",
                src=images,
                alt="Survival and hazard functions",
            ),
            tags.br(),
            tags.strong(
                """
                AFTER CHOOSING A DISTRIBUTION, THE MODEL IS RUN ACCORDING TO THE SELECTED PENALIZER.""",
                style="""
                font-size: 12px;
                text-align: justify;
                word-break: break-word;
                hyphens: auto;
                """,
            ),
            size="l",
            easy_close=True,
            footer=modal_button("Close", id="close", class_="all-button"),
        )
    )
