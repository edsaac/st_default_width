import streamlit as st
from functools import partial
from types import MethodType

CALLABLES_WITH_ADJUSTABLE_WIDTH = [
    "altair_chart",
    "area_chart",
    "bar_chart",
    "bokeh_chart",
    "button",
    "dataframe",
    "data_editor",
    "download_button",
    "pydeck_chart",
    "form_submit_button",
    "graphviz_chart",
    "image",
    "line_chart",
    "link_button",
    "map",
    "page_link",
    "plotly_chart",
    "popover",
    "pyplot",
    "scatter_chart",
    "vega_lite_chart",
]


def set_use_container_width_default(default: bool = True):
    for func_name in CALLABLES_WITH_ADJUSTABLE_WIDTH:
        kwarg = "use_column_width" if func_name == "image" else "use_container_width"
        func = st.__dict__[func_name]

        if isinstance(func, MethodType):
            st.__dict__[func_name] = partial(func, **{kwarg: default})

        elif isinstance(func, partial):
            if func.keywords[kwarg] != default:
                st.__dict__[func_name].keywords[kwarg] = default


def revert_use_container_width_default():
    for func_name in CALLABLES_WITH_ADJUSTABLE_WIDTH:
        func = st.__dict__[func_name]

        if isinstance(func, partial):
            st.__dict__[func_name] = func.func
