""".. (IN PROGRESS)
"""

from shiny import ui

# from tools.help import portfolio_text


def model_ui():
    """Description :

    Initizalize the model inputs interface.

    Example :

    >>> .. (IN PROGRESS)
    """
    return (
        ui.tags.div(
            ui.input_slider("p", "Penalizer", 0, 1, 0.01),
            ui.input_action_button("bp", "Run the model", class_="all-button"),
        ),
    )


def output_model():
    """Description :

    Initizalize the model output interface.

    Example :

    >>> .. (IN PROGRESS)
    """
    return ui.output_text_verbatim("model_output")
