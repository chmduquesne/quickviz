import ipywidgets as widgets
import seaborn


def arg_widgets(df):
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
            #"markers":
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
            #"markers"
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
            "color": widgets.Text(value="g"),
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
            "color": catplot["color"],
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
            "color": catplot["color"],
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
            "color": catplot["color"],
            "palette": relplot["palette"],
            "saturation": widgets.FloatSlider(min=0.0, max=1.0, step=0.05, value=1.0),
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
            "color": catplot["color"],
            "palette": relplot["palette"],
            "saturation": boxplot["saturation"],
        }
    boxenplot = {
            "x": relplot["x"],
            "y": relplot["y"],
            "hue": relplot["hue"],
            #"order","hue_order"
            "orient": catplot["orient"],
            "color": catplot["color"],
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
            #"markers"
            #linestyles
            #"dodge"
            "join": widgets.Checkbox(),
            "scale": widgets.FloatText(value=1.0),
            "orient": catplot["orient"],
            "color": catplot["color"],
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
            "color": catplot["color"],
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
            "color": catplot["color"],
            "palette": relplot["palette"],
            "saturation": boxplot["saturation"],
            #"dodge"
        }
    jointplot = {
            "x": relplot["x"],
            "y": relplot["y"],
            "kind": widgets.Dropdown(options=["scatter", "reg", "resid", "kde", "hex"]),
            #stat_func
            "color": catplot["color"],
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
            #"markers"
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
            "color": catplot["color"],
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
            #"markers",
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
    regplot = {
            "x": relplot["x"],
            "y": relplot["y"],
            #x_estimator
            "x_bins": lmplot["x_bins"],
            "x_ci": lmplot["x_ci"],
            "scatter": lmplot["scatter"],
            "fit_reg": lmplot["fit_reg"],
            "ci": lmplot["ci"],
            "n_boot": lineplot["n_boot"],
            #units
            "order": lmplot["order"],
            "logistic": lmplot["logistic"],
            "lowess": lmplot["lowess"],
            "robust": lmplot["robust"],
            "logx": lmplot["logx"],
            "x_partial": lmplot["x_partial"],
            "y_partial": lmplot["y_partial"],
            "truncate": lmplot["truncate"],
            "x_jitter": lmplot["x_jitter"],
            "y_jitter": lmplot["y_jitter"],
            "label": distplot["label"],
            "color": catplot["color"],
            "marker": widgets.Dropdown(options=['o', 'v', '^', '<', '>', '8', 's', 'p', '*', 'h', 'H', 'D', 'd', 'P', 'X']),
        }
    residplot = {
            "x": relplot["x"],
            "y": relplot["y"],
            "lowess": lmplot["lowess"],
            "x_partial": lmplot["x_partial"],
            "y_partial": lmplot["y_partial"],
            "order": lmplot["order"],
            "robust": lmplot["robust"],
            "dropna": jointplot["dropna"],
            "label": distplot["label"],
            "color": catplot["color"],
        }
    heatmap = {
            "vmin": widgets.FloatText(value=1.0),
            "vmax": widgets.FloatText(value=1.0),
            "cmap": widgets.Text(value="viridis"),
            "center": widgets.FloatText(value=1.0),
            "robust": lmplot["robust"],
            "annot": widgets.Checkbox(),
            "fmt": widgets.Text(),
            "linewidths": widgets.FloatText(value=1.0),
            "linecolor": widgets.Text(),
            "cbar": widgets.Checkbox(),
            "square": widgets.Checkbox(),
            #xticklabels, yticklabels
            #"mask"
        }
    #clustermap = {}
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
        "regplot": regplot,
        "residplot": residplot,
        "heatmap": heatmap,
        #"clustermap": clustermap,
    }


def plot(df, plot_type, kwargs):
    method = getattr(seaborn, plot_type)
    if plot_type not in ["distplot", "kdeplot"]:
        kwargs["data"]=df
    method(**kwargs)
