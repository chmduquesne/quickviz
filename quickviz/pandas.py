import ipywidgets as widgets

def gen_widgets(df):
    """
    Returns a dictionary of dictionaries

    The dictionary '*' contains all the widgets. The keys don't matter in
    the UI.

    All other dictionaries are named after the plot they represent. They
    map their arguments to widgets defined in '*'.
    """
    w = {
        "C": widgets.Dropdown(options=list(df)),
        "bins": widgets.IntText(value=10),
        "bw_method": widgets.Dropdown(options=["scott", "silverman"]),
        "by": widgets.Dropdown(options=list(df)),
        "c": widgets.Dropdown(options=list(df)),
        "colormap": widgets.Text(),
        "column": widgets.SelectMultiple(options=list(df)),
        "fontsize": widgets.IntSlider(min=2, max=40),
        "grid": widgets.Checkbox(),
        "gridsize": widgets.IntText(value=100),
        "ind": widgets.IntText(value=1000),
        "legend": widgets.Checkbox(),
        "logx": widgets.Checkbox(),
        "logy": widgets.Checkbox(),
        "mark_right": widgets.Checkbox(),
        "position": widgets.FloatSlider(min=0.0, max=1.0, step=0.05),
        "s": widgets.Dropdown(options=dict([(col, list(df[col])) for col in list(df)])),
        "sharex": widgets.Checkbox(),
        "sharey": widgets.Checkbox(),
        "sort_columns": widgets.Checkbox(),
        "stacked": widgets.Checkbox(),
        "subplots": widgets.Checkbox(),
        "title": widgets.Text(),
        "use_index": widgets.Checkbox(),
        "x": widgets.Dropdown(options=list(df)),
        "xerr": widgets.Dropdown(options=dict([(col, list(df[col])) for col in list(df)])),
        "y": widgets.Dropdown(options=list(df)),
        "yerr": widgets.Dropdown(options=dict([(col, list(df[col])) for col in list(df)])),
    }
    generic_args = {
            k:w[k] for k in [ "x", "y", "subplots", "sharex", "sharey",
                "use_index", "title", "grid", "legend", "logx", "logy",
                "fontsize", "colormap", "position", "xerr", "yerr",
                "stacked", "sort_columns", "mark_right", ]
    }
    res = {
        "*": w,
        "area": {},
        "bar": {},
        "barh": {},
        "box": {
            "by": w["by"],
        },
        "density": {
            "bw_method": w["bw_method"],
            "ind": w["ind"],
        },
        "hexbin": {
            "C": w["C"],
            "gridsize": w["gridsize"],
        },
        "hist": {
            "by": w["by"],
            "bins": w["bins"],
        },
        "kde": {
            "bw_method": w["bw_method"],
            "ind": w["ind"],
        },
        "line": {},
        "pie": {},
        "scatter": {
            "s": w["s"],
            "c": w["c"],
        },
        "boxplot": {
            "by": w["by"],
        },
        "hist": {
            "by": w["by"],
            "bins": w["bins"],
            "column": w["column"],
        }
    }
    for plot_type in res:
        res[plot_type].update(**generic_args)
    return res


def plot(df, plot_type, kwargs):
    method = getattr(df.plot, plot_type)
    return method(**kwargs)
