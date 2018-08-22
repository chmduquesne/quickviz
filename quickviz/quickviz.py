import matplotlib
import pandas as pd
from IPython.display import display, clear_output
import ipywidgets as widgets
from ipywidgets.widgets.interaction import show_inline_matplotlib_plots


def panda_arg_widgets(df):
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


class UI(object):
    def __init__(self, df):
        self.df = df
        self.arg_widgets = panda_arg_widgets(df)
        self.connected_args = []
        self.connect_widgets()

        self.plot_type_chooser = widgets.Dropdown(options=self.get_plot_types(), description="Plot")
        self.plot_type_chooser.observe(self.redraw, 'value')

        self.add_arg_box = widgets.HBox()
        self.arg_chooser = widgets.Dropdown(description="Controls")
        self.arg_chooser.observe(self.add_arg, 'value')
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

        self.arg_chooser.options = self.get_accepted_args()

    def plot(self, *_):
        method = getattr(self.df.plot, self.plot_type_chooser.value)
        kwargs = {
            arg:self.get_widget(arg).value for arg in self.connected_args
        }
        show_inline_matplotlib_plots()
        with self.output:
            try:
                clear_output(wait=True)
                method(**kwargs)
                show_inline_matplotlib_plots()
            except:
                pass

def visualize(df):
    return UI(df)
