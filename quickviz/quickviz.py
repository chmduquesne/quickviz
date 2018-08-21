import matplotlib
import pandas as pd
from IPython.display import display, clear_output
import ipywidgets as widgets
from ipywidgets.widgets.interaction import show_inline_matplotlib_plots

class UI(object):
    def __init__(self, df):
        self.df = df
        self.arg_widgets = {
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

        self.plot_type_chooser = widgets.Dropdown(options=self.get_plot_types(), description="Plot")
        self.plot_type_chooser.observe(self.redraw)

        self.add_arg_box = widgets.HBox()
        self.arg_chooser = widgets.Dropdown(description="Controls")
        arg_button = widgets.Button(description="add")
        arg_button.on_click(self.add_arg)
        self.add_arg_box.children = [self.arg_chooser, arg_button]

        self.vbox = widgets.VBox()
        self.vbox.children = [self.plot_type_chooser, self.add_arg_box]
        self.args = []
        self.output = widgets.Output()
        display(self.vbox, self.output)
        self.redraw()

    def get_plot_types(self):
        graph_types = list(self.arg_widgets.keys())
        graph_types.remove("*")
        return graph_types

    def get_available_args(self):
        basic_options = list(self.arg_widgets["*"].keys())
        plot_options = list(self.arg_widgets[self.plot_type_chooser.value].keys())
        return basic_options + plot_options

    def add_arg(self, *_):
        if self.arg_chooser.value not in self.args:
            self.args.append(self.arg_chooser.value)
            self.redraw()

    def get_widget(self, arg):
        if arg in self.arg_widgets["*"]:
            return self.arg_widgets["*"][arg]
        else:
            return self.arg_widgets[self.plot_type_chooser.value][arg]

    def add_arg_controller(self, arg):
        w = self.get_widget(arg)
        w.description = arg
        r = widgets.Button(description='remove')
        h = widgets.HBox(children=[w, r])
        def remove(*_):
            for c in h.children:
                if c != w:
                    c.close()
            h.close()
            self.args.remove(arg)
            self.redraw()
        r.on_click(remove)
        return h

    def update_content(self):
        self.args = [a for a in self.args[:] if (a in self.arg_widgets["*"]
                    or a in self.arg_widgets[self.plot_type_chooser.value])]
        lines = []
        lines.append(self.plot_type_chooser)
        for arg in self.args:
            lines.append(self.add_arg_controller(arg))
        lines.append(widgets.HBox([widgets.Label(value="---")]))
        lines.append(self.add_arg_box)
        self.vbox.children = lines

        self.arg_chooser.options = self.get_available_args()

    def connect_controls(self, f):
        controls = dict([(arg, self.get_widget(arg)) for arg in self.args])
        def observer(change):
            kwargs = {k:v.value for k,v in controls.items()}
            show_inline_matplotlib_plots()
            with self.output:
                clear_output(wait=True)
                f(**kwargs)
                show_inline_matplotlib_plots()
        for k,w in controls.items():
            w.observe(observer, 'value')
        show_inline_matplotlib_plots()
        observer(None)

    def redraw(self, *_):
        self.update_content()
        self.connect_controls(self.plot)

    def plot(self, **kwargs):
        method=getattr(self.df.plot, self.plot_type_chooser.value)
        try:
            method(**kwargs)
        except:
            pass


def visualize(df):
    return UI(df)
