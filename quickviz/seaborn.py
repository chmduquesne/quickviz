import ipywidgets as widgets
import seaborn


def arg_widgets(df):
    w = {
            "x": widgets.Dropdown(options=list(df)),
            "y": widgets.Dropdown(options=list(df)),
            "hue": widgets.Dropdown(options=list(df)),
            "size_vector": widgets.Dropdown(options=list(df)),
            "size_float": widgets.FloatText(value=1.0),
            "style": widgets.Dropdown(options=list(df)),
            "row": widgets.Dropdown(options=list(df)),
            "col": widgets.Dropdown(options=list(df)),
            "col_wrap": widgets.IntText(value=10),
            "palette": widgets.Text(),
            "legend": widgets.Dropdown(options={"brief": "brief", "full":"full", "False": False}),
            "legend_out": widgets.Checkbox(),
            "kind_relplot": widgets.Dropdown(options=["scatter", "line"]),
            "kind_catplot": widgets.Dropdown(options=["point", "bar", "strip", "swarm", "box", "violin", "boxen"]),
            "alpha": widgets.FloatSlider(min=0.0, max=1.0, step=0.05),
            "n_boot": widgets.IntText(value=1000),
            "sort": widgets.Checkbox(),
            "err_style": widgets.Dropdown(options=["band", "bars"]),
            "orient": widgets.Dropdown(options=["v", "h"]),
            "color": widgets.Text(value="g"),
            "sharex": widgets.Dropdown(options={"True": True, "col": "col", "row": "row"}),
            "sharey": widgets.Dropdown(options={"True": True, "col": "col", "row": "row"}),
            "margin_titles": widgets.Checkbox(),
            "jitter": widgets.Checkbox(),
            "linewidth": widgets.FloatText(value=1.0),
            "saturation": widgets.FloatSlider(min=0.0, max=1.0, step=0.05, value=1.0),
            "width": widgets.FloatText(value=1.0),
            "fliersize": widgets.FloatText(value=1.0),
            "whis":  widgets.FloatText(value=1.0),
            "notch": widgets.Checkbox(),
            "bw": widgets.Dropdown(options=["scott", "silverman"]),
            "cut": widgets.FloatText(value=1.0),
            "scale_violinplot": widgets.Dropdown(options=["area", "count", "width"]),
            "scale_hue": widgets.Checkbox(),
            "gridsize": widgets.IntText(value=100),
            "inner": widgets.Dropdown(options=["box", "quartile", "point", "stick"]),
            "split": widgets.Checkbox(),
            "k_depth": widgets.Dropdown(options=["proportion", "tukey", "trustworthy"]),
            "scale_boxenplot": widgets.Dropdown(options=["linear", "exponential", "area"]),
            "outlier_prop": widgets.FloatSlider(min=0.0, max=1.0, step=0.001, value=0.007),
            "join": widgets.Checkbox(),
            "scale_float": widgets.FloatText(value=1.0),
            "errwidth": widgets.FloatText(value=1.0),
            "capsize": widgets.FloatText(value=1.0),
            "kind_jointplot": widgets.Dropdown(options=["scatter", "reg", "resid", "kde", "hex"]),
            "height": widgets.FloatText(value=5),
            "aspect": widgets.FloatText(value=1),
            "ratio": widgets.IntText(value=5),
            "space": widgets.FloatText(value=.2),
            "dropna": widgets.Checkbox(),
            "kind_pairplot": widgets.Dropdown(options=["scatter", "reg"]),
            "diag_kind": widgets.Dropdown(options=["auto", "hist", "kde"]),
            "edgecolor": widgets.Text(value="gray"),
            "a": widgets.Dropdown(options=[(col, list(df[col])) for col in list(df)]),
            "bins": widgets.IntText(value=10),
            "hist": widgets.Checkbox(),
            "kde": widgets.Checkbox(),
            "rug": widgets.Checkbox(),
            "vertical": widgets.Checkbox(),
            "norm_hist": widgets.Checkbox(),
            "axlabel": widgets.Text(),
            "label": widgets.Text(),
            "data": widgets.Dropdown(options=[(col, list(df[col])) for col in list(df)]),
            "data2": widgets.Dropdown(options=[(col, list(df[col])) for col in list(df)]),
            "shade": widgets.Checkbox(),
            "kernel": widgets.Dropdown(options=['gau', 'cos', 'biw', 'epa', 'tri', 'triw']),
            "cumulative": widgets.Checkbox(),
            "shade_lowest": widgets.Checkbox(),
            "cbar": widgets.Checkbox(),
            "cbar_ax": widgets.Checkbox(),
            "x_bins": widgets.IntText(value=10),
            "x_ci": widgets.IntSlider(min=0, max=100, value=95),
            "scatter": widgets.Checkbox(),
            "fit_reg": widgets.Checkbox(),
            "ci": widgets.FloatSlider(min=0, max=100, value=95, step=0.1),
            "order_regression": widgets.IntText(value=1),
            "logistic": widgets.Checkbox(),
            "lowess": widgets.Checkbox(),
            "robust": widgets.Checkbox(),
            "logx": widgets.Checkbox(),
            "x_partial": widgets.Dropdown(options=list(df)),
            "y_partial": widgets.Dropdown(options=list(df)),
            "truncate": widgets.Checkbox(),
            "x_jitter": widgets.FloatText(value=.1),
            "y_jitter": widgets.FloatText(value=.1),
            "marker": widgets.Dropdown(options=['o', 'v', '^', '<', '>', '8', 's', 'p', '*', 'h', 'H', 'D', 'd', 'P', 'X']),
            "vmin": widgets.FloatText(value=1.0, step=0.1),
            "vmax": widgets.FloatText(value=1.0, step=0.1),
            "cmap": widgets.Text(value="viridis"),
            "center": widgets.FloatText(value=1.0),
            "annot": widgets.Checkbox(),
            "fmt": widgets.Text(value=".2g"),
            "linewidths": widgets.FloatText(value=0.0, step=0.01),
            "linecolor": widgets.Text("white"),
            "cbar": widgets.Checkbox(),
            "square": widgets.Checkbox(),
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
            #"units": (non functional)
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
            #"units"
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
            #"units"
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
            #"units"
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
            #units
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
            #units
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
