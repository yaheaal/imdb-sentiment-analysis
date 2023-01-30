"""
This module contains three functions that generate different types of plots using the Plotly library.

histplot(data: pd.DataFrame, color: str, title: str) -> None:
This function generates a histogram plot of the input dataframe, with the specified color and title.

bar(data: pd.DataFrame, color: str, x: str, y: str, title: str) -> None:
This function generates a bar chart of the input dataframe, with the specified color, x-axis and y-axis, and title.

tree(data: pd.DataFrame, path: str, values: str, title: str) -> None:
This function generates a treemap plot of the input dataframe, with the specified path, values, and title.
"""


import plotly.express as px
import pandas as pd

def histplot(data: pd.DataFrame, color: str, title: str) -> None:
    fig = px.histogram(data, color_discrete_sequence=[color], title=title)
    fig.show()


def bar(data: pd.DataFrame, color: str, x: str, y: str, title: str) -> None:
    fig = px.bar(data, x=x, y=y, title=title, orientation='h', 
                 width=700, height=700, color=color)
    fig.show()


def tree(data: pd.DataFrame, path: str, values: str, title: str) -> None:
    fig = px.treemap(data, path=[path], values=values, title=title)
    fig.show()