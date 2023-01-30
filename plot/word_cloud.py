from wordcloud import WordCloud
import matplotlib.pyplot as plt

def plot_wordcloud(data: str, title: str) -> None:
    wordcloud = WordCloud(
        background_color='white',
        max_words=200,
        width=1200,
        height=600,
    ).generate(str(data))

    fig = plt.figure(figsize=(20, 20))
    
    plt.axis('off')
    fig.suptitle(title, fontsize=20)
    fig.subplots_adjust(top=2.3)

    plt.imshow(wordcloud)
    plt.show()     