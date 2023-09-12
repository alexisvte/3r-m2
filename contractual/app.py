""" app.py:

UI
Script to create the interface and import the data.

SERVER.
Script to import libraries and to call and run the interface and the server together.

WARNING: Can be commented and optimized!
"""

import pandas as pd

from pathlib import Path
from shiny import App, ui, render, reactive, Session
from shinywidgets import render_widget

from core import portfolio, graphic
from tools.help import info, info_model, about_text
from tools.graphic_tools import create_figure, create_table, data_portfolio
from tools.portfolio_tools import model

# data:
dfbis = pd.read_csv(Path(__file__).parent / "data" / "dfbis.csv")

# dependencies:
ui_dependencies = ui.tags.head(
    ui.tags.link(rel="stylesheet", type="text/css", href="layout.css"),
    ui.tags.link(rel="stylesheet", type="text/css", href="style.css"),
    ui.tags.script(src="index.js"),
    ui.tags.script(
        src="https://mathjax.rstudio.com/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"
    ),
    ui.tags.script("if (window.MathJax) MathJax.Hub.Queue(['Typeset', MathJax.Hub]);"),
    ui.tags.meta(name="description", content="Portfolio value app"),
    ui.tags.meta(name="theme-color", content="#000000"),
    ui.tags.meta(name="apple-mobile-web-app-status-bar-style", content="#000000"),
    ui.tags.meta(name="apple-mobile-web-app-capable", content="yes"),
    ui.tags.meta(name="viewport", content="width=device-width, initial-scale=1"),
)

# header :
page_header = ui.tags.div(
    ui.tags.div(
        ui.tags.a(
            ui.tags.img(src="static/img/mecen.jpg", height="50px"),
            href="https://fr.linkedin.com/company/master-mecen-universite-de-tours?"
            + "original_referer=https%3A%2F%2Fwww.google.com%2F",
        ),
        id="logo-top",
        class_="navigation-logo",
    ),
    ui.tags.div(
        ui.a("PORTFOLIO VALUE APP"),
        id="title-top",
        class_="navigation-title",
    ),
    ui.tags.div(
        ui.tags.div(
            ui.input_action_button(
                id="weibull_icon",
                label="Weibull",
                class_="navbar-button",
            ),
        ),
        ui.tags.div(
            ui.input_action_button(
                id="lnormale_icon",
                label="Log-Normal",
                class_="navbar-button",
            ),
        ),
        ui.tags.div(
            ui.input_action_button(
                id="llogistique_icon",
                label="Log-Logistic",
                class_="navbar-button",
            ),
        ),
        class_="navigation-menu",
    ),
    ui.tags.div(
        ui.input_action_button(
            id="info_icon",
            label=None,
            icon=ui.tags.i(class_="glyphicon glyphicon-info-sign"),
            class_="navbar-info",
        ),
        class_="navigation-info",
    ),
    id="div-navbar-info",
    class_="navbar-top page-header card-style",
)

# run the model and create the plot / table :
page_model = ui.tags.div(
    ui.tags.div(
        ui.output_text("law_output"),
        portfolio.model_ui(),
        ui.tags.br(),
        graphic.graphic_ui(),
        class_="main-sidebar",
    ),
    ui.tags.div(
        ui.tags.div(
            graphic.output_graphic(),
            portfolio.output_model(),
            class_="card-style",
        ),
        ui.tags.br(),
        ui.row(
            ui.column(
                3,
                ui.input_select(
                    id="tv",
                    label="Select variable:",
                    choices=list(dfbis.columns[1:]),
                    selected=list(dfbis.columns[1:])[0],
                    multiple=False,
                ),
                ui.input_action_button("vw", "View the table", class_="all-button"),
                ui.tags.br(),
                ui.tags.br(),
                ui.tags.br(),
                ui.tags.strong("All other things being equal."),
            ),
            ui.column(
                9,
                ui.tags.div(
                    ui.output_table("tab_view", class_="df_table"),
                    class_="table-container",
                ),
            ),
        ),
        # ui.tags.br(),
        # ui.tags.div(ui.output_table("table", class_="df_table_scroller")),
        class_="main-main",
    ),
    id="container-model",
    class_="main-subheader main-layout",
)

# app layout :
ui_layout = ui.tags.div(
    page_header,
    page_model,
    class_="page-layout",
)

# app :
app_ui = ui.page_fluid(
    ui_dependencies,
    ui_layout,
    title="Portfolio Value App",
)


def server(input, output, session: Session):
    """Description :

    Create the dialogue for the interaction.

    input:
        Several inputs created.
    output:
        Several outputs to create.

    Example :

    >>> .. (IN PROGRESS)
    """
    info()

    model_name = reactive.Value("Weibull")

    penalizer = reactive.Value(0.01)

    model_calculate = reactive.Value(model(model_name="Weibull", penalizer=0.01))

    # about the app :
    @reactive.Effect
    @reactive.event(input.info_icon)
    def _():
        info()

    # change the layout :
    @reactive.Effect
    @reactive.event(input.weibull_icon)
    def _():
        model_name.set("Weibull")

        info_model(model_name=model_name())

    @reactive.Effect
    @reactive.event(input.lnormale_icon)
    def _():
        model_name.set("Log-Normal")

        info_model(model_name=model_name())

    @reactive.Effect
    @reactive.event(input.llogistique_icon)
    def _():
        model_name.set("Log-Logistic")

        info_model(model_name=model_name())

    @reactive.Calc
    def law_print():
        return f"{model_name()} law is currently selected."

    @output
    @render.text
    def law_output():
        return law_print()

    # run the model :
    @reactive.Effect
    @reactive.event(input.bp)
    def _():
        penalizer.set(input.p())

    @reactive.Effect
    def _():
        model_calculate.set((model(model_name=model_name(), penalizer=penalizer())))

    @reactive.Calc
    def model_print():
        return f"""
        {model_name()} model concordance index and Akaike information criterion (AIC) are {round(model_calculate().concordance_index_, 2)} and {round(model_calculate().AIC_, 2)}.
        """

    @output
    @render.text
    def model_output():
        return model_print()

    # create the plot :
    @reactive.Calc
    def fig():
        result = data_portfolio(
            repartition=[
                input.df_0(),
                input.df_1(),
                input.df_2(),
                input.df_3(),
                input.df_4(),
                input.df_5(),
                input.df_6(),
                input.df_7(),
            ],
            other=[
                input.o_0(),
                input.o_1(),
                input.o_2(),
            ],
            model=model_calculate(),
        )

        return create_figure(
            X=result[0],
            Xbis=result[1],
            portfolio=result[2],
            portfoliobis=result[3],
            data=result[4],
        )

    @output(suspend_when_hidden=False)
    @render_widget
    def fig_plot():
        return fig()[0]

    # view the dataframe :
    # @output
    # @render.table
    # def table():
    #     return fig()[1]

    # create the table :
    @reactive.Calc
    @reactive.event(input.vw)
    def tab():
        return create_table(
            variable=input.tv(),
            other=[
                input.o_0(),
                input.o_1(),
                input.o_2(),
            ],
            model=model_calculate(),
        )

    @output
    @render.table
    def tab_view():
        return tab()


# run the app :
www_dir = Path(__file__).parent / "www"
app = App(app_ui, server, static_assets=www_dir)
