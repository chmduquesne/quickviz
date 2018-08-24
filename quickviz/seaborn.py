import ipywidgets as widgets
import seaborn


def gen_widgets(df):
    """
    Returns a dictionary of dictionaries

    The dictionary '*' contains all the widgets. The keys don't matter in
    the UI.

    All other dictionaries are named after the plot they represent. They
    map their arguments to widgets defined in '*'.
    """
    w = {
        "a": widgets.Dropdown(options=[(col, list(df[col])) for col in list(df)]),
        "alpha": widgets.FloatSlider(min=0.0, max=1.0, step=0.05),
        "annot": widgets.Checkbox(),
        "aspect": widgets.FloatText(value=1),
        "axlabel": widgets.Text(),
        "bins": widgets.IntText(value=10),
        "bw": widgets.Dropdown(options=["scott", "silverman"]),
        "capsize": widgets.FloatText(value=1.0),
        "cbar": widgets.Checkbox(),
        "cbar": widgets.Checkbox(),
        "cbar_ax": widgets.Checkbox(),
        "center": widgets.FloatText(value=1.0),
        "ci": widgets.FloatSlider(min=0, max=100, value=95, step=0.1),
        "cmap": widgets.Text(value="viridis"),
        "col": widgets.Dropdown(options=list(df)),
        "col_wrap": widgets.IntText(value=10),
        "color": widgets.Text(value="g"),
        "cumulative": widgets.Checkbox(),
        "cut": widgets.FloatText(value=1.0),
        "data": widgets.Dropdown(options=[(col, list(df[col])) for col in list(df)]),
        "data2": widgets.Dropdown(options=[(col, list(df[col])) for col in list(df)]),
        "diag_kind": widgets.Dropdown(options=["auto", "hist", "kde"]),
        "dropna": widgets.Checkbox(),
        "edgecolor": widgets.Text(value="gray"),
        "err_style": widgets.Dropdown(options=["band", "bars"]),
        "errwidth": widgets.FloatText(value=1.0),
        "fit_reg": widgets.Checkbox(),
        "fliersize": widgets.FloatText(value=1.0),
        "fmt": widgets.Text(value=".2g"),
        "gridsize": widgets.IntText(value=100),
        "height": widgets.FloatText(value=5),
        "hist": widgets.Checkbox(),
        "hue": widgets.Dropdown(options=list(df)),
        "inner": widgets.Dropdown(options=["box", "quartile", "point", "stick"]),
        "jitter": widgets.Checkbox(),
        "join": widgets.Checkbox(),
        "k_depth": widgets.Dropdown(options=["proportion", "tukey", "trustworthy"]),
        "kde": widgets.Checkbox(),
        "kernel": widgets.Dropdown(options=['gau', 'cos', 'biw', 'epa', 'tri', 'triw']),
        "kind_catplot": widgets.Dropdown(options=["point", "bar", "strip", "swarm", "box", "violin", "boxen"]),
        "kind_jointplot": widgets.Dropdown(options=["scatter", "reg", "resid", "kde", "hex"]),
        "kind_pairplot": widgets.Dropdown(options=["scatter", "reg"]),
        "kind_relplot": widgets.Dropdown(options=["scatter", "line"]),
        "label": widgets.Text(),
        "legend": widgets.Dropdown(options={"brief": "brief", "full":"full", "False": False}),
        "legend_out": widgets.Checkbox(),
        "linecolor": widgets.Text("white"),
        "linewidth": widgets.FloatText(value=1.0),
        "linewidths": widgets.FloatText(value=0.0, step=0.01),
        "logistic": widgets.Checkbox(),
        "logx": widgets.Checkbox(),
        "lowess": widgets.Checkbox(),
        "margin_titles": widgets.Checkbox(),
        "marker": widgets.Dropdown(options=['o', 'v', '^', '<', '>', '8', 's', 'p', '*', 'h', 'H', 'D', 'd', 'P', 'X']),
        "n_boot": widgets.IntText(value=1000),
        "norm_hist": widgets.Checkbox(),
        "notch": widgets.Checkbox(),
        "order_regression": widgets.IntText(value=1),
        "orient": widgets.Dropdown(options=["v", "h"]),
        "outlier_prop": widgets.FloatSlider(min=0.0, max=1.0, step=0.001, value=0.007),
        "palette": widgets.Text(),
        "ratio": widgets.IntText(value=5),
        "robust": widgets.Checkbox(),
        "row": widgets.Dropdown(options=list(df)),
        "rug": widgets.Checkbox(),
        "saturation": widgets.FloatSlider(min=0.0, max=1.0, step=0.05, value=1.0),
        "scale_boxenplot": widgets.Dropdown(options=["linear", "exponential", "area"]),
        "scale_float": widgets.FloatText(value=1.0),
        "scale_hue": widgets.Checkbox(),
        "scale_violinplot": widgets.Dropdown(options=["area", "count", "width"]),
        "scatter": widgets.Checkbox(),
        "shade": widgets.Checkbox(),
        "shade_lowest": widgets.Checkbox(),
        "sharex": widgets.Dropdown(options={"True": True, "col": "col", "row": "row"}),
        "sharey": widgets.Dropdown(options={"True": True, "col": "col", "row": "row"}),
        "size_float": widgets.FloatText(value=1.0),
        "size_vector": widgets.Dropdown(options=list(df)),
        "sort": widgets.Checkbox(),
        "space": widgets.FloatText(value=.2),
        "split": widgets.Checkbox(),
        "square": widgets.Checkbox(),
        "style": widgets.Dropdown(options=list(df)),
        "truncate": widgets.Checkbox(),
        "units": widgets.Dropdown(options=list(df)),
        "vertical": widgets.Checkbox(),
        "vmax": widgets.FloatText(value=1.0, step=0.1),
        "vmin": widgets.FloatText(value=1.0, step=0.1),
        "whis":  widgets.FloatText(value=1.0),
        "width": widgets.FloatText(value=1.0),
        "x": widgets.Dropdown(options=list(df)),
        "x_bins": widgets.IntText(value=10),
        "x_ci": widgets.IntSlider(min=0, max=100, value=95),
        "x_jitter": widgets.FloatText(value=.1),
        "x_partial": widgets.Dropdown(options=list(df)),
        "y": widgets.Dropdown(options=list(df)),
        "y_jitter": widgets.FloatText(value=.1),
        "y_partial": widgets.Dropdown(options=list(df)),
    }
    relplot = {
        "x": w["x"],
        "y": w["y"],
        "hue": w["hue"],
        "size": w["size_vector"],
        "style": w["style"],
        "row": w["row"],
        "col": w["col"],
        "col_wrap": w["col_wrap"],
        #"row_order":
        #"col_order":
        "palette": w["palette"],
        #"hue_order":
        #"hue_norm":
        #"sizes"
        #"size_order":
        #"size_norm":
        "legend": w["legend"],
        "kind": w["kind_relplot"],
        "height": w["height"],
        "aspect": w["aspect"],
    }
    scatterplot = {
        "x": w["x"],
        "y": w["y"],
        "hue": w["hue"],
        "size": w["size_vector"],
        "style": w["style"],
        "palette": w["palette"],
        #"hue_order":
        #"hue_norm":
        #"sizes": w["sizes"],
        #"size_order":
        #"size_norm":
        #"markers":
        #"style_order":
        #"{x,y}_bins": (non functional)
        #"units": (non functional)
        #"estimator": (non functional)
        #"ci": (non functional)
        #"n_boot": (non functional)
        "alpha": w["alpha"],
        #"{x,y}_jitter": (non functional)
        "legend": w["legend"],
    }
    lineplot = {
        "x": w["x"],
        "y": w["y"],
        "hue": w["hue"],
        "size": w["size_vector"],
        "style": w["style"],
        "palette": w["palette"],
        #"hue_order":
        #"hue_norm":
        #"sizes",
        #"dashes":,
        #"markers"
        #"style_order":
        "units": w["units"],
        #"estimator"
        "ci": w["ci"],
        "n_boot": w["n_boot"],
        "sort": w["sort"],
        "err_style": w["err_style"],
        "legend": w["legend"],
    }
    catplot = {
        "x": w["x"],
        "y": w["y"],
        "row": w["row"],
        "col": w["col"],
        "col_wrap": w["col_wrap"],
        #"estimator"
        "ci": w["ci"],
        "n_boot": w["n_boot"],
        "units": w["units"],
        #"order","hue_order"
        #"row_order","col_order"
        "kind": w["kind_catplot"],
        "height": w["height"],
        "aspect": w["aspect"],
        "orient": w["orient"],
        "color": w["color"],
        "palette": w["palette"],
        "legend": w["legend"],
        "legend_out": w["legend_out"],
        "sharex": w["sharex"],
        "sharey": w["sharey"],
        "margin_titles": w["margin_titles"],
    }
    stripplot = {
        "x": w["x"],
        "y": w["y"],
        #"order","hue_order"
        "jitter": w["jitter"],
        #"dodge"
        "orient": w["orient"],
        "color": w["color"],
        "palette": w["palette"],
        "size": w["size_float"],
        "edgecolor": w["edgecolor"],
        "linewidth": w["linewidth"],
    }
    swarmplot = {
        "x": w["x"],
        "y": w["y"],
        #"order","hue_order"
        #"dodge"
        "orient": w["orient"],
        "color": w["color"],
        "palette": w["palette"],
        "size": w["size_float"],
        "edgecolor": w["edgecolor"],
        "linewidth": w["linewidth"],
    }
    boxplot = {
        "x": w["x"],
        "y": w["y"],
        #"order","hue_order"
        "orient": w["orient"],
        "color": w["color"],
        "palette": w["palette"],
        "saturation": w["saturation"],
        "width": w["width"],
        #"dodge"
        "fliersize": w["fliersize"],
        "linewidth": w["linewidth"],
        "whis":  w["whis"],
        "notch": w["notch"],
    }
    violinplot = {
        "x": w["x"],
        "y": w["y"],
        "hue": w["hue"],
        #"order","hue_order"
        "bw": w["bw"],
        "cut": w["cut"],
        "scale": w["scale_violinplot"],
        "scale_hue": w["scale_hue"],
        "gridsize": w["gridsize"],
        "width": w["width"],
        "inner": w["inner"],
        "split": w["split"],
        #"dodge"
        "orient": w["orient"],
        "linewidth": w["linewidth"],
        "color": w["color"],
        "palette": w["palette"],
        "saturation": w["saturation"],
    }
    boxenplot = {
        "x": w["x"],
        "y": w["y"],
        "hue": w["hue"],
        #"order","hue_order"
        "orient": w["orient"],
        "color": w["color"],
        "palette": w["palette"],
        "saturation": w["saturation"],
        "width": w["width"],
        #"dodge"
        "k_depth": w["k_depth"],
        "linewidth": w["linewidth"],
        "scale":  w["scale_boxenplot"],
        "outlier_prop": w["outlier_prop"],
    }
    pointplot = {
        "x": w["x"],
        "y": w["y"],
        "hue": w["hue"],
        #"order","hue_order"
        #"estimator"
        "ci": w["ci"],
        "n_boot": w["n_boot"],
        "units": w["units"],
        #"markers"
        #linestyles
        #"dodge"
        "join": w["join"],
        "scale": w["scale_float"],
        "orient": w["orient"],
        "color": w["color"],
        "palette": w["palette"],
        "errwidth": w["errwidth"],
        "capsize": w["capsize"],
    }
    barplot = {
        "x": w["x"],
        "y": w["y"],
        "hue": w["hue"],
        #"order","hue_order"
        #"estimator"
        "ci": w["ci"],
        "n_boot": w["n_boot"],
        "units": w["units"],
        "orient": w["orient"],
        "color": w["color"],
        "palette": w["palette"],
        "saturation": w["saturation"],
        #"errcolor"
        "errwidth": w["errwidth"],
        "capsize": w["capsize"],
        #"dodge"
    }
    countplot = {
        "x": w["x"],
        "y": w["y"],
        "hue": w["hue"],
        #"order","hue_order"
        "orient": w["orient"],
        "color": w["color"],
        "palette": w["palette"],
        "saturation": w["saturation"],
        #"dodge"
    }
    jointplot = {
        "x": w["x"],
        "y": w["y"],
        "kind": w["kind_jointplot"],
        #stat_func
        "color": w["color"],
        "height": w["height"],
        "ratio": w["ratio"],
        "space": w["space"],
        "dropna": w["dropna"],
        #"xlim"
        #"ylim"
    }
    pairplot = {
        "hue": w["hue"],
        #hue_order
        "palette": w["palette"],
        #vars
        #x_vars
        #y_vars
        "kind": w["kind_pairplot"],
        "diag_kind": w["diag_kind"],
        #"markers"
        "height": w["height"],
        "aspect": w["aspect"],
        "dropna": w["dropna"],
    }
    distplot = {
        "a": w["a"],
        "bins": w["bins"],
        "hist": w["hist"],
        "kde": w["kde"],
        "rug": w["rug"],
        #"fit"
        #{hist, kde, rug, fit}_kws
        "color": w["color"],
        "vertical": w["vertical"],
        "norm_hist": w["norm_hist"],
        "axlabel": w["axlabel"],
        "label": w["label"],
    }
    kdeplot = {
        "data": w["data"],
        "data2": w["data2"],
        "shade": w["shade"],
        "vertical": w["vertical"],
        "kernel": w["kernel"],
        "bw": w["bw"],
        "gridsize": w["gridsize"],
        "cut": w["cut"],
        #"clip":
        "legend": w["legend"],
        "cumulative": w["cumulative"],
        "shade_lowest": w["shade_lowest"],
        "cbar": w["cbar"],
        "cbar_ax": w["cbar_ax"],
    }
    lmplot = {
        "x": w["x"],
        "y": w["y"],
        "hue": w["hue"],
        "col": w["col"],
        "row": w["row"],
        "palette": w["palette"],
        "col_wrap": w["col_wrap"],
        "height": w["height"],
        "aspect": w["aspect"],
        #"markers",
        "sharex": w["sharex"],
        "sharey": w["sharey"],
        "legend": w["legend"],
        "legend_out": w["legend_out"],
        #x_estimator
        "x_bins": w["x_bins"],
        "x_ci": w["x_ci"],
        "scatter": w["scatter"],
        "fit_reg": w["fit_reg"],
        "ci": w["ci"],
        "n_boot": w["n_boot"],
        "units": w["units"],
        "order": w["order_regression"],
        "logistic": w["logistic"],
        "lowess": w["lowess"],
        "robust": w["robust"],
        "logx": w["logx"],
        "x_partial": w["x_partial"],
        "y_partial": w["y_partial"],
        "truncate": w["truncate"],
        "x_jitter": w["x_jitter"],
        "y_jitter": w["y_jitter"],
    }
    regplot = {
        "x": w["x"],
        "y": w["y"],
        #x_estimator
        "x_bins": w["x_bins"],
        "x_ci": w["x_ci"],
        "scatter": w["scatter"],
        "fit_reg": w["fit_reg"],
        "ci": w["ci"],
        "n_boot": w["n_boot"],
        "units": w["units"],
        "order": w["order_regression"],
        "logistic": w["logistic"],
        "lowess": w["lowess"],
        "robust": w["robust"],
        "logx": w["logx"],
        "x_partial": w["x_partial"],
        "y_partial": w["y_partial"],
        "truncate": w["truncate"],
        "x_jitter": w["x_jitter"],
        "y_jitter": w["y_jitter"],
        "label": w["label"],
        "color": w["color"],
        "marker": w["marker"],
    }
    residplot = {
        "x": w["x"],
        "y": w["y"],
        "lowess": w["lowess"],
        "x_partial": w["x_partial"],
        "y_partial": w["y_partial"],
        "order": w["order_regression"],
        "robust": w["robust"],
        "dropna": w["dropna"],
        "label": w["label"],
        "color": w["color"],
    }
    heatmap = {
        "vmin": w["vmin"],
        "vmax": w["vmax"],
        "cmap": w["cmap"],
        "center": w["center"],
        "robust": w["robust"],
        "annot": w["annot"],
        "fmt": w["fmt"],
        "linewidths": w["linewidths"],
        "linecolor": w["linecolor"],
        "cbar": w["cbar"],
        "square": w["square"],
        #xticklabels, yticklabels
        #"mask"
    }
    #clustermap = {}
    return {
        "*": w,
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
