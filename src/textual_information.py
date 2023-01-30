"""
InfoExtraction: A class for extracting information from a series of reviews.
"""


import abc
import numpy as np
import pandas as pd


class AbstractInfoExtractor(abc.ABC):
    @abc.abstractmethod
    def extract(self) -> pd.Series:
        pass
    

class NumberOfCharactersPerReview(AbstractInfoExtractor):
    """
    Calculates the number of characters in each review.
    
    Returns:
    pd.Series: A series of the number of characters in each review.
    """

    def __init__(self, reviews: pd.Series) -> None:
        self.reviews = reviews
        
    def extract(self) -> pd.Series:
        return self.reviews.map(lambda x: len("".join(x)))


class NumberOfWordsPerReview(AbstractInfoExtractor):
    """
    Calculates the number of words in each review.
    
    Returns:
    pd.Series: A series of the number of words in each review.
    """

    def __init__(self, reviews: pd.Series) -> None:
        self.reviews = reviews
        
    def extract(self) -> pd.Series:
        return self.reviews.str.len()

    
class AverageWordLengthPerReview(AbstractInfoExtractor):
    """
    Calculates the average word length in each review.
    
    Returns:
    pd.Series: A series of the average word length in each review.
    """

    def __init__(self, reviews: pd.Series) -> None:
        self.reviews = reviews
        
    def extract(self) -> pd.Series:
        return self.reviews.apply(lambda x: np.mean([len(i) for i in x]))