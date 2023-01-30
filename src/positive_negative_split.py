"""
This module contains a class called PositiveNegativeSplit that separates positive and negative reviews from a given dataframe.
"""


from src.constant import POSITIVE_NEGATIVE_MAP
import pandas as pd

class PositiveNegativeSplit:
    def __init__(self, data: pd.DataFrame, text_column: str, label_column: str) -> None:
        """
        Initializes an instance of the class with a DataFrame, the name of the text column, and the name of the label column.
        """

        self.data = data
        self.text_column = text_column
        self.label_column = label_column

    def split(self, sentiment: str) -> pd.Series:
        """
        This function separates the reviews in the DataFrame based on the specified sentiment.
        It returns a pandas series of the text of the reviews that match the sentiment.

        """

        label =  POSITIVE_NEGATIVE_MAP.get(sentiment)
        if not label:
            raise ValueError(f"Sentiment must be one of {list(POSITIVE_NEGATIVE_MAP.keys())}")

        filter = self.data[self.label_column] == label
        reviews = self.data[filter][self.text_column]
        return reviews