import pandas as pd
import ipywidgets as widgets
from . import pandas
from . import seaborn
from ipywidgets.widgets.interaction import show_inline_matplotlib_plots
from IPython.display import display, clear_output


class UI(object):
    def __init__(self, df, generate_widgets, plot_function):
        self.df = df
        self.arg_widgets = generate_widgets(df)
        self.plot_function = plot_function
        self.connected_args = []
        self.connect_widgets()

        self.plot_type_box = widgets.HBox()
        self.plot_type_chooser = widgets.Dropdown(options=self.get_plot_types(), description='Plot type')
        self.auto_update = widgets.Checkbox(description='auto-update')
        self.plot_type_box.children = [self.plot_type_chooser, self.auto_update]
        self.plot_type_chooser.observe(self.redraw, 'value')
        self.auto_update.observe(self.redraw, 'value')

        self.add_arg_box = widgets.HBox()
        self.arg_chooser = widgets.Dropdown(description='Add arg')
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
        args  = [(a, a) for a in sorted(self.arg_widgets['*'].keys())]
        p = self.plot_type_chooser.value
        args += [(a, a) for a in sorted(self.arg_widgets[p].keys())]
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
        if arg in self.arg_widgets['*']:
            return self.arg_widgets['*'][arg]
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
        lines.append(self.plot_type_box)
        for arg in self.connected_args:
            lines.append(self.arg_controller(arg))
        lines.append(widgets.HBox([widgets.Label(value='---')]))
        lines.append(self.add_arg_box)
        self.vbox.children = lines

        arg_choice = self.arg_chooser.value
        try:
            self.arg_chooser.unobserve(self.add_arg, 'value')
        except ValueError:
            pass
        self.arg_chooser.options = self.get_accepted_args()
        if arg_choice in dict(self.get_accepted_args()).values():
            self.arg_chooser.value = arg_choice
        else:
            self.arg_chooser.value = None
        self.arg_chooser.observe(self.add_arg, 'value')
        self.plot()

    def get_controller(self, name):
        for h in self.vbox.children:
            w = h.children[0]
            if w.description == name:
                return w
        raise KeyError("No controller for name %s" % name)

    def get_plot_parameters(self):
        plot_type = self.plot_type_chooser.value
        kwargs = {
            arg:self.get_widget(arg).value for arg in self.connected_args
        }
        return (plot_type, kwargs)

    def plot(self, *_):
        if not self.auto_update.value:
            return
        plot_type, kwargs = self.get_plot_parameters()
        show_inline_matplotlib_plots()
        with self.output:
            clear_output(wait=True)
            self.plot_function(
                    self.df,
                    plot_type,
                    kwargs)
            show_inline_matplotlib_plots()


def visualize_pandas(df):
    return UI(
            df,
            generate_widgets=pandas.arg_widgets,
            plot_function=pandas.plot
            )


def visualize_seaborn(df):
    return UI(
            df,
            generate_widgets=seaborn.arg_widgets,
            plot_function=seaborn.plot
            )


def visualize(df, method='seaborn'):
    if not isinstance(df, pd.core.frame.DataFrame):
        raise TypeError('The argument must be a pandas dataframes')
    if method == 'pandas':
        return visualize_pandas(df)
    elif method == 'seaborn':
        return visualize_seaborn(df)
    else:
        raise ValueError('unsupported method')
