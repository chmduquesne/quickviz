import matplotlib
import pandas as pd
import ipywidgets as widgets
from . import pandas
from . import seaborn
from IPython.display import display, clear_output
from ipywidgets.widgets.interaction import show_inline_matplotlib_plots


class UI(object):
    def __init__(self, df, gen_widgets, plot):
        self.df = df
        self.manual_kwargs = {}
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
        """
        Make sure that a change to any of the widgets triggers a replot
        """
        for w in self.widgets['*'].values():
            w.observe(self.display_plot, 'value')

    def get_plot_types(self):
        """
        All the plot types
        """
        return sorted([p for p in self.widgets.keys() if p != '*'])

    def get_accepted_args(self):
        """
        Arguments that are accepted by the currently selected plot type
        """
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
        """
        Add the argument selected by the user in the plot arguments
        """
        if self.arg_chooser.value not in self.connected_args:
            self.connected_args.append(self.arg_chooser.value)
            self.redraw()

    def get_widget(self, arg):
        """
        Return the widget associated with the argument. Which widget is
        returned for a given argument name depends on the selected plot
        type.
        """
        p = self.plot_type_chooser.value
        return self.widgets[p][arg]

    def gen_arg_line(self, arg):
        """
        Create a line, ready to be inserted, containing the widget
        associated with  the argument, as well as a remove button. The
        remove button should not only remove the line, but also remove the
        argument from the connected arguments.
        """
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
        """
        Remove from the connected arguments any argument that is
        irrelevant for the current plot type
        """
        self.connected_args = [
            a for a in self.connected_args[:]
            if a in self.get_accepted_args()
        ]

    def save(self):
        """
        Save the UI state in a dictionary
        """
        return {
            'plot': self.plot_type_chooser.value,
            'kwargs': self.kwargs(),
        }

    def load(self, d):
        """
        Load a dictionary into the UI state
        """
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
            self.get_widget(arg).value = value
        self.auto_update.value = True

    def kwargs(self):
        """
        Return a kwarg dictionary associated with the current UI state
        """
        return {
            arg:self.get_widget(arg).value for arg in self.connected_args
        }

    def gen_plot(self):
        """
        Return the plot object associated with the UI state
        """
        kwargs = self.kwargs()
        kwargs.update(**self.manual_kwargs)
        plot_type = self.plot_type_chooser.value
        return self.plot(self.df, plot_type, kwargs)

    def display_plot(self, *_):
        """
        Display the plot object associated with the UI state, unless the
        user does not want interactive updates
        """
        if not self.auto_update.value:
            return
        show_inline_matplotlib_plots()
        with self.output:
            clear_output(wait=True)
            self.gen_plot()
            show_inline_matplotlib_plots()

    def redraw(self, *_):
        """
        Redraw all the UI buttons so that they match the internally
        selected args, then display the plot
        """
        self.filter_connected_args()

        lines = []
        lines.append(self.plot_type_box)
        for arg in self.connected_args:
            lines.append(self.gen_arg_line(arg))
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

        self.display_plot()

    def __add__(self, other):
        """
        Overlays self and other. Probably buggy.
        """
        if not isinstance(other, UI):
            raise TypeError("wrong type for %s" % str(other))
        p = self.gen_plot()
        if not isinstance(p, matplotlib.axes.Axes):
            p = p.ax
        restore = ("ax" in other.manual_kwargs)
        old_ax = other.manual_kwargs.get("ax")
        other.manual_kwargs["ax"] = p
        other.gen_plot()
        if restore:
            other.manual_kwargs["ax"] = old_ax
        else:
            del other.manual_kwargs["ax"]
        return other


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
