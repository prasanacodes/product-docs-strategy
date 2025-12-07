# Email: 22f1001255@ds.study.iitm.ac.in

import marimo as mo

app = mo.App()


@app.cell
def __():
    # This cell imports marimo and exposes `mo` to later cells.
    # Data flow: None -> mo (used by later cells for UI + markdown)
    return mo


@app.cell
def __(mo):
    # This cell creates an interactive slider widget.
    # Data flow: mo -> number_slider (widget used in the next cells)
    number_slider = mo.ui.slider(
        start=0,
        stop=100,
        step=5,
        value=25,
        label="Select a number",
    )

    # Display the slider in the UI
    number_slider

    # Expose the widget so other cells can depend on its state
    return number_slider


@app.cell
def __(number_slider):
    # This cell depends on `number_slider` from the previous cell.
    # It reads the current slider value and computes a derived variable.
    # Data flow: number_slider -> selected_value, squared_value
    selected_value = number_slider.value
    squared_value = selected_value**2

    # Optionally show computed values (useful when inspecting)
    selected_value, squared_value

    return selected_value, squared_value


@app.cell
def __(mo, selected_value, squared_value):
    # This cell produces dynamic markdown based on widget state and
    # the derived computations.
    #
    # Data flow:
    #   selected_value, squared_value -> dynamic_markdown
    # The markdown updates automatically whenever the slider moves.
    dynamic_markdown = mo.md(
        f"""
# Interactive Slider Summary

- You selected: **{selected_value}**
- Its square is: **{squared_value}**

Try moving the slider above and watch this text update in real time.
"""
    )

    dynamic_markdown

    return dynamic_markdown


if __name__ == "__main__":
    app.run()
