Quickviz
========

Quickviz provides widgets for quickly visualizing pandas dataframes.

How to use it
-------------

    %matplotlib inline
    from quickviz import visualize as v
    from vega_datasets import data
    v(data.iris(), method="seaborn") # or method="pandas"

Installation
------------

    pip install ipywidgets
    jupyter nbextension enable --py widgetsnbextension
    pip install quickviz

Examples
--------

See the [gallery](https://nbviewer.jupyter.org/github/chmduquesne/quickviz/tree/master/examples/).

Disclaimer
----------

Quickviz does not read the documentation for you! It only makes it easier
to use seaborn/pandas with a mouse. In order to understand what you are
doing, you still need to dig in their respective APIs.
