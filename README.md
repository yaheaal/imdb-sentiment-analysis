# ๐ Sentiment Analysis Project ๐ค

This README and all the docstring in the code was written by **ChatGPT**

## ๐ Introduction
Sentiment analysis is the ๐ป process of determining the sentiment of a piece of text, whether it is positive, negative, or neutral ๐ค. In this project, we aim to perform sentiment analysis on a dataset of text data ๐ฌ. The problem we are trying to solve is to accurately classify the sentiment of the text and gain insights into the underlying data ๐ก. To achieve this, we propose a solution that involves preprocessing and cleaning the text data ๐งผ, followed by exploratory data analysis ๐ to gain insights. The cleaned and preprocessed data will then be used as input to a sentiment analysis model ๐ง , which will classify the sentiment of the text. This project will demonstrate the importance of thorough preprocessing and EDA in the overall process of sentiment analysis ๐ค.

At the end we will use tfidf and Logistic regression ๐จโ๐ป to train a classification sentiment analysis model ๐ฆพ.

<br>

## ๐ป Requirements
**Python 3.9.6**  
I used **Mac m1**. You can use any PC with any operating system, but of course, you must make some changes to the packages ๐ป  

**Install packages**  
`pip install -r requirements.txt`

<br>

## ๐ Project Structure
A clear and concise description of the project structure, including the 4 folders and main eda.ipynb file ๐พ.


### src Folder
* `constants.py`: Contains all the constants used in the project ๐
* `helpers.py`: Contains helper functions ๐ก
* `positive_negative_split.py`: Helps in splitting the data into positive and negative sentiments ๐ค
* `text_preprocessing.py`: Processes the data for analysis ๐งผ
* `textual_information.py`: Extracts information from the text ๐


### data Link
You can find the data [here](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews) ๐พ


### plot Folder
* `plot_text.py`: Plots text plots ๐
* `word_cloud.py`: Makes wordcloud plots ๐ช๏ธ


### test Folder
* `input_testing.py`: Tests inputs before passing them to a function ๐


### plotly Folder
Contains all the plots made by plotly

<br>

## ๐ Usage
After installing the requirements, you can open eda.ipynb and run it, that's it ๐

<br>

## ๐ Conclusion
Exploratory Data Analysis (EDA) and preprocessing are crucial steps in any data science project ๐ค. In this repository, we focused on cleaning and exploring the text data to gain insights before building the model ๐ง . The preprocessing stage is often the most time-consuming part of a project, but it is also one of the most important ๐ฏ. Proper preprocessing and cleaning of the data ensures that the model is built on quality data, leading to better results ๐ค. In conclusion, the time and effort invested in EDA and preprocessing pays off in the form of a more accurate and robust model ๐ช. This repository serves as a foundation for further analysis and model building, and demonstrates the importance of thorough preprocessing in any data analysis project ๐.

<br>

## ๐ References
This [notebook](https://www.kaggle.com/code/derrelldsouza/imdb-sentiment-analysis-eda-ml-lstm-bert/notebook)
