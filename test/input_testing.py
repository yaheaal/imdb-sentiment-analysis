"""
The module contains utility functions for validating the
types of inputs passed to other functions.

The is_pandas_series() function takes a pandas Series and
a message string as input, and raises a TypeError if the
passed object is not a pandas Series.

The is_list() function takes a list and a message string as input,
and raises a TypeError if the passed object is not a list.

The is_pandas_series_of_lists() function takes a pandas Series and
a message string as input, and raises a TypeError if the passed
Series is not a series of lists.

The is_list_of_strings() function takes a list and a message string as input,
and raises a TypeError if the passed list is not a list of strings.

These functions are used to ensure that the input passed to other functions in the module conform to the expected types.
"""


import pandas as pd

def is_pandas_series(series: pd.Series, message: str) -> None:
    if not type(series) is pd.Series:
        raise TypeError(f"{message}")


def is_list(list_: list, message: str) -> None:
    if not type(list_) is list:
        raise TypeError(f'{message}')
    

def is_pandas_series_of_lists(series: pd.Series, message: str) -> None:
    is_pandas_series(series, message)

    is_series_of_lists = all(map(lambda row: isinstance(row, list), series))
    if not is_series_of_lists:
        raise TypeError(f"{message}")
    

def is_list_of_strings(list_: list[str], message: str) -> None:
    is_list(list_, message)
    
    is_list_of_strings = all([isinstance(element, str) for element in list_])
    if not is_list_of_strings:
        raise TypeError(f'{message}')