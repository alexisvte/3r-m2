""".. (IN PROGRESS)
"""

from shiny import ui
from shinywidgets import output_widget

# from tools.help import slider_text_plot


def graphic_ui():
    """Description :

    Initizalize the figure inputs interface.

    Example :

    >>> .. (IN PROGRESS)
    """
    return ui.tags.div(
        ui.input_numeric(
            "o_0", "Constant acquisition cost", value=50.0, min=0.0, max=100.0
        ),
        ui.input_numeric("o_1", "Constant cost", value=25.0, min=0.0, max=100.0),
        ui.input_numeric("o_2", "Discount rate", value=13.0, min=1.0, max=100.0),
        ui.input_slider("df_0", f"Contract_Month-to-month", 0.01, 1, 0.55),
        ui.input_slider("df_1", f"Dependents_Yes", 0.01, 1, 0.29),
        ui.input_slider("df_2", f"MultipleLines_Yes", 0.01, 1, 0.42),
        ui.input_slider("df_3", f"Partner_Yes", 0.01, 1, 0.48),
        ui.input_slider("df_4", f"PaperlessBilling_Yes", 0.01, 1, 0.59),
        ui.input_slider("df_5", f"PaymentMethod_Electronic check", 0.01, 1, 0.33),
        ui.input_slider("df_6", f"SeniorCitizen_Yes", 0.01, 1, 0.16),
        ui.input_slider("df_7", f"TechSupport_Yes", 0.01, 1, 0.29),
        class_="card-style",
    )


def output_graphic():
    """Description :

    Initizalize the figure output interface.

    Example :

    >>> .. (IN PROGRESS)
    """
    return output_widget("fig_plot")
