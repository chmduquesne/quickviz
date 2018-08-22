import matplotlib
import pandas as pd
import seaborn
from IPython.display import display, clear_output
import ipywidgets as widgets
from ipywidgets.widgets.interaction import show_inline_matplotlib_plots


def pandas_arg_widgets(df):
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


def pandas_plot(df, plot_type, kwargs):
    method = getattr(df.plot, plot_type)
    method(**kwargs)


def seaborn_arg_widgets(df):
    relplot = {
            "x": widgets.Dropdown(options=list(df)),
            "y": widgets.Dropdown(options=list(df)),
            "hue": widgets.Dropdown(options=list(df)),
            "size": widgets.Dropdown(options=list(df)),
            "style": widgets.Dropdown(options=list(df)),
            "row": widgets.Dropdown(options=list(df)),
            "col": widgets.Dropdown(options=list(df)),
            "col_wrap": widgets.IntText(value=10),
            #"row_order":
            #"col_order":
            "palette": widgets.Text(),
            #"hue_order":
            #"hue_norm":
            "sizes": widgets.Dropdown(options=dict([(col, list(df[col])) for col in list(df)])),
            #"size_order":
            #"size_norm":
            "legend": widgets.Dropdown(options={"brief": "brief", "full":"full", "False": False}),
            "kind": widgets.Dropdown(options=["scatter", "line"]),
            #"height":
            #"aspect":
        }
    scatterplot = {
            "x": relplot["x"],
            "y": relplot["y"],
            "hue": relplot["hue"],
            "size": relplot["size"],
            "style": relplot["style"],
            "palette": relplot["palette"],
            #"hue_order":
            #"hue_norm":
            "sizes": relplot["sizes"],
            #"size_order":
            #"size_norm":
            "markers": widgets.Dropdown(options=dict([(col, list(df[col])) for col in list(df)])),
            #"style_order":
            #"{x,y}_bins": (non functional)
            #"units": (non functional)
            #"estimator": (non functional)
            #"ci": (non functional)
            #"n_boot": (non functional)
            "alpha": widgets.FloatSlider(min=0.0, max=1.0, step=0.05),
            #"{x,y}_jitter": (non functional)
            "legend": relplot["legend"],
        }
    lineplot = {
            "x": relplot["x"],
            "y": relplot["y"],
            "hue": relplot["hue"],
            "size": relplot["size"],
            "style": relplot["style"],
            "palette": relplot["palette"],
            #"hue_order":
            #"hue_norm":
            "sizes": relplot["sizes"],
            "dashes": widgets.Dropdown(options=dict([(col, list(df[col])) for col in list(df)])),
            "markers": scatterplot["markers"],
            #"style_order":
            #"units": (non functional)
            #"estimator"
            #"ci"
            "n_boot": widgets.IntText(value=10000),
            "sort": widgets.Checkbox(),
            "err_style": widgets.Dropdown(options=["band", "bars"]),
            "legend": relplot["legend"],
        }
    catplot = {
            "x": relplot["x"],
            "y": relplot["y"],
            "row": relplot["row"],
            "col": relplot["col"],
            "col_wrap": relplot["col_wrap"],
            #"estimator"
            #"ci"
            "n_boot": lineplot["n_boot"],
            #"units"
            #"order","hue_order"
            #"row_order","col_order"
            "kind": widgets.Dropdown(options=["point", "bar", "strip", "swarm", "box", "violin", "boxen"]),
            #"height"
            #"aspect"
            "orient": widgets.Dropdown(options=["v", "h"]),
            #"color"
            "palette": relplot["palette"],
            "legend": relplot["legend"],
            "legend_out": widgets.Checkbox(),
            "sharex": widgets.Dropdown(options={"True": True, "col": "col", "row": "row"}),
            "sharey": widgets.Dropdown(options={"True": True, "col": "col", "row": "row"}),
            "margin_titles": widgets.Checkbox(),
        }
    stripplot = {
            "x": relplot["x"],
            "y": relplot["y"],
            #"order","hue_order"
            "jitter": widgets.Checkbox(),
            #"dodge"
            "orient": catplot["orient"],
            #"color"
            "palette": relplot["palette"],
            "size": widgets.FloatText(value=1.0),
            #"edgecolor"
            "linewidth": widgets.FloatText(value=1.0),
        }
    swarmplot = {
            "x": relplot["x"],
            "y": relplot["y"],
            #"order","hue_order"
            #"dodge"
            "orient": catplot["orient"],
            #"color"
            "palette": relplot["palette"],
            "size": stripplot["size"],
            #"edgecolor"
            "linewidth": stripplot["linewidth"],
        }
    boxplot = {
            "x": relplot["x"],
            "y": relplot["y"],
            #"order","hue_order"
            "orient": catplot["orient"],
            #"color"
            "palette": relplot["palette"],
            "saturation": widgets.FloatText(value=1.0),
            "width": widgets.FloatText(value=1.0),
            #"dodge"
            "fliersize": widgets.FloatText(value=1.0),
            "linewidth": stripplot["linewidth"],
            "whis":  widgets.FloatText(value=1.0),
            "notch": widgets.Checkbox(),
        }
    violinplot = {
            "x": relplot["x"],
            "y": relplot["y"],
            "hue": relplot["hue"],
            #"order","hue_order"
            "bw": widgets.Dropdown(options=["scott", "silverman"]),
            "cut": widgets.FloatText(value=1.0),
            "scale": widgets.Dropdown(options=["area", "count", "width"]),
            "scale_hue": widgets.Checkbox(),
            "gridsize": widgets.IntText(value=100),
            "width": boxplot["width"],
            "inner": widgets.Dropdown(options=["box", "quartile", "point", "stick"]),
            "split": widgets.Checkbox(),
            #"dodge"
            "orient": catplot["orient"],
            "linewidth": stripplot["linewidth"],
            #"color"
            "palette": relplot["palette"],
            "saturation": boxplot["saturation"],
        }
    boxenplot = {
            "x": relplot["x"],
            "y": relplot["y"],
            "hue": relplot["hue"],
            #"order","hue_order"
            "orient": catplot["orient"],
            #"color"
            "palette": relplot["palette"],
            "saturation": boxplot["saturation"],
            "width": boxplot["width"],
            #"dodge"
            "k_depth": widgets.Dropdown(options=["proportion", "tukey", "trustworthy"]),
            "linewidth": stripplot["linewidth"],
            "scale":  widgets.Dropdown(options=["linear", "exponential", "area"]),
            "outlier_prop": widgets.FloatSlider(min=0.0, max=1.0, step=0.001, value=0.007),
        }
    pointplot = {
            "x": relplot["x"],
            "y": relplot["y"],
            "hue": relplot["hue"],
            #"order","hue_order"
            #"estimator"
            #"ci"
            "n_boot": lineplot["n_boot"],
            #"units"
            "markers": scatterplot["markers"],
            #linestyles
            #"dodge"
            "join": widgets.Checkbox(),
            "scale": widgets.FloatText(value=1.0),
            "orient": catplot["orient"],
            #"color"
            "palette": relplot["palette"],
            "errwidth": widgets.FloatText(value=1.0),
            "capsize": widgets.FloatText(value=1.0),
        }
    barplot = {
            "x": relplot["x"],
            "y": relplot["y"],
            "hue": relplot["hue"],
            #"order","hue_order"
            #"estimator"
            #"ci"
            "n_boot": lineplot["n_boot"],
            #"units"
            "orient": catplot["orient"],
            #"color"
            "palette": relplot["palette"],
            "saturation": boxplot["saturation"],
            #"errcolor"
            "errwidth": pointplot["errwidth"],
            "capsize": pointplot["capsize"],
            #"dodge"
        }
    countplot = {
            "x": relplot["x"],
            "y": relplot["y"],
            "hue": relplot["hue"],
            #"order","hue_order"
            "orient": catplot["orient"],
            #"color"
            "palette": relplot["palette"],
            "saturation": boxplot["saturation"],
            #"dodge"
        }
    jointplot = {
            "x": relplot["x"],
            "y": relplot["y"],
            "kind": widgets.Dropdown(options=["scatter", "reg", "resid", "kde", "hex"]),
            #stat_func
            #color
            "height": widgets.IntText(value=5),
            "ratio": widgets.IntText(value=1),
            "space": widgets.IntText(value=1),
            "dropna": widgets.Checkbox(),
            #"xlim"
            #"ylim"
        }
    pairplot = {
            "hue": relplot["hue"],
            #hue_order
            "palette": relplot["palette"],
            #vars
            #x_vars
            #y_vars
            "kind": widgets.Dropdown(options=["scatter", "reg"]),
            "diag_kind": widgets.Dropdown(options=["auto", "hist", "kde"]),
            "markers": scatterplot["markers"],
            "height": widgets.FloatText(value=1.0),
            "aspect": widgets.FloatText(value=1.0),
            "dropna": jointplot["dropna"],
        }
    distplot = {
            "a": widgets.Dropdown(options=[(col, list(df[col])) for col in list(df)]),
            #"bins"
            "hist": widgets.Checkbox(),
            "kde": widgets.Checkbox(),
            "rug": widgets.Checkbox(),
            #"fit"
            #{hist, kde, rug, fit}_kws
            #"color"
            "vertical": widgets.Checkbox(),
            "norm_hist": widgets.Checkbox(),
            "axlabel": widgets.Text(),
            "label": widgets.Text(),
        }
    kdeplot = {
            "data": widgets.Dropdown(options=[(col, list(df[col])) for col in list(df)]),
            "data2": widgets.Dropdown(options=[(col, list(df[col])) for col in list(df)]),
            "shade": widgets.Checkbox(),
            "vertical": distplot["vertical"],
            "kernel": widgets.Dropdown(options=['gau', 'cos', 'biw', 'epa', 'tri', 'triw']),
            "bw": violinplot["bw"],
            "gridsize": violinplot["gridsize"],
            "cut": violinplot["cut"],
            #"clip":
            "legend": relplot["legend"],
            "cumulative": widgets.Checkbox(),
            "shade_lowest": widgets.Checkbox(),
            "cbar": widgets.Checkbox(),
            "cbar_ax": widgets.Checkbox(),
        }
    lmplot = {
            "x": relplot["x"],
            "y": relplot["y"],
            "hue": relplot["hue"],
            "col": relplot["col"],
            "row": relplot["row"],
            "palette": relplot["palette"],
            "col_wrap": relplot["col_wrap"],
            "height": widgets.FloatText(value=1.0),
            "aspect": widgets.FloatText(value=1.0),
            "markers": scatterplot["markers"],
            "sharex": widgets.Dropdown(options={"True": True, "col": "col", "row": "row"}),
            "sharey": widgets.Dropdown(options={"True": True, "col": "col", "row": "row"}),
            "legend": relplot["legend"],
            "legend_out": widgets.Checkbox(),
            #x_estimator
            "x_bins": widgets.IntText(value=10),
            "x_ci": widgets.IntSlider(min=0, max=100, value=95),
            "scatter": widgets.Checkbox(),
            "fit_reg": widgets.Checkbox(),
            "ci": widgets.IntSlider(min=0, max=100, value=95),
            "n_boot": lineplot["n_boot"],
            #units
            "order": widgets.IntText(value=1),
            "logistic": widgets.Checkbox(),
            "lowess": widgets.Checkbox(),
            "robust": widgets.Checkbox(),
            "logx": widgets.Checkbox(),
            "x_partial": widgets.Dropdown(options=list(df)),
            "y_partial": widgets.Dropdown(options=list(df)),
            "truncate": widgets.Checkbox(),
            "x_jitter": widgets.FloatText(value=1.0),
            "y_jitter": widgets.FloatText(value=1.0),
        }
    return {
        "*": {},
        "relplot": relplot,
        "scatterplot": scatterplot,
        "lineplot": lineplot,
        "catplot": catplot,
        "stripplot": stripplot,
        "swarmplot": swarmplot,
        "boxplot": boxplot,
        "violinplot": violinplot,
        "boxenplot": boxenplot,
        "pointplot": pointplot,
        "barplot": barplot,
        "countplot": countplot,
        "jointplot": jointplot,
        "pairplot": pairplot,
        "distplot": distplot,
        "kdeplot": kdeplot,
        #rugplot -> not interesting
        "lmplot": lmplot,
    }


