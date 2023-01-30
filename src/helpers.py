"""
This module provides functions for processing text data in a pandas Series.

Functions:
    split_reviews_to_words(series: pd.Series) -> list[str]:
        Splits a pandas series of lists into individual words.
    
    top_n_words(all_words: list[str], n_words: int=10) -> list[tuple[str, int]]:
        Finds the top n most common words in a list of words.
    
    series_lists_to_series_str(series: pd.Series) -> pd.Series:
        Converts a pandas series of lists to a pandas series of strings.
    
    series_str_to_one_str(series: pd.Series) -> str:
        Concatenates all strings in a pandas series into a single string.

"""


from test.input_testing import is_pandas_series_of_lists, is_list_of_strings, is_pandas_series
from collections import Counter
import pandas as pd



def split_reviews_to_words(series: pd.Series) -> list[str]:
    """
    Splits a pandas series of lists into individual words.

    Args:
        series (pd.Series): A pandas series of lists.
    
    Returns:
        list[str]: A list of individual words.

    Raises:
        TypeError: If `series` is not a pandas series of lists.
        TypeError: If `all_words` is not a list of strings.
    """

    is_pandas_series_of_lists(series, message='Input must be a pandas series of lists')

    all_words = [word for row in series for word in row]
    
    is_list_of_strings(all_words, message='Input must be a list of strings')

    return all_words


def top_n_words(all_words: list[str], n_words: int=10) -> list[tuple[str, int]]:
    """
    Finds the top n most common words in a list of words.

    Args:
        all_words (list[str]): A list of words.
        n_words (int, optional): The number of top words to return. Defaults to 10.
    
    Returns:
        list[tuple[str, int]]: A list of top n words and their frequency.

    Raises:
        TypeError: If `all_words` is not a list of strings.
    """

    is_list_of_strings(all_words, message='Input must be a list of strings')

    counter = Counter(all_words)
    most_common = counter.most_common(n_words)
    return most_common


def series_lists_to_series_str(series: pd.Series) -> pd.Series:
    """
    Converts a pandas series of lists to a pandas series of strings.

    Args:
        series (pd.Series): A pandas series of lists.
    
    Returns:
        pd.Series: A pandas series of strings.

    Raises:
        TypeError: If `series` is not a pandas series of lists.
    """

    is_pandas_series_of_lists(series, message='Input must be a pandas series of lists')
    return series.apply(lambda x: ' '.join(x))


def series_str_to_one_str(series: pd.Series) -> str:
    """
    Convert a pandas series of strings to a single string.

    Args:
        series (pd.Series): A pandas series of strings.
    
    Returns:
        pd.Series: One single string.

    Raises:
        TypeError: If `series` is not a pandas series.
    """

    is_pandas_series(series, message='Input must be a pandas series')
    return " ".join(v for v in series)
