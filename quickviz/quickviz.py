import pandas as pd
import ipywidgets as widgets
from . import pandas
from . import seaborn
from ipywidgets.widgets.interaction import show_inline_matplotlib_plots
from IPython.display import display, clear_output


class UI(object):
    def __init__(self, df, gen_widgets, plot):
        self.df = df
        self.widgets = gen_widgets(df)
        self.plot = plot
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
        self.arg_chooser.observe(self.add_arg, 'value')

        self.vbox = widgets.VBox()
        self.output = widgets.Output()

        display(self.vbox, self.output)
        self.redraw()

    def connect_widgets(self):
        for w in self.widgets['*'].values():
            w.observe(self._plot, 'value')

    def get_plot_types(self):
        return sorted([p for p in self.widgets.keys() if p != '*'])

    def get_accepted_args(self):
        p = self.plot_type_chooser.value
        args = sorted(self.widgets[p].keys())
        # place the most useful arguments on top
        top = ['x', 'y']
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
        p = self.plot_type_chooser.value
        return self.widgets[p][arg]

    def arg_controller(self, arg):
        w = self.get_widget(arg)
        w.description = arg
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
            if a in self.get_accepted_args()
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
        # avoid accidentally adding args during redraw
        self.arg_chooser.unobserve(self.add_arg, 'value')
        self.arg_chooser.options = self.get_accepted_args()
        # restore choice if possible
        if arg_choice in self.get_accepted_args():
            self.arg_chooser.value = arg_choice
        else:
            self.arg_chooser.value = None
        self.arg_chooser.observe(self.add_arg, 'value')

        self._plot()

    def save(self):
        return {
            'plot': self.plot_type_chooser.value,
            'kwargs': self._kwargs(),
        }

    def load(self, d):
        for k in d.keys():
            if k not in ['plot', 'kwargs']:
                raise ValueError('%s: unexpected key')
        plot = d['plot']
        if plot not in self.get_plot_types():
            raise ValueError('%s: not an acceptable plot type' % plot)
        self.plot_type_chooser.value = plot
        for arg in d['kwargs'].keys():
            if arg not in self.get_accepted_args():
                raise ValueError('%s: not an acceptable arg' % arg)
        self.connected_args = list(d['kwargs'].keys())
        self.redraw()
        for arg, value in d['kwargs'].items():
            self.get_controller(arg).value = value

    def get_controller(self, name):
        for h in self.vbox.children:
            w = h.children[0]
            if w.description == name:
                return w
        raise KeyError("No controller for name %s" % name)

    def _kwargs(self):
        return {
            arg:self.get_widget(arg).value for arg in self.connected_args
        }

    def _plot(self, *_):
        if not self.auto_update.value:
            return
        kwargs = self._kwargs()
        plot_type = self.plot_type_chooser.value
        show_inline_matplotlib_plots()
        with self.output:
            clear_output(wait=True)
            self.plot(
                    self.df,
                    plot_type,
                    kwargs)
            show_inline_matplotlib_plots()


def visualize_pandas(df):
    return UI(
            df,
            gen_widgets=pandas.gen_widgets,
            plot=pandas.plot
            )


def visualize_seaborn(df):
    return UI(
            df,
            gen_widgets=seaborn.gen_widgets,
            plot=seaborn.plot
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