def seaborn_plot(df, plot_type, kwargs):
    method = getattr(seaborn, plot_type)
    if plot_type not in ["distplot", "kdeplot"]:
        kwargs["data"]=df
    method(**kwargs)


class UI(object):
    def __init__(self, df, generate_widgets, plot_function):
        self.df = df
        self.arg_widgets = generate_widgets(df)
        self.plot_function = plot_function
        self.connected_args = []
        self.connect_widgets()

        self.plot_type_chooser = widgets.Dropdown(options=self.get_plot_types(), description="Plot")
        self.plot_type_chooser.observe(self.redraw, 'value')

        self.add_arg_box = widgets.HBox()
        self.arg_chooser = widgets.Dropdown(description="Controls")
        self.add_arg_box.children = [self.arg_chooser]

        self.vbox = widgets.VBox()
        self.output = widgets.Output()

        display(self.vbox, self.output)
        self.redraw()

    def connect_widgets(self):
        for widget_dict in self.arg_widgets.values():
            for a, w in widget_dict.items():
                w.description = a
                w.observe(self.plot, 'value')

    def get_plot_types(self):
        return sorted([name for name in list(self.arg_widgets.keys()) if name != '*'])

    def get_accepted_args(self):
        args  = [(a, a) for a in sorted(self.arg_widgets["*"].keys())]
        p = self.plot_type_chooser.value
        args += [('[%s] %s' % (p, a), a) for a in
                sorted(self.arg_widgets[p].keys())]
        # place the most useful arguments on top
        top = [('x', 'x'), ('y', 'y')]
        for t in reversed(top):
            if t in args:
                args.remove(t)
                args = [t] + args
        return args

    def add_arg(self, *_):
        if self.arg_chooser.value not in self.connected_args:
            self.connected_args.append(self.arg_chooser.value)
            self.redraw()

    def get_widget(self, arg):
        if arg in self.arg_widgets["*"]:
            return self.arg_widgets["*"][arg]
        else:
            return self.arg_widgets[self.plot_type_chooser.value][arg]

    def arg_controller(self, arg):
        w = self.get_widget(arg)
        r = widgets.Button(description='remove')
        h = widgets.HBox(children=[w, r])
        def remove(*_):
            for c in h.children:
                if c != w:
                    c.close()
            h.close()
            self.connected_args.remove(arg)
            self.redraw()
        r.on_click(remove)
        return h

    def filter_connected_args(self):
        self.connected_args = [
            a for a in self.connected_args[:]
            if a in dict(self.get_accepted_args()).values()
        ]

    def redraw(self, *_):
        self.filter_connected_args()

        lines = []
        lines.append(self.add_arg_box)
        lines.append(widgets.HBox([widgets.Label(value="---")]))
        for arg in self.connected_args:
            lines.append(self.arg_controller(arg))
        lines.append(self.plot_type_chooser)
        self.vbox.children = lines

        arg_choice = self.arg_chooser.value
        try:
            self.arg_chooser.unobserve(self.add_arg, 'value')
        except ValueError:
            pass
        self.arg_chooser.options = self.get_accepted_args()
        if arg_choice in dict(self.get_accepted_args()).values():
            self.arg_chooser.value = arg_choice
        self.arg_chooser.observe(self.add_arg, 'value')
        self.plot()


    def plot(self, *_):
        kwargs = {
            arg:self.get_widget(arg).value for arg in self.connected_args
        }
        show_inline_matplotlib_plots()
        with self.output:
            clear_output(wait=True)
            self.plot_function(
                    self.df,
                    self.plot_type_chooser.value,
                    kwargs)
            show_inline_matplotlib_plots()


def visualize_pandas(df):
    return UI(
            df,
            generate_widgets=pandas_arg_widgets,
            plot_function=pandas_plot
            )


def visualize_seaborn(df):
    return UI(
            df,
            generate_widgets=seaborn_arg_widgets,
            plot_function=seaborn_plot
            )


def visualize(df, method='pandas'):
    if method == "pandas":
        return visualize_pandas(df)
    elif method == "seaborn":
        return visualize_seaborn(df)
    else:
        raise ValueError("unsupported method")
