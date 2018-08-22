import ipywidgets as widgets

def arg_widgets(df):
    return {
        "*": {
            "x": widgets.Dropdown(options=list(df)),
            "y": widgets.Dropdown(options=list(df)),
            "subplots": widgets.Checkbox(),
            "sharex": widgets.Checkbox(),
            "sharey": widgets.Checkbox(),
            "use_index": widgets.Checkbox(),
            "title": widgets.Text(),
            "grid": widgets.Checkbox(),
            "legend": widgets.Checkbox(),
            "logx": widgets.Checkbox(),
            "logy": widgets.Checkbox(),
            "fontsize": widgets.IntSlider(min=2, max=40),
            "colormap": widgets.Text(),
            "position": widgets.FloatSlider(min=0.0, max=1.0, step=0.05),
            "xerr": widgets.Dropdown(options=dict([(col, list(df[col])) for col in list(df)])),
            "yerr": widgets.Dropdown(options=dict([(col, list(df[col])) for col in list(df)])),
            "stacked": widgets.Checkbox(),
            "sort_columns": widgets.Checkbox(),
            "mark_right": widgets.Checkbox(),
        },
        "area": {},
        "bar": {},
        "barh": {},
        "box": {
            "by": widgets.Dropdown(options=list(df)),
        },
        "density": {
            "bw_method": widgets.Dropdown(options=["scott", "silverman"]),
            "ind": widgets.IntText(value=1000),
        },
        "hexbin": {
            "C": widgets.Dropdown(options=list(df)),
            "gridsize": widgets.IntText(value=100),
        },
        "hist": {
            "by": widgets.Dropdown(options=list(df)),
            "bins": widgets.IntText(value=10),
        },
        "kde": {
            "bw_method": widgets.Dropdown(options=["scott", "silverman"]),
            "ind": widgets.IntText(value=1000),
        },
        "line": {},
        "pie": {},
        "scatter": {
            "s": widgets.Dropdown(options=dict([(col, list(df[col])) for col in list(df)])),
            "c": widgets.Dropdown(options=list(df)),
        },
        "boxplot": {
            "by": widgets.Dropdown(options=list(df)),
        },
        "hist": {
            "by": widgets.Dropdown(options=list(df)),
            "bins": widgets.IntText(value=10),
            "column": widgets.SelectMultiple(options=list(df)),
        }
    }


def plot(df, plot_type, kwargs):
    method = getattr(df.plot, plot_type)
    method(**kwargs)
